######################################### CVD #########################################
#######################################################################################
#    Fabrication process step sub category consisting in the deposition of a solid    #
# material onto a substrate by chemical reaction of a gaseous precursor or mixture of #
#                       precursors, commonly initiated by heat                        #
#######################################################################################

from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.metainfo import (
    MEnum,
    Package,
    Quantity,
    Section,
    SubSection,
)
from schema_packages.fabrication_utilities import (
    FabricationProcessStep,
    FabricationProcessStepBase,
)
from schema_packages.steps.utils import (
    Carrier,
    Chuck,
    ICP_Column,
    Massflow_controller,
    SynthesisOutputs,
)
from schema_packages.utils import (
    FabricationChemical,
    TimeRampPressure,
    TimeRampTemperature,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Schemas for cvds steps in fabrication')


class LPCVDbase(FabricationProcessStepBase):
    m_def = Section(
        description='Atomistic component of a general LPCVD step',
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'tag',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'chamber_temperature',
                    'chamber_pressure',
                    'number_of_loops',
                    'notes',
                ],
            },
        },
    )

    chamber_pressure = Quantity(
        type=np.float64,
        description='Pressure in the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )

    chamber_temperature = Quantity(
        type=np.float64,
        description='Temperature of the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    number_of_loops = Quantity(
        type=int,
        description='Times for which this step is repeated with equal parameters',
        a_eln={'component': 'NumberEditQuantity'},
    )

    material_deposited = SubSection(
        section_def=FabricationChemical,
        description='In this sections you can describe one or more materials deposited',
        repeats=True,
    )

    pressure_ramps = SubSection(
        section_def=TimeRampPressure,
        repeats=True,
    )

    temperature_ramps = SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    fluximeters = SubSection(
        section_def=Massflow_controller,
        description='Through this section you can describe the gases involved.',
        repeats=True,
    )

    item_carrier = SubSection(
        section_def=Carrier,
        description="""
        Tipically wafers are loaded by a multiple wafer device which enters into the
        furnace
        """,
        repeats=False,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class PECVDbase(FabricationProcessStepBase):
    m_def = Section(
        description='Atomistic component of a PECVD step',
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'tag',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'chamber_temperature',
                    'chamber_pressure',
                    'number_of_loops',
                    'notes',
                ]
            },
        },
    )

    chamber_pressure = Quantity(
        type=np.float64,
        description='Pressure in the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )

    chamber_temperature = Quantity(
        type=np.float64,
        description='Temperature of the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    number_of_loops = Quantity(
        type=int,
        description='Times for which this step is repeated with equal parameters',
        a_eln={'component': 'NumberEditQuantity'},
    )

    material_deposited = SubSection(
        section_def=FabricationChemical,
        description='In this sections you can describe one or more materials deposited',
        repeats=True,
    )

    pressure_ramps = SubSection(
        section_def=TimeRampPressure,
        repeats=True,
    )

    temperature_ramps = SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    fluximeters = SubSection(
        section_def=Massflow_controller,
        description='Through this section you can describe the gases involved.',
        repeats=True,
    )

    chuck = SubSection(
        section_def=Chuck,
        description="""
        Tipically PECVD is performed on wafer positioned onto a chuck. Here ou can
        describe its parameters and other features
        """,
        repeats=False,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class ICP_CVDbase(PECVDbase):
    m_def = Section(
        description='Atomistic component of an ICP CVD step',
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'tag',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'chamber_temperature',
                    'chamber_pressure',
                    'number_of_loops',
                    'notes',
                ]
            },
        },
    )

    icp_column = SubSection(
        section_def=ICP_Column,
        description='Section containing the parameters for the ICP column',
        repeats=False,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class LPCVD(FabricationProcessStep):
    m_def = Section(
        description="""
        Deposition of a solid material onto a substrate by chemical reaction of
        a gaseous precursor or mixture of precursors, commonly initiated by heat.
        """,
        a_eln={
            'hide': ['tag', 'duration'],
            'properties': {
                'order': [
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'institution',
                    'facility',
                    'laboratory',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'step_id',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'thickness_target',
                    'duration_target',
                    'deposition_rate_target',
                    'notes',
                ]
            },
        },
    )

    thickness_target = Quantity(
        type=np.float64,
        description='Amount of material to be deposited',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )

    duration_target = Quantity(
        type=np.float64,
        description='Duration required of the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )

    deposition_rate_target = Quantity(
        type=np.float64,
        description='Deposition rate desired',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm/minute',
        },
        unit='nm/minute',
    )

    synthesis_steps = SubSection(
        section_def=LPCVDbase,
        repeats=True,
    )

    outputs = SubSection(
        section_def=SynthesisOutputs,
        repeats=False,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class PECVD(LPCVD):
    m_def = Section(
        description="""
        Deposition of a solid material onto a substrate by chemical reaction of a
        gaseous precursor or mixture of precursors, commonly initiated by heat to create
        a plasma. PECVD uses temperature tipically lower of LPCVD but relyies on an
        electrode system on the sample.
        """,
        a_eln={
            'hide': ['tag', 'duration'],
            'properties': {
                'order': [
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'institution',
                    'facility',
                    'laboratory',
                    'id_item_processed',
                    'wafer_side',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'step_id',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'thickness_target',
                    'duration_target',
                    'deposition_rate_target',
                    'notes',
                ]
            },
        },
    )

    wafer_side = Quantity(
        type=MEnum(
            'front',
            'back',
        ),
        description='Side exposed in the process',
        a_eln={'component': 'EnumEditQuantity'},
    )

    synthesis_steps = SubSection(
        section_def=PECVDbase,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class ICP_CVD(PECVD):
    m_def = Section(
        description="""
        Deposition of a solid material onto a substrate by chemical reaction of a
        gaseous precursor or mixture of precursors, commonly initiated by heat to create
        a plasma. To generate the plasma the ICP CVD procedure uses a current in
        addition to the lower electrodes to enanche by magnetic field the generation.
        """,
        a_eln={
            'hide': ['tag', 'duration'],
            'properties': {
                'order': [
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'institution',
                    'facility',
                    'laboratory',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'step_id',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'thickness_target',
                    'duration_target',
                    'deposition_rate_target',
                    'notes',
                ]
            },
        },
    )

    synthesis_steps = SubSection(
        section_def=ICP_CVDbase,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


m_package.__init_metainfo__()
