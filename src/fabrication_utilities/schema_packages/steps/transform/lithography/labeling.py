from typing import (
    TYPE_CHECKING,
)

from nomad.metainfo import (
    MEnum,
    Package,
    Quantity,
    Section,
)
from schema_packages.fabrication_utilities import FabricationProcessStep

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Schema package for labeling step')


class LabelingCleaning(FabricationProcessStep):
    m_def = Section(
        a_eln={
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
                    'wafer_label_position',
                    'wafer_label_name',
                    'wafer_cleaning_DI_ultrasound_required',
                    'wafer_cleaning_rca_required',
                    'wafer_cleaning_piranha_required',
                    'wafer_cleaning_dipHF_required',
                    'wafer_cleaning_rinse_spin_dryer_required',
                    'notes',
                ]
            },
        },
    )
    wafer_label_position = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    wafer_label_name = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    wafer_cleaning_DI_ultrasound_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    wafer_cleaning_rca_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    wafer_cleaning_piranha_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    wafer_cleaning_dipHF_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    wafer_cleaning_rinse_spin_dryer_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
