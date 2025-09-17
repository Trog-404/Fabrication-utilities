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
from schema_packages.steps.utils import BaseOutputs, Massflow_controller
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
        }
    )

    ramp_up_temperature = SubSection(section_def=TimeRampTemperature, repeats=False)

    ramp_down_temperature = SubSection(section_def=TimeRampTemperature, repeats=False)

    annealed_material = SubSection(section_def=FabricationChemical, repeats=False)

    fluximeters = SubSection(section_def=Massflow_controller, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class Annealing(FabricationProcessStep):
    m_def = Section(
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
                    'operator',
                    'room',
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
                ]
            },
        },
    )

    annealing_steps = SubSection(section_def=Annealingbase, repeats=True)

    outputs = SubSection(section_def=BaseOutputs, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


m_package.__init_metainfo__()
