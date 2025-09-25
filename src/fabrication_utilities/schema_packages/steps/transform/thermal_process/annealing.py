from typing import (
    TYPE_CHECKING,
)

from nomad.metainfo import (
    Package,
    Section,
    SubSection,
)
from schema_packages.fabrication_utilities import (
    FabricationProcessStep,
    FabricationProcessStepBase,
)
from schema_packages.steps.utils import AnnealingOutputs, Massflow_controller
from schema_packages.utils import FabricationChemical, TimeRampTemperature

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Schemas to describe annealing steps')


class Annealingbase(FabricationProcessStepBase):
    m_def = Section(
        description='Atomistic component of an annealing step',
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'tag',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'notes',
                ]
            }
        },
    )

    ramp_up = SubSection(section_def=TimeRampTemperature, repeats=False)

    ramp_down = SubSection(section_def=TimeRampTemperature, repeats=False)

    annealed_material = SubSection(section_def=FabricationChemical, repeats=False)

    fluximeters = SubSection(section_def=Massflow_controller, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class Annealing(FabricationProcessStep):
    m_def = Section(
        description="""
        Fabrication process step where the wafer or other item are inserted into a
        hermetically sealed furnace chamber where N2 is injected and the temperature
        rose until the target. Main aim of this process is recovering of damages
        induced by previous process steps, mainly ion implantation.
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
                    'notes',
                ]
            },
        },
    )

    annealing_steps = SubSection(section_def=Annealingbase, repeats=True)

    outputs = SubSection(section_def=AnnealingOutputs, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


m_package.__init_metainfo__()
