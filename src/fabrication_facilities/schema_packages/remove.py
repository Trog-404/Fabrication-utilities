#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
from typing import (
    TYPE_CHECKING,
)

import numpy as np
from ase.data import atomic_masses as am
from ase.data import atomic_numbers as an
from nomad.datamodel.data import (
    ArchiveSection,
)
from nomad.datamodel.metainfo.basesections import ElementalComposition
from nomad.datamodel.metainfo.eln import Chemical
from nomad.metainfo import (
    MEnum,
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.fabrication_utilities import (
    FabricationProcessStep,
    FabricationProcessStepBase,
)
from fabrication_facilities.schema_packages.utils import (
    Massflow_controller,
    DRIE_Massflow_controller,
    parse_chemical_formula,
    FabricationChemical,
    TimeRampTemperature,
    TimeRampMassflow,
    TimeRampPressure,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Etching workflow schema')


class EtchingOutputs(ArchiveSection):

    m_def=Section(
        a_eln={
            'properties':{
                'order':[
                    'job_number',
                    'duration_measured',
                ],
            }
        },
        description= 'Set of parameters obtained in an etching process',
    )

    job_number = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )

    duration_measured = Quantity(
        type=np.float64,
        description='Real time of the process ad output',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )

    control_parameter_profile=SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )


class RIEbase(FabricationProcessStepBase, ArchiveSection):
    m_def = Section(
        description = 'Atomistic component of a RIE step',
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
                'step_type',
                'definition_of_process_step',
                'keywords',
                'recipe_name',
                'recipe_file',
                'recipe_preview',
                'name',
                'description',
                'affiliation',
                'room',
                'location',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'tag',
                    'id_item_processed',
                    'operator',
                    'starting_date',
                    'ending_date',
                    'short_names',
                    'target_materials_formulas',
                    'wall_temperature',
                    'chuck_temperature',
                    'chuck_power',
                    'chuck_frequency',
                    'chamber_pressure',
                    'bias',
                    'clamping',
                    'clamping_type',
                    'clamping_pressure',
                    'number of loops'
                    'notes',
                ]
            },
        },
    )
    short_names = Quantity(
        type=str,
        description='Name of reactive species',
        shape=['*'],
        a_eln={'component': 'StringEditQuantity', 'label': 'target materials names'},
    )
    target_materials_formulas = Quantity(
        type=str,
        description='Inserted only if known',
        shape=['*'],
        a_eln={'component': 'StringEditQuantity'},
    )
    chamber_pressure = Quantity(
        type=np.float64,
        description='Pressure in the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )
    wall_temperature = Quantity(
        type=np.float64,
        description='Temperature of the wall of the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    chuck_temperature = Quantity(
        type=np.float64,
        description='Temperature imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    chuck_power = Quantity(
        type=np.float64,
        description='Power imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'W'},
        unit='W',
    )
    chuck_frequency = Quantity(
        type=np.float64,
        description='Frequency impulse imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'MHz'},
        unit='MHz',
    )
    bias = Quantity(
        type=np.float64,
        description='Voltage imposed on the sample by electodes',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )
    clamping = Quantity(
        type=bool,
        description='Is clamping used in the process?',
        a_eln={'component': 'BoolEditQuantity'},
    )
    clamping_type = Quantity(
        type=MEnum(
            [
                'None',
                'Mechanical',
                'Electrostatic',
            ]
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )

    clamping_pressure = Quantity(
        type=np.float64,
        description='Pressure generated by a cooling helium flow on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    number_of_loops=Quantity(
        type=int,
        description='Times for which this step is repeated with equal parameters',
        a_eln={'component':'NumberEditQuantity'},
    )

    fluximeters = SubSection(
        section_def=Massflow_controller,
        repeats=True,
    )

    temperature_ramps=SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    pressure_ramps=SubSection(
        section_def=TimeRampPressure,
        repeats=True,
    )

    gaseous_massflow_ramps=SubSection(
        section_def=TimeRampMassflow,
        repeats=True,
    )

    materials_etched = SubSection(
        section_def=FabricationChemical,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.target_materials_formulas is None:
            pass
        else:
            chems = []
            for formula in self.target_materials_formulas:
                chemical = FabricationChemical()
                chemical.chemical_formula = formula
                chemical.normalize(archive, logger)
                chems.append(chemical)
            self.materials_etched = chems


class RIE (FabricationProcessStep, ArchiveSection):

    m_def=Section(
        description="""
        Form of plasma etching  in which the wafer is placed on a radio-frequency-driven
        electrode and the counter electrode has a larger area than the driven electrode.
        Uses both physical and chemical mechanisms to achieve high levels of resolutions.
        In the RIE process, cations are produced from reactive gases which are
        accelerated with high energy to the substrate and chemically react with the item
        surface. Factors such as applied coil or electrode power, reactant gas flow
        rates, duty cycles and chamber presures were considered as main process
        parameters. The plasma beam is generated under low pressure by an electromagnetic
         field. High energy ions, predominantly bombarding the surface, normally create
        a local abundance of radicals that react with the surface.
        """,
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
                'tag',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'depth_target',
                    'duration_target',
                    'etching_rate_target',
                    'notes',
                ]
            }
        }
    )

    depth_target = Quantity(
        type=np.float64,
        description='Amount of material to be etched',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )

    duration_target = Quantity(
        type=np.float64,
        description='Time prescribed by the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )

    etching_rate_target = Quantity(
        type=np.float64,
        description='etching rate desired',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm/minute',
        },
        unit='nm/minute',
    )

    etching_steps=SubSection(
        section_def=RIEbase,
        repeats=True,
    )

    outputs=SubSection(
        section_def=EtchingOutputs,
        repeats=True,
    )


class ICP_RIEbase(RIEbase, ArchiveSection):
    m_def = Section(
        description = 'Atomistic component of an ICP RIE step',
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
                'step_type',
                'definition_of_process_step',
                'keywords',
                'recipe_name',
                'recipe_file',
                'recipe_preview',
                'name',
                'description',
                'affiliation',
                'room',
                'location',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'tag',
                    'id_item_processed',
                    'operator',
                    'starting_date',
                    'ending_date',
                    'short_names',
                    'target_materials_formulas',
                    'wall_temperature',
                    'chamber_pressure',
                    'chuck_temperature',
                    'chuck_power',
                    'chuck_frequency',
                    'icp_power',
                    'icp_frequency',
                    'bias',
                    'clamping',
                    'clamping_type',
                    'clamping_pressure',
                    'number_of_loops',
                    'notes',
                ]
            },
        },
    )

    icp_power = Quantity(
        type=np.float64,
        description='Power erogated in the region of the plasma',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )
    icp_frequency = Quantity(
        type=np.float64,
        description='Frequency of current on the gases area',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )


class ICP_RIE(RIE, ArchiveSection):

    m_def=Section(
        description="""
        Dry etching method by which energy is magnetically coupled into the
        plasma by a current carrying loop around the chamber,
        using etching based on ions reacting with substrate surface and hitting it
        """,
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
                'tag',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'depth_target',
                    'duration_target',
                    'etching_rate_target',
                    'notes',
                ]
            }
        }
    )

    etching_steps=SubSection(
        section_def=ICP_RIEbase,
        repeats=True,
    )


class DRIE_BOSCHbase(ICP_RIEbase, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
                'step_type',
                'definition_of_process_step',
                'keywords',
                'recipe_name',
                'recipe_file',
                'recipe_preview',
                'name',
                'description',
                'affiliation',
                'room',
                'location',
                'chuck_power',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'tag',
                    'id_item_processed',
                    'operator',
                    'starting_date',
                    'ending_date',
                    'short_names',
                    'target_materials_formulas',
                    'depth_target',
                    'duration_target',
                    'etching_rate_target',
                    'wall_temperature',
                    'chamber_pressure',
                    'chuck_temperature',
                    'high_chuck_power',
                    'high_chuck_power_duration',
                    'low_chuck_power',
                    'low_chuck_power_duration',
                    'chuck_frequency',
                    'icp_power',
                    'icp_frequency',
                    'bias',
                    'clamping',
                    'clamping_type',
                    'clamping_pressure',
                    'number_of_loops',
                    'notes',
                ]
            },
        },
    )

    high_chuck_power = Quantity(
        type=np.float64,
        description='Power erogated on the chuck in the high phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    low_chuck_power = Quantity(
        type=np.float64,
        description='Power erogated on the chuck in the low phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    high_chuck_power_duration = Quantity(
        type=np.float64,
        description='Power erogated on the chuck in the high phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )

    low_chuck_power_duration = Quantity(
        type=np.float64,
        description='Duration of the low phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )

    fluximeters=SubSection(
        section_def=DRIE_Massflow_controller,
        repeats=True,
    )


class DRIE_BOSCH(ICP_RIE, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
                'tag',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                ]
            }
        }
    )

    etching_steps = SubSection(
        section_def=DRIE_BOSCHbase,
        repeats=True,
    )

    temperature_ramps=SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    pressure_ramps=SubSection(
        section_def=TimeRampPressure,
        repeats=True,
    )

    gaseous_massflow_ramps=SubSection(
        section_def=TimeRampMassflow,
        repeats=True,
    )

    outputs=SubSection(
        section_def=EtchingOutputs,
        repeats=True,
    )


class WetEtching(FabricationProcessStep, ArchiveSection):
    m_def = Section(
        description="""
        Wet etching is a material removal process that uses liquid chemicals or etchants
        to remove materials from a wafer. The specific patters are defined by masks on
        the wafer. Materials that are not protected by the masks are etched away by
        liquid chemicals. A wet etching process involves multiple chemical reactions that
        consume the original reactants and produce new reactants. The wet etch process
        can be described by three basic steps. (1) Diffusion of the liquid etchant to the
        structure that is to be removed. (2) The reaction between the liquid etchant and
        the material being etched away. A reduction-oxidation (redox) reaction usually
        occurs. This reaction entails the oxidation of the material then dissolving the
        oxidized material. (3) Diffusion of the byproducts in the reaction from the
        reacted surface.
        """,
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'tag',
                    'depth_target',
                    'duration_target',
                    'erching_rate_target',
                    'short_names',
                    'target_materials_formulas',
                    'etching_solution',
                    'etching_solution_proportions',
                    'etching_reactives',
                    'etching_reactives_formulas',
                    'enanching_temperature',
                    'hood_pressure',
                    'hood_atmospheric_gas',
                    'wetting',
                    'wetting_duration',
                    'ultrasounds_required',
                    'ultrasounds_frequency',
                    'ultrasounds_duration',
                    'rinsing_solution',
                    'rinsing_solution_proportions',
                    'rinsing_duration',
                    'rinsing_de_ionic_H2O',
                    'rinsing_de_ionic_H2O_duration',
                    'notes',
                ]
            },
        },
    )
    short_names = Quantity(
        type=str,
        description='Materials to be etched',
        shape=['*'],
        a_eln={'component': 'StringEditQuantity', 'label': 'target materials'},
    )
    target_materials_formulas = Quantity(
        type=str,
        description='Formulas of materials etched',
        shape=['*'],
        a_eln={'component': 'StringEditQuantity'},
    )
    depth_target = Quantity(
        type=np.float64,
        description='Amount of material to be etched',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    etching_solution = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    etching_solution_proportions = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    etching_reactives = Quantity(
        type=str,
        description='Names of compounds used to etch',
        shape=['*'],
        a_eln={'component': 'StringEditQuantity'},
    )
    etching_reactives_formulas = Quantity(
        type=str,
        description='Formulas of compounds used to etch',
        shape=['*'],
        a_eln={'component': 'StringEditQuantity'},
    )
    duration_target = Quantity(
        type=np.float64,
        description='Time prescribed by the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    etching_rate_target = Quantity(
        type=np.float64,
        description='Etching rate prescribed by the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm/minute'},
        unit='nm/minute',
    )
    enanching_temperature = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    hood_pressure = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar'
        },
        unit= 'mbar'
    )

    hood_atmospheric_gas = Quantity(
        type=str,
        a_eln={
            'component':'StringEditQuantity'
        }
    )

    wetting=Quantity(
        type= bool,
        a_eln={
            'component':'BoolEditQuantity',
        }
    )

    wetting_duration = Quantity(
        type= np.float64,
        a_eln={
            'component':'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )

    ultrasounds_required=Quantity(
        type= bool ,
        a_eln={
            'component':'BoolEditQuantity',
        }
    )

    ultrasounds_frequency=Quantity(
        type= np.float64,
        a_eln={
            'component':'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )

    ultrasounds_duration=Quantity(
        type= np.float64,
        a_eln={
            'component':'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )

    rinsing_solution = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    rinsing_solution_proportions = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    rinsing_duration = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )

    rinsing_de_ionic_H2O = Quantity(
        type=bool,
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )
    rinsing_de_ionic_H2O_duration = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )

    materials_etched = SubSection(
        section_def=FabricationChemical,
        repeats=True,
    )

    reactives_used_to_etch = SubSection(
        section_def=FabricationChemical,
        repeats=True,
    )

    outputs=SubSection(
        section_def=EtchingOutputs,
        repeats=False,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.target_materials_formulas is None:
            pass
        else:
            chems = []
            for v1, v2 in zip(self.short_names, self.target_materials_formulas):
                chemical = FabricationChemical()
                val1 = v1 #if v1 != '-' else None
                val2 = v2 if v2 != '-' else None
                chemical.name=val1
                chemical.chemical_formula=val2
                chemical.normalize(archive, logger)
                chems.append(chemical)
            self.materials_etched = chems

        if self.etching_reactives_formulas is None:
            pass
        else:
            reactives = []
            for v1, v2 in zip(self.etching_reactives, self.etching_reactives_formulas):
                chemical = FabricationChemical()
                val1 = v1 #if v1 != '-' else val1=v2
                val2 = v2 if v2 != '-' else None
                chemical.name=val1
                chemical.chemical_formula=val2
                chemical.normalize(archive, logger)
                reactives.append(chemical)
            self.reactives_used_to_etch = reactives


class WetCleaning(WetEtching):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'tag',
                    'depth_target',
                    'duration_target',
                    'erching_rate_target',
                    'short_names',
                    'target_materials_formulas',
                    'etching_solution',
                    'etching_solution_proportions',
                    'etching_reactives',
                    'etching_reactives_formulas',
                    'enanching_temperature',
                    'hood_pressure',
                    'hood_atmospheric_gas',
                    'wetting',
                    'wetting_duration',
                    'ultrasounds_required',
                    'ultrasounds_frequency',
                    'ultrasounds_duration',
                    'rinsing_solution',
                    'rinsing_solution_proportions',
                    'rinsing_duration',
                    'rinsing_de_ionic_H2O',
                    'rinsing_de_ionic_H2O_duration',
                    'notes',
                ]
            },
        },
    )
    etching_solution = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity', 'label': 'cleaning solution'},
    )
    etching_solution_proportions = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'cleaning solution proportions',
        },
    )
    etching_duration = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
            'label': 'cleaning duration',
        },
        unit='minute',
    )


class Stripping(Chemical, FabricationProcessStep, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'stripping_type',
                    'short_name',
                    'chemical_formula',
                    'duration_target',
                    'removing_temperature',
                    'ultrasound_required',
                    'notes',
                ]
            },
        },
    )
    stripping_type = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    short_name = Quantity(
        type=str,
        description='Material to remove',
        a_eln={'component': 'StringEditQuantity', 'label': 'Target material'},
    )
    chemical_formula = Quantity(
        type=str,
        description='Inserted only if known',
        a_eln={'component': 'StringEditQuantity'},
    )
    removing_temperature = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    duration_target = Quantity(
        type=np.float64,
        description='Time prescribed by the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    ultrasound_required = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )

    material_elemental_composition = SubSection(
        section_def=ElementalComposition, repeats=True
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.chemical_formula:
            elements, counts = parse_chemical_formula(self.chemical_formula)
            total = 0
            for token in counts:
                total += int(token)
            if total != 0:
                elemental_fraction = np.array(counts) / total
                elementality = []
                i = 0
                for entry in elements:
                    elemental_try = ElementalComposition()
                    elemental_try.element = entry
                    elemental_try.atomic_fraction = elemental_fraction[i]
                    i += 1
                    elementality.append(elemental_try)
            else:
                print('No elements provided')
            self.material_elemental_composition = elementality


m_package.__init_metainfo__()
