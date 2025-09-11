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
    DevelopingSolution,
    SpinningComponent,
    SpinRinsingbase,
)
from schema_packages.utils import FabricationChemical

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger


m_package = Package(name='Resist development steps schemas definitions')


class ResistDevelopmentbase(FabricationProcessStepBase):
    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'tag',
                    'id_item_processed',
                    'adhesion_type',
                    'operator',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'developing_mode',
                    'developing_duration',
                    'developing_temperature',
                    'number of loops',
                    'notes',
                ]
            }
        }
    )

    adhesion_type = Quantity(
        type=MEnum(
            'None',
            'Direct',
            'Suspended',
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )

    developing_mode = Quantity(
        type=MEnum(
            'auto',
            'manual',
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    developing_duration = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )
    developing_temperature = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    number_of_loops = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )

    materials_developed = SubSection(section_def=FabricationChemical, repeats=True)

    developing_solution = SubSection(section_def=DevelopingSolution, repeats=False)

    final_rinsing = SubSection(section_def=SpinRinsingbase, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class SpinResistDevelopmentbase(ResistDevelopmentbase):
    m_def = Section()

    spin_parameters = SubSection(section_def=SpinningComponent, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class ResistDevelopment(FabricationProcessStep):
    m_def = Section(
        a_eln={
            'hide': [
                'tag',
                'duration',
                'operator',
            ],
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
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'notes',
                ]
            },
        }
    )

    development_steps = SubSection(
        section_def=ResistDevelopmentbase,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class SpinResistDevelopment(ResistDevelopment):
    m_def = Section(
        a_eln={
            'hide': ['tag', 'duration', 'operator'],
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
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'notes',
                ]
            },
        }
    )

    development_steps = SubSection(
        section_def=SpinResistDevelopmentbase,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
