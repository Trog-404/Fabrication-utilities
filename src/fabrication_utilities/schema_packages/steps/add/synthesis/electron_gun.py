from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.metainfo import Package, Quantity, Section, SubSection
from schema_packages.fabrication_utilities import (
    FabricationProcessStep,
    FabricationProcessStepBase,
)
from schema_packages.steps.utils import ElectronGunOutputs, SpinningComponent
from schema_packages.utils import FabricationChemical

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

m_package = Package(name='ElectronGun fabrication steps schema')


class ElectronGunbase(FabricationProcessStepBase):
    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'tag',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'chamber_pressure',
                    'wafer_stack_name',
                    'notes',
                ]
            },
        },
    )

    chamber_pressure = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )

    wafer_stack_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )

    material_deposited = SubSection(section_def=FabricationChemical, repeats=True)
    spin_parameters = SubSection(section_def=SpinningComponent, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class ElectronGun(FabricationProcessStep):
    m_def = Section(
        a_eln={
            'hide': ['tag', 'duration'],
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
                    'notes',
                ]
            },
        },
    )

    thickness_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    duration_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )

    deposition_steps = SubSection(section_def=ElectronGunbase, repeats=True)

    outputs = SubSection(section_def=ElectronGunOutputs, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


m_package.__init_metainfo__()
