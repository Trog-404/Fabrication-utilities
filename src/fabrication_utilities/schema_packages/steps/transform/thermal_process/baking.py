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
from schema_packages.steps.utils import BaseOutputs
from schema_packages.utils import TimeRampTemperature

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Schemas to describe baking steps in fabrication')


class Bakingbase(FabricationProcessStepBase):
    m_def = Section(
        description='Atomistic component of a baking step',
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'tag',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'baking_temperature',
                    'baking_pressure',
                    'notes',
                ]
            },
        },
    )

    baking_temperature = Quantity(
        type=np.float64,
        description="""
        Temperature imposed on the oven or thermal plate to perform the baking step
        """,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    baking_pressure = Quantity(
        type=np.float64,
        description='Pressure of the system used. If not specified is the atmospheric',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    temperature_ramps = SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class Baking(FabricationProcessStep):
    m_def = Section(
        description="""
        Thermal processing aimed at transforming one or more material layers present on
        the top of the wafer. Examples are: resist backing, to strengthen it before
        etching or ion implantation.
        """,
        a_eln={
            'hide': [
                'tag',
                'duration',
            ],
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
                    'notes',
                ],
            },
        },
    )

    baking_steps = SubSection(
        section_def=Bakingbase,
        repeats=True,
    )

    outputs = SubSection(section_def=BaseOutputs, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


m_package.__init_metainfo__()
