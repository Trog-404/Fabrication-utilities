####################################### COATING #######################################
#######################################################################################
#     Synthesis sub category where a layer of material is deposited from a liquid     #
#                              solution onto a substrate                              #
#######################################################################################

from typing import (
    TYPE_CHECKING,
)

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
from schema_packages.steps.utils import Priming, SpinningComponent
from schema_packages.utils import FabricationChemical

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )


m_package = Package(name='Schemas for coating steps in fabrication')


class Spin_Coatingbase(FabricationProcessStepBase):
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
                    'resist_name',
                    'chemical_formula',
                    'resist_type',
                    'dispensing_mode',
                    'dispensing_locus',
                    'dispensed_volume',
                    'clamping_type',
                    'back_rinsing',
                    'edge_rinsing',
                    'notes',
                ]
            },
        },
    )
    dispensing_mode = Quantity(
        type=MEnum(
            'auto',
            'manual',
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    dispensing_locus = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    dispensed_volume = Quantity(
        type=np.float64,
        description='Solution dispensed',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'milliliter',
        },
        unit='milliliter',
    )
    clamping_type = Quantity(
        type=MEnum('None', 'Entire wafer', 'Edge clamping', 'Other (see notes)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    back_rinsing = Quantity(
        type=bool,
        description="""
        At the end of the resist deposition is there a phase of polishing on the back?
        """,
        a_eln={'component': 'BoolEditQuantity'},
    )
    edge_rinsing = Quantity(
        type=bool,
        description="""
        At the end of the resist deposition is there a phase of polishing on the sides?
        """,
        a_eln={'component': 'BoolEditQuantity'},
    )
    resist_material = SubSection(section_def=FabricationChemical, repeats=True)

    priming = SubSection(section_def=Priming, repeats=False)

    spin_phase = SubSection(section_def=SpinningComponent, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class Spin_Coating(FabricationProcessStep):
    m_def = Section(
        a_eln={
            'hide': ['duration', 'tag', 'operator'],
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
                    'wafer_side',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'thickness_target',
                    'notes',
                ]
            },
        },
    )

    wafer_side = Quantity(
        type=MEnum(
            'front',
            'back',
        ),
        description='Side exposed in the process',
        a_eln={'component': 'EnumEditQuantity'},
    )

    thickness_target = Quantity(
        type=np.float64,
        description='Amount of resist to be deposited',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )

    spin_coating_steps = SubSection(section_def=Spin_Coatingbase, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
