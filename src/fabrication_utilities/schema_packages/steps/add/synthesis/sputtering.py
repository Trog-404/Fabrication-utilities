from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.metainfo import Package, Quantity, Section, SubSection
from schema_packages.fabrication_utilities import (
    FabricationProcessStep,
    FabricationProcessStepBase,
)
from schema_packages.steps.utils import Chuck, SpinningComponent, SynthesisOutputs
from schema_packages.utils import FabricationChemical

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

m_package = Package(name='Schemas to describe the sputtering steps')


class Sputteringbase(FabricationProcessStepBase):
    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'tag',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'item_movement',
                    'index',
                    'delay_between_stack_layers',
                    'power',
                    'notes',
                ]
            }
        }
    )

    item_movement = Quantity(
        type=str,
        description='Movimentation the item is exposed to',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    index = Quantity(
        type=int,
        description='Deposition step index',
        a_eln={
            'component': 'NumberEditQuantity',
        },
    )
    delay_between_stack_layers = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    power = Quantity(
        type=np.float64,
        description='Power erogated to the sputterer',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'watt'},
        unit='watt',
    )
    material_deposited = SubSection(section_def=FabricationChemical, repeats=True)
    chuck = SubSection(section_def=Chuck, repeats=False)

    spin_parameters = SubSection(section_def=SpinningComponent, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class Sputtering(FabricationProcessStep):
    m_def = Section(
        a_eln={
            'hide': ['duration', 'tag'],
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
                    'deposition_rate_target',
                    'notes',
                ]
            },
        },
    )
    thickness_target = Quantity(
        type=np.float64,
        description='Amount of material to be deposited',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    duration_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    deposition_rate_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='nm/sec',
    )
    outputs = SubSection(section_def=SynthesisOutputs, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


m_package.__init_metainfo__()
