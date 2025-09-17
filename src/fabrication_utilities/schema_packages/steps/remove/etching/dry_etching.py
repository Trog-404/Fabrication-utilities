#######################################################################################
##################################### DRY ETCHING #####################################
#######################################################################################

from typing import TYPE_CHECKING

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
    Chuck,
    DRIE_Chuck,
    DRIE_Massflow_controller,
    EtchingOutputs,
    ICP_Column,
    Massflow_controller,
)
from schema_packages.utils import (
    FabricationChemical,
    TimeRampPressure,
    TimeRampTemperature,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger


m_package = Package(name='Dry etching steps schemas definitions for fabrications')


class RIEbase(FabricationProcessStepBase):
    m_def = Section(
        description='Atomistic component of a RIE step',
        a_eln={
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'tag',
                    'id_item_processed',
                    'operator',
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
        description='Temperature of the wall of the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    number_of_loops = Quantity(
        type=int,
        description='Times for which this step is repeated with equal parameters',
        a_eln={'component': 'NumberEditQuantity'},
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
        repeats=True,
    )

    chuck = SubSection(
        section_def=Chuck,
        repeats=False,
    )

    materials_etched = SubSection(
        section_def=FabricationChemical,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class ICP_RIEbase(RIEbase):
    m_def = Section(
        description='Atomistic component of an ICP RIE step',
        a_eln={
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'tag',
                    'id_item_processed',
                    'operator',
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
        repeats=False,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class DRIE_BOSCHbase(ICP_RIEbase):
    m_def = Section(
        a_eln={
            'hide': [
                'chuck_power',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'tag',
                    'id_item_processed',
                    'operator',
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

    fluximeters = SubSection(
        section_def=DRIE_Massflow_controller,
        repeats=True,
    )

    chuck = SubSection(
        section_def=DRIE_Chuck,
        repeats=False,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class RIE(FabricationProcessStep):
    m_def = Section(
        description="""
        Form of plasma etching  in which the wafer is placed on a radio-frequency-driven
        electrode and the counter electrode has a larger area than the driven
        electrode. Uses both physical and chemical mechanisms to achieve high levels
        of resolutions. In the RIE process, cations are produced from reactive gases
        which are accelerated with high energy to the substrate and chemically react
        with the item surface. Factors such as applied coil or electrode power, reactant
        gas flow rates, duty cycles and chamber presures were considered as main process
        parameters. The plasma beam is generated under low pressure by an
        electromagnetic field. High energy ions, predominantly bombarding the surface,
        normally create a local abundance of radicals that react with the surface.
        """,
        a_eln={
            'hide': ['duration', 'tag', 'operator'],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'step_id',
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
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'depth_target',
                    'duration_target',
                    'etching_rate_target',
                    'endpoint',
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

    endpoint = Quantity(
        type=bool,
        description="""
        The process uses a time or is performed with an endpoint for some parameters
        """,
        a_eln={'component': 'BoolEditQuantity'},
    )

    etching_steps = SubSection(
        section_def=RIEbase,
        repeats=True,
    )

    outputs = SubSection(
        section_def=EtchingOutputs,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class ICP_RIE(RIE):
    m_def = Section(
        description="""
        Dry etching method by which energy is magnetically coupled into the
        plasma by a current carrying loop around the chamber,
        using etching based on ions reacting with substrate surface and hitting it
        """,
        a_eln={
            'hide': ['duration', 'tag', 'operator'],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'step_id',
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
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'depth_target',
                    'duration_target',
                    'etching_rate_target',
                    'endpoint',
                    'notes',
                ]
            },
        },
    )

    etching_steps = SubSection(
        section_def=ICP_RIEbase,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class DRIE_BOSCH(ICP_RIE):
    m_def = Section(
        a_eln={
            'hide': ['duration', 'tag', 'operator'],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'step_id',
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
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'endpoint',
                    'notes',
                ]
            },
        }
    )

    etching_steps = SubSection(
        section_def=DRIE_BOSCHbase,
        repeats=True,
    )

    outputs = SubSection(
        section_def=EtchingOutputs,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
