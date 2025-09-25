from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.metainfo import (
    Package,
    Quantity,
    Section,
    SubSection,
)
from schema_packages.fabrication_utilities import (
    FabricationProcessStep,
    FabricationProcessStepBase,
)
from schema_packages.steps.utils import Carrier, Massflow_controller, OxidationOutputs
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

m_package = Package(name='Schemas to describe thermal oxidation steps')


class ThermalOxidationbase(FabricationProcessStepBase):
    m_def = Section(
        description='Atomistic component of a dry or wet oxidation process step.',
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'tag',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'oxidation_type',
                    'temperature_final_target',
                    'notes',
                ]
            },
        },
    )

    oxidation_type = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})

    temperature_final_target = Quantity(
        type=np.float64,
        description='Operative value of the furnace as set on the equipment',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    number_of_loops = Quantity(
        type=int,
        description='Times for which this step is repeated with equal parameters',
        a_eln={'component': 'NumberEditQuantity'},
    )

    target_material = SubSection(section_def=FabricationChemical, repeats=False)

    fluximeters = SubSection(section_def=Massflow_controller, repeats=True)

    temperature_ramps = SubSection(section_def=TimeRampTemperature, repeats=True)

    pressure_ramps = SubSection(section_def=TimeRampPressure, repeats=True)

    item_carrier = SubSection(section_def=Carrier, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class ThermalOxidation(FabricationProcessStep):
    m_def = Section(
        description="""
        Thermal process step  where the wafer or other silicon item are inserted into an
        hermetically sealed furnace chamber where a mixture of gases are injected once
        the internal chamber temperature has reached the target. The O2 reacts with 
        surface Si generating SiO2. It can be dry if only O2 is transferred in the
        chamber or wet if also H2 is present.
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
                    'oxidation_rate_target',
                    'notes',
                ]
            },
        },
    )
    thickness_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )

    duration_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )

    oxidation_rate_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm/minute'},
        unit='nm/minute',
    )

    oxidation_steps = SubSection(section_def=ThermalOxidationbase, repeats=True)

    outputs = SubSection(section_def=OxidationOutputs, repeats=False)


m_package.__init_metainfo__()
