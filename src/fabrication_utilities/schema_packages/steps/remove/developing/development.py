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
    BaseOutputs,
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
        description='Atomistic component of a developing step',
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'tag',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'adhesion_type',
                    'developing_mode',
                    'duration',
                    'developing_temperature',
                    'number of loops',
                    'notes',
                ]
            }
        },
    )

    adhesion_type = Quantity(
        type=MEnum(
            'None',
            'Direct',
            'Suspended',
        ),
        description="""
        Sometimes the item could be in direct contact or suspended during the procedure.
        """,
        a_eln={'component': 'EnumEditQuantity'},
    )

    developing_mode = Quantity(
        type=MEnum(
            'auto',
            'manual',
        ),
        description='The step is executed manually or it is automatized?',
        a_eln={'component': 'EnumEditQuantity'},
    )
    developing_temperature = Quantity(
        type=np.float64,
        description="""
        Field describing an eventual temperature imposed to enanche the development
        """,
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

    final_rinsing = SubSection(
        section_def=SpinRinsingbase,
        description="""
        Rinsing phases are usually used to stop undesired reactions due to remaining
        developers solution on the surface.
        """,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class SpinResistDevelopmentbase(ResistDevelopmentbase):
    m_def = Section(description='Atomistic component of a spinned development step')

    spin_parameters = SubSection(section_def=SpinningComponent, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class ResistDevelopment(FabricationProcessStep):
    m_def = Section(
        description="""
        Process step, tipically executed after an exposure, which aim to remove the 
        resist, not more needed for the next steps, using a developer solution.
        """,
        a_eln={
            'hide': [
                'tag',
                'duration',
            ],
            'properties': {
                'order': [
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
        },
    )

    development_steps = SubSection(
        section_def=ResistDevelopmentbase,
        repeats=True,
    )

    outputs = SubSection(
        section_def=BaseOutputs,
        repeats=False,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class SpinResistDevelopment(ResistDevelopment):
    m_def = Section(
        description="""
        Process step, tipically executed after an exposure, which aim to remove the 
        resist not more needed for the next steps. A spinner is used to remove excess
        of developer solution or resist residual.
        """,
        a_eln={
            'hide': ['tag', 'duration'],
            'properties': {
                'order': [
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
        },
    )

    development_steps = SubSection(
        section_def=SpinResistDevelopmentbase,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
