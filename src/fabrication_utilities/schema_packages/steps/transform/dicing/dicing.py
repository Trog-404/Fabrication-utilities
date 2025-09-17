from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.metainfo import Package, Quantity, Section, SubSection
from schema_packages.fabrication_utilities import (
    FabricationProcessStep,
    FabricationProcessStepBase,
)
from schema_packages.steps.utils import DicingOutputs

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package('Schemas to describe dicing steps')


class Dicingbase(FabricationProcessStepBase):
    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'tag',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'protective_film_required',
                    'spindle_frequency',
                    'dicing_feed_rate',
                    'depth_step',
                    'notes',
                ]
            }
        }
    )

    protective_film_required = Quantity(
        type=bool,
        a_eln={
            'label': 'Protective film',
            'component': 'BoolEditQuantity',
        },
    )
    spindle_frequency = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'rpm',
        },
        unit='rpm',
    )
    dicing_feed_rate = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mm/s',
        },
        unit='mm/s',
    )
    depth_step = Quantity(
        type=np.float64,
        description='In a multistep dicing process the depth for each particular step',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um',
        },
        unit='um',
    )


class Dicing(FabricationProcessStep):
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
                    'blade_name',
                    'depth_target',
                    'notes',
                ]
            },
        },
    )

    dicing_blade_name = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    depth_target = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um',
        },
        unit='um',
    )

    dicing_steps = SubSection(section_def=Dicingbase, repeats=True)

    outputs = SubSection(section_def=DicingOutputs, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


m_package.__init_metainfo__()
