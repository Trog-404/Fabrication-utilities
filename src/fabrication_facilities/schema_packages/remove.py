#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import (
    ArchiveSection,
)
from nomad.datamodel.metainfo.eln import Chemical
from nomad.metainfo import (
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.fabrication_steps import (
    FabricationProcessStep,
)
from fabrication_facilities.schema_packages.transform import DevelopingStep
from fabrication_facilities.schema_packages.utils import Massflow_controller

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Etching workflow schema')


class EtchingRIE(FabricationProcessStep, Chemical, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
            ],
            'properties': {
                'order': [
                    'name',
                    'job_progressive_id',
                    'start_time',
                    'ending_date',
                    'fabricationProcessStepDefinition',
                    'fabricationEquipmentRecipeName',
                    'depth_from_recipe',
                    'duration_from_recipe',
                    'etching_rate_from_recipe',
                    'short_name',
                    'chemical_formula',
                    'depth_target',
                    'chamber_pressure',
                    'chuck_temperature',
                    'power',
                    'bias',
                    'depth_obtained',
                    'duration_effective',
                    'etching_rate_obtained',
                    'notes',
                ]
            },
        },
    )
    depth_from_recipe = Quantity(
        type=np.float64,
        description='Amount of material etched as described in the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um'},
        unit='um',
    )
    duration_from_recipe = Quantity(
        type=np.float64,
        description='Time prescribed by the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    etching_rate_from_recipe = Quantity(
        type=np.float64,
        description='Etching rate provided in the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um/minute'},
        unit='um/minute',
    )
    short_name = Quantity(
        type=str,
        description='Material to be etched',
        a_eln={'component': 'StringEditQuantity', 'label': 'target material'},
    )
    chemical_formula = Quantity(
        type=str,
        description='Inserted only if known',
        a_eln={'component': 'StringEditQuantity'},
    )
    depth_target = Quantity(
        type=np.float64,
        description='Amount of material to be etched',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um'},
        unit='um',
    )
    chamber_pressure = Quantity(
        type=np.float64,
        description='Pressure in the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )
    chuck_temperature = Quantity(
        type=np.float64,
        description='Temperature of the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    power = Quantity(
        type=np.float64,
        description='Power erogated',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'watt'},
        unit='watt',
    )
    bias = Quantity(
        type=np.float64,
        description='Bias voltage in the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'volt'},
        unit='volt',
    )
    depth_obtained = Quantity(
        type=np.float64,
        description='Amount of material ethced effectively in the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um'},
        unit='um',
    )
    duration_effective = Quantity(
        type=np.float64,
        description='Real time of the process ad output',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    etching_rate_obtained = Quantity(
        type=np.float64,
        description='Etching rate as output',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um/minute'},
        unit='um/minute',
    )
    fluximeters = SubSection(
        section_def=Massflow_controller,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `Step` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class WetCleaning(DevelopingStep, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
            ],
            'properties': {
                'order': [
                    'name',
                    'job_progressive_id',
                    'start_time',
                    'ending_date',
                    'fabricationProcessStepDefinition',
                    'fabricationEquipmentRecipeName',
                    'developing_solution',
                    'devoloping_solution_proportions',
                    'developing_duration',
                    'cleaning_solution',
                    'cleaning_solution_proportions',
                    'cleaning_duration',
                    'notes',
                ]
            },
        },
    )

    developing_solution = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity', 'label': 'removing_solution'},
    )
    developing_solution_proportions = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'removing solution proportions',
        },
    )
    developing_duration = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
            'label': 'removing duration',
        },
        unit='sec',
    )
    cleaning_solution = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'rising solution',
        },
    )
    cleaning_solution_proportions = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'rising solution proportions',
        },
    )
    cleaning_duration = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
            'label': 'rising duration',
        },
        unit='sec',
    )


m_package.__init_metainfo__()
