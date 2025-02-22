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
    EntryData,
)
from nomad.datamodel.metainfo.eln import Instrument
from nomad.datamodel.metainfo.workflow import Link
from nomad.metainfo import (
    Datetime,
    MEnum,
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.Items import ItemPropertyDefinition

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='FABLIMS Equipment Schema')


class FinalTechnique(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={'properties': {'order': ['name', 'id', 'description', 'comment']}},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    id = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    comment = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `finaltechnique` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class Jobdone(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'job_number',
                    'notes',
                    'starting_date',
                    'ending_date',
                    'id_item_processed',
                    'referenced_activity',
                ]
            }
        },
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    job_number = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    notes = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    starting_date = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    ending_date = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    id_items_processed = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
        shape=['*'],
    )
    referenced_activity = Quantity(
        type=FinalTechnique,
        a_eln={'component': 'ReferenceEditQuantity'},
        shape=['*'],
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `Jobdone` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class TechniqueSubCategory(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={'properties': {'order': ['name', 'id', 'description', 'notes']}},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    id = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    comment = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    Specific_techniques = SubSection(
        section_def=FinalTechnique,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `techniqueSubCategory` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class TechniqueMainCategory(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={'properties': {'order': ['name', 'id', 'description', 'comment']}},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    id = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    comment = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    superclass = Quantity(
        type=MEnum(
            [
                'Add',
                'CharacterizationRemove',
                'Transform',
            ]
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    SubCategories = SubSection(
        section_def=TechniqueSubCategory,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `techniqueMainCategory` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class TechniqueCategories(EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={'properties': {'order': ['description', 'comment']}},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    comment = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    techniqueMainCategories = SubSection(
        section_def=TechniqueMainCategory,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `TechniqueCategories` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class EquipmentTechnique(ArchiveSection):
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
                    'genericEquipmentName',
                    'techniqueMainCategory',
                    'techniqueSubCategory',
                ]
            }
        },
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    id = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    genericEquipmentName = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    techniqueMainCategory = Quantity(
        type=MEnum(
            [
                'synthesis',
                'integration',
                'doping',
                'dicing',
                'thermal processing',
                'lithography',
                'etching',
            ]
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    techniqueSubCategory = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    referencingcategorization = Quantity(
        type=TechniqueCategories,
        description='Reference to the taxonomy adopted',
        a_eln={'component': 'ReferenceEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `EquipmentTechnique` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class ItemPermittedPropertyDefinition(ItemPropertyDefinition, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(a_eln={'hide': ['value']})

    valuemax = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    valuemin = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `ItemPermittedPropertyDefinition` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class EquipmentHasPermittedItemPropertyData(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={'properties': {'order': ['id', 'ItemShapeType']}},
    )
    id = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    itemShapeType = Quantity(
        type=MEnum(
            [
                'Wafer with flat standard',
                'Wafer with flat JEIDA',
                'Rectangle shape',
                '1/2 wafer',
                '1/4 wafer',
                'Fragment',
                'Square shape',
                'Powder',
                'Wafer with Notch standard',
            ]
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    properties = SubSection(
        section_def=ItemPermittedPropertyDefinition,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `EquipmentHasPermittedItemPropertyData` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class EquipmentParameterData(ItemPermittedPropertyDefinition, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `EquipmentParameterData` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class Equipment(Instrument, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    iventary_code = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    institution = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    manufacturer = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    productModel = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    automatization = Quantity(
        type=bool,
        a_eln={'component': 'BoolEditQuantity'},
    )
    is_bookable = Quantity(
        type=bool,
        a_eln={'component': 'BoolEditQuantity'},
    )
    capabilities = SubSection(section_def=EquipmentParameterData, repeats=True)
    equipmentTechniques = SubSection(
        section_def=EquipmentTechnique,
        repeats=True,
    )
    permittedItems = SubSection(
        section_def=EquipmentHasPermittedItemPropertyData,
        repeats=True,
    )
    equipmentLogBook = SubSection(
        section_def=Jobdone,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `Equipment` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class EquipmentReference(Link, ArchiveSection):
    m_def = Section()

    id = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    notes = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )

    section = Quantity(
        type=Instrument,
        a_eln={'component': 'ReferenceEditQuantity'},
    )


m_package.__init_metainfo__()
