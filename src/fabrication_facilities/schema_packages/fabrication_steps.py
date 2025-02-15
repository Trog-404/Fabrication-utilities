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

from nomad.datamodel.data import (
    ArchiveSection,
    EntryData,
)
from nomad.datamodel.metainfo.basesections import (
    Process,
    ProcessStep,
)
from nomad.metainfo import (
    Datetime,
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.equipment import (
    Equipment,
    EquipmentReference,
    EquipmentTechnique,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Fablims Process Schema rev4')


class FabricationProductType(EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={'properties': {'order': ['name', 'description', 'id']}},
    )
    id = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )


class ListofProductType(EntryData, ArchiveSection):
    m_def = Section()

    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    available_products = SubSection(
        section_def=FabricationProductType,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `FabricationProcessProductType` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class FabricationProcessStepDefinition(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'description',
                    'id',
                    'name_equipment',
                    'equipment_reference',
                    'equipmentTechnique',
                    'technique_reference',
                ]
            }
        },
    )
    id = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    name_equipment = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    equipment_reference = Quantity(
        type=Equipment,
        a_eln={'component': 'ReferenceEditQuantity'},
    )
    equipmentTechnique = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    technique_reference = Quantity(
        type=EquipmentTechnique,
        a_eln={'component': 'ReferenceEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `FabricationProcessStepDefinition` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class FabricationProcessStep(ProcessStep, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'hide': [
                'comment',
                'duration',
            ],
            'properties': {
                'order': [
                    'job_progressive_id',
                    'name',
                    'description',
                    'start_time',
                    'ending_date',
                    'fabricationProcessStepDefinition',
                    'fabricationEquipmentRecipeName',
                    'notes',
                ],
            },
        },
    )
    job_progressive_id = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    start_time = Quantity(
        type=Datetime,
        a_eln={'label': 'starting date', 'component': 'DateTimeEditQuantity'},
    )
    ending_date = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    fabricationProcessStepDefinition = Quantity(
        type=FabricationProcessStepDefinition,
        a_eln={'component': 'ReferenceEditQuantity'},
    )
    fabricationEquipmentRecipeName = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity', 'label': 'recipe name'},
    )
    notes = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `FabricationProcessStep` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class FabricationProcess(Process, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'id',
                    'description',
                    'datetime',
                    'end_time',
                    'fabricationProductType',
                    'comment',
                ]
            },
            'hide': [
                'lab_id',
                'location',
                'method',
            ],
        },
    )
    id = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    datetime = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity', 'label': 'starting date'},
    )
    end_time = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity', 'label': 'ending date'},
    )
    comment = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity', 'label': 'notes'},
    )
    fabricationProductType = Quantity(
        type=ListofProductType,
        a_eln={'component': 'ReferenceEditQuantity'},
    )
    steps = SubSection(
        section_def=FabricationProcessStep,
        repeats=True,
    )
    instruments = SubSection(
        section_def=EquipmentReference,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `FabricationProcess` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


m_package.__init_metainfo__()
