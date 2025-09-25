from typing import (
    TYPE_CHECKING,
)

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
from schema_packages.steps.utils import (
    Alignment,
    BeamColumn,
    DirectLitoOutputs,
    WritingParameters,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Schemas to describe ebl steps')


class EBLbase(FabricationProcessStepBase):
    m_def = Section(
        description='Atomistic component of an EBL step',
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'tag',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'chamber_pressure',
                    'notes',
                ]
            },
        },
    )

    chamber_pressure = Quantity(
        type=np.float64,
        description='Pressure in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    writing_settings = SubSection(
        section_def=WritingParameters,
        repeats=False,
    )

    beam_column = SubSection(section_def=BeamColumn, repeats=False)

    alignment = SubSection(section_def=Alignment, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class EBL(FabricationProcessStep):
    m_def = Section(
        description="""
        Direct write patterning process that uses a focused, concentrated stream of
        electrons to modify the solubility of a resist layer.
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
                    'duration_target',
                    'notes',
                ]
            },
        },
    )
    recipe_name = Quantity(
        type=str,
        description='Name of the file that contains the geometry to impress',
        a_eln={
            'label': 'file CAD name',
            'component': 'StringEditQuantity',
        },
    )
    recipe_file = Quantity(
        type=str,
        description='Name of the file that contains the geometry to impress',
        a_eln={
            'label': 'file CAD',
            'component': 'FileEditQuantity',
        },
    )
    duration_target = Quantity(
        type=np.float64,
        description='Duration of the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )
    writing_steps = SubSection(
        section_def=EBLbase,
        repeats=True,
    )
    outputs = SubSection(
        section_def=DirectLitoOutputs,
        repeats=False,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


m_package.__init_metainfo__()
