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
from schema_packages.steps.utils import (
    BaseOutputs,
    Priming,
    ResistDescription,
    SpinningComponent,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )


m_package = Package(name='Schemas for coating steps in fabrication')


class Coatingbase(FabricationProcessStepBase):
    m_def = Section(
        description='Atomistic component of a general coating step',
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'tag',
                    'starting_date',
                    'ending_date',
                    'duration',
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
        description="""
        Field describing if the step is performed by an operator or automatically
        """,
        a_eln={'component': 'EnumEditQuantity'},
    )
    dispensing_locus = Quantity(
        type=str,
        description="""
        In which position of the item the solution is ideally dispensed. By default the
        center.
        """,
        a_eln={'component': 'StringEditQuantity'},
    )
    dispensed_volume = Quantity(
        type=np.float64,
        description='Quantity of solution dispensed',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'milliliter',
        },
        unit='milliliter',
    )
    clamping_type = Quantity(
        type=MEnum('None', 'Entire wafer', 'Edge clamping', 'Other (see notes)'),
        description="""
        Sometimes, tipically in spninned deposition, the item can be stable on a plate.
        """,
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
        At the end of the resist deposition is there a phase of polishing on the edges?
        """,
        a_eln={'component': 'BoolEditQuantity'},
    )
    resist_material = SubSection(section_def=ResistDescription, repeats=True)

    priming = SubSection(section_def=Priming, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class Spin_Coatingbase(Coatingbase):
    m_def = Section(
        description='Atomistic component of spin enanched coating procedure',
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'tag',
                    'starting_date',
                    'ending_date',
                    'duration',
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

    spin_phase = SubSection(section_def=SpinningComponent, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class Coating(FabricationProcessStep):
    m_def = Section(
        description="""
        Fabrication process step where a layer of a resist material is deposited one the
        surface of a material by dispensing the resist solution on the surface and 
        successively expanding on it the solution which needs to evaporate.
        """,
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
                    'wafer_side',
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

    coating_steps = SubSection(section_def=Coatingbase, repeats=True)

    outputs = SubSection(section_def=BaseOutputs, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class Spin_Coating(Coating):
    m_def = Section(
        description="""
        Fabrication process step where a layer of a resist material is deposited one the
        surface of a material by dispensing the resist solution on the surface and 
        successively spinning the item to distribute the resist.
        """,
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
                    'wafer_side',
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
                    'notes',
                ]
            },
        },
    )

    coating_steps = SubSection(section_def=Spin_Coatingbase, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


m_package.__init_metainfo__()
