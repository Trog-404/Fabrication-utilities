from typing import TYPE_CHECKING

from nomad.metainfo import (
    Package,
    Section,
    SubSection,
)
from schema_packages.fabrication_utilities import (
    FabricationProcessStep,
    FabricationProcessStepBase,
)
from schema_packages.steps.utils import SpinDryingbase, SpinRinsingbase

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger


m_package = Package(name='Drying steps schemas definitions for fabrication')


class Rinsing_Dryingbase(FabricationProcessStepBase):
    m_def = Section(
        description='Atomistic components of a rinsing drying process step',
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
                    'notes',
                ]
            }
        },
    )

    initial_rinsing_parameters = SubSection(section_def=SpinRinsingbase, repeats=False)

    drying_parameters = SubSection(section_def=SpinDryingbase, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class Rinsing_Drying(FabricationProcessStep):
    m_def = Section(
        description="""
        Fabrication process step consisting in a two phase procedure.(1) Initial
        rinsing to rid of eventual wet residuals; (2) a drying phase operable by heat
        on the wafers or by inactieve gas like N2 heated and pushed in the chamber (
        also both heating is possible in principle).
        """,
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
        },
    )

    rinsing_drying_steps = SubSection(section_def=Rinsing_Dryingbase, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
