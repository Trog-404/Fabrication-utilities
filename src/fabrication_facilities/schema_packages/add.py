from typing import (
    TYPE_CHECKING,
)

import numpy as np
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
)
from fabrication_facilities.schema_packages.utils import (
    Massflow_controller,
    parse_chemical_formula,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Add processes schema')


class ICP_CVD(Chemical, FabricationProcessStep, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

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
                    'recipe_name',
                    'recipe_file',
                    'short_name',
                    'chemical_formula',
                    'thickness_target',
                    'deposition_rate_target',
                    'chamber_pressure',
                    'chuck_temperature',
                    'power',
                    'bias',
                    'thickness_measured',
                    'duration_measured',
                    'deposition_rate_obtained',
                    'notes',
                ]
            },
        },
    )
    deposition_rate_target = Quantity(
        type=np.float64,
        description='Deposition rate desired',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm/minute'},
        unit='nm/minute',
    )
    short_name = Quantity(
        type=str,
        description='Material to be deposited',
        a_eln={'component': 'StringEditQuantity', 'label': 'target material'},
    )
    chemical_formula = Quantity(
        type=str,
        description='Inserted only if known',
        a_eln={'component': 'StringEditQuantity'},
    )
    thickness_target = Quantity(
        type=np.float64,
        description='Amount of material to be deposited',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    chamber_pressure = Quantity(
        type=np.float64,
        description='Pressure in the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )
    chuck_temperature = Quantity(
        type=np.float64,
        description='Temperature of the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    power = Quantity(
        type=np.float64,
        description='Power erogated',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'watt'},
        unit='watt',
    )
    bias = Quantity(
        type=np.float64,
        description='Bias voltage in the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'volt'},
        unit='volt',
    )
    thickness_measured = Quantity(
        type=np.float64,
        description='Amount of material deposited efefctively in the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    duration_measured = Quantity(
        type=np.float64,
        description='Real time employed',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    deposition_rate_obtained = Quantity(
        type=np.float64,
        description='Deposition rate as output',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm/minute'},
        unit='nm/minute',
    )
    fluximeters = SubSection(
        section_def=Massflow_controller,
        repeats=True,
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


class Spin_Coating(Chemical, FabricationProcessStep, ArchiveSection):
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
                    'recipe_name',
                    'thickness_from_recipe',
                    'duration_from_recipe',
                    'short_name',
                    'chemical_formula',
                    'thickness_target',
                    'hdms_required',
                    'exposure_required',
                    'exposure_duration',
                    'peb_required',
                    'peb_duration',
                    'peb_temperature',
                    'dewetting_duration',
                    'dewetting_temperature',
                    'spin_dispensed_volume',
                    'spin_frequency',
                    'spin_angular_acceleration',
                    'spin_duration',
                    'baking_required',
                    'baking_duration',
                    'baking_temperature',
                    'thickness_measured',
                    'notes',
                ]
            },
        },
    )
    thickness_from_recipe = Quantity(
        type=np.float64,
        description='Amount of material deposited as described in the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    duration_from_recipe = Quantity(
        type=np.float64,
        description='Time prescribed by the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    short_name = Quantity(
        type=str,
        description='Material to be deposited',
        a_eln={'component': 'StringEditQuantity', 'label': 'resist name'},
    )
    chemical_formula = Quantity(
        type=str,
        description='Inserted only if known',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    thickness_target = Quantity(
        type=np.float64,
        description='Amount of material to be deposited',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    hdms_required = Quantity(
        type=bool,
        description='The recipe use the hdms?',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )
    exposure_required = Quantity(
        type=bool,
        description='The recipe use exposure?',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )
    exposure_duration = Quantity(
        type=np.float64,
        description='The duration of the exposure',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )
    peb_required = Quantity(
        type=bool,
        description='The recipe needs PEB?',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )
    peb_duration = Quantity(
        type=np.float64,
        description='The duration of the peb',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )
    peb_temperature = Quantity(
        type=np.float64,
        description='The temperature of the peb',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    dewetting_duration = Quantity(
        type=np.float64,
        description='The duration of the dewetting',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )
    dewetting_temperature = Quantity(
        type=np.float64,
        description='The temperaure of the dewetting',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    spin_dispensed_volume = Quantity(
        type=np.float64,
        description='Solution dispensed',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'milliliter',
        },
        unit='milliliter',
    )
    spin_frequency = Quantity(
        type=np.float64,
        description='Velocity of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'revolutions_per_minute',
        },
        unit='revolutions_per_minute',
    )
    spin_angular_acceleration = Quantity(
        type=np.float64,
        description='Acceleration of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'revolutions_per_minute/sec',
        },
        unit='revolutions_per_minute/sec',
    )
    spin_duration = Quantity(
        type=np.float64,
        description='Acceleration of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )
    baking_required = Quantity(
        type=bool,
        description='The recipe use exposure?',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )
    baking_duration = Quantity(
        type=np.float64,
        description='The duration of the dewetting',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )
    baking_temperature = Quantity(
        type=np.float64,
        description='The temperaure of the dewetting',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    thickness_measured = Quantity(
        type=np.float64,
        description='Amount of material deposited as described in the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )

    resist_elemental_composition = SubSection(
        section_def=ElementalComposition, repeats=True
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.exposure_required:
            self.exposure_duration = Quantity(
                type=np.float64,
                description='The duration of the exposure',
                a_eln={
                    'component': 'NumberEditQuantity',
                    'defaultDisplayUnit': 'minute',
                },
                unit='minute',
            )
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
            self.resist_elemental_composition = elementality


class Bonding(FabricationProcessStep, ArchiveSection):
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
                    'recipe_name',
                    'wafer_bonding_type',
                    'alignment_required',
                    'alignment_max_error',
                    'wafer_stack_1_name',
                    'wafer_stack_2_name',
                    'wafer_space_required',
                    'alignment_target_mask_name',
                    'alignment_viewfinder_mask_name',
                    'wafer_bonded_name',
                    'notes',
                ]
            },
        },
    )

    wafer_bonding_type = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    alignment_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    alignment_max_error = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    wafer_stack_1_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    wafer_stack_2_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    wafer_space_required = Quantity(
        type=bool,
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )
    alignment_target_mask_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    alignment_viewfinder_mask_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    wafer_bonded_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )


class ElectronGun(FabricationProcessStep, ArchiveSection):
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
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'short_name',
                    'wafer_stack_name',
                    'deposition_thickness_target',
                    'deposition_duration',
                    'deposition_chamber_pressure',
                    'deposition_thickness_measured',
                    'gun_voltage_measured',
                    'gun_current_measured',
                    'notes',
                ]
            },
        },
    )
    short_name = Quantity(
        type=str,
        description='Deposited Material',
        a_eln={'component': 'StringEditQuantity', 'label': 'Target material'},
    )
    wafer_stack_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    deposition_thickness_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    deposition_duration = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    deposition_chamber_pressure = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )
    deposition_thickness_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    gun_voltage_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )
    gun_current_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mampere'},
        unit='mampere',
    )


class Sputtering(Chemical, FabricationProcessStep, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

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
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'short_name',
                    'chemical_formula',
                    'thickness_target',
                    'duration_target',
                    'chuck_temperature',
                    'power',
                    'delay_between_stack_layers',
                    'thickness_measured',
                    'duration_measured',
                    'deposition_rate_obtained',
                    'notes',
                ]
            },
        },
    )
    short_name = Quantity(
        type=str,
        description='Material to be deposited',
        a_eln={'component': 'StringEditQuantity', 'label': 'target material'},
    )
    thickness_target = Quantity(
        type=np.float64,
        description='Amount of material to be deposited',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    duration_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    chuck_temperature = Quantity(
        type=np.float64,
        description='Temperature of the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    power = Quantity(
        type=np.float64,
        description='Power erogated',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'watt'},
        unit='watt',
    )
    delay_between_stack_layers = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    thickness_measured = Quantity(
        type=np.float64,
        description='Amount of material deposited effectively in the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um'},
        unit='um',
    )
    duration_measured = Quantity(
        type=np.float64,
        description='Real time employed',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    deposition_rate_obtained = Quantity(
        type=np.float64,
        description='Deposition rate as output',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm/minute'},
        unit='nm/minute',
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


class SOG(Chemical, FabricationProcessStep, ArchiveSection):
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
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'short_name',
                    'chemical_formula',
                    'pre_cleaning',
                    'thickness_target',
                    'dewetting_duration',
                    'dewetting_temperature',
                    'thickness_measured',
                    'notes',
                ]
            },
        },
    )

    short_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity', 'label': 'Substrate Material'},
    )
    pre_cleaning = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    thickness_target = Quantity(
        type=np.float64,
        description='Amount of material to be deposited',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um'},
        unit='um',
    )
    dewetting_duration = Quantity(
        type=np.float64,
        description='The duration of the dewetting',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )
    dewetting_temperature = Quantity(
        type=np.float64,
        description='The temperaure of the dewetting',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    thickness_measured = Quantity(
        type=np.float64,
        description='Amount of material deposited as described in the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um'},
        unit='um',
    )

    substrate_elemental_composition = SubSection(
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
            self.substrate_elemental_composition = elementality


m_package.__init_metainfo__()
