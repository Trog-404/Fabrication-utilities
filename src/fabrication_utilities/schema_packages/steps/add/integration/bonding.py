from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.metainfo import MEnum, Package, Quantity, Section, SubSection
from schema_packages.fabrication_utilities import (
    FabricationProcessStep,
    FabricationProcessStepBase,
)
from schema_packages.steps.utils import BondingOutputs

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

m_package = Package(name='Schemas to describe the bonding steps')


class Bondingbase(FabricationProcessStepBase):
    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'tag',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'wafer_bonding_type',
                    'alignment_required',
                    'alignment_max_error',
                    'wafer_stack_1_name',
                    'wafer_stack_2_name',
                    'wafer_space_required',
                    'alignment_target_mask_name',
                    'alignment_viewfinder_mask_name',
                    'notes',
                ]
            },
        },
    )

    wafer_bonding_type = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    alignment_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    alignment_max_error = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    wafer_stack_1_name = Quantity(
        type=str,
        description='Name or in general of an identifier of one of the bonded items',
        a_eln={'component': 'StringEditQuantity'},
    )
    wafer_stack_2_name = Quantity(
        type=str,
        description='Name or in general of an identifier of one of the bonded items',
        a_eln={'component': 'StringEditQuantity'},
    )
    wafer_space_required = Quantity(
        type=bool,
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )
    alignment_target_mask_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    alignment_viewfinder_mask_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class Bonding(FabricationProcessStep):
    m_def = Section(
        a_eln={
            'hide': ['tag', 'duration', 'id_item_processed'],
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

    bonding_steps = SubSection(section_def=Bondingbase, repeats=True)

    outputs = SubSection(section_def=BondingOutputs, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
