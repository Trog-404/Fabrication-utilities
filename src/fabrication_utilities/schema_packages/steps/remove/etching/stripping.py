from typing import TYPE_CHECKING

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
from schema_packages.utils import FabricationChemical

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger


m_package = Package(name='Stripping steps schema definition')


class Strippingbase(FabricationProcessStepBase):
    m_def = Section(
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
                    'stripping_type',
                    'removing_temperature',
                    'ultrasound_required',
                    'number of loops',
                    'notes',
                ]
            }
        }
    )
    stripping_type = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    removing_temperature = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    ultrasound_required = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )

    number_of_loops = Quantity(type=int, a_eln={'component': 'NumberEditQuantity'})

    resist_to_strip = SubSection(section_def=FabricationChemical, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class Stripping(FabricationProcessStep):
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
        },
    )

    stripping_steps = SubSection(section_def=Strippingbase, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
