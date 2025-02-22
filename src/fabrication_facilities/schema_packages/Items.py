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
# import datetime
from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import (
    ArchiveSection,
    EntryData,
)
from nomad.datamodel.metainfo.basesections import (
    Entity,
    ElementalComposition,
    ProcessStep,
)
from nomad.datamodel.metainfo.eln import Chemical
from nomad.datamodel.metainfo.workflow import Link
from nomad.metainfo import (
    MEnum,
    Package,
    Quantity,
    Section,
    SubSection,
)
from fabrication_facilities.schema_packages.utils import parse_chemical_formula


if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Items plugin')


# In questa parte del plugin non mi piace come si inseriscono le proprietà degli items
# forse sarebbe il caso di definirle una per una
from nomad.metainfo import Section, Quantity, SubSection
import numpy as np


class ItemPropertyDefinition(ArchiveSection):
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
                    'unit',
                    'value',
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
    unit = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    value = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )


class StringProperties(ItemPropertyDefinition):
    m_def = Section()
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
    value = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )


class NumericProperties(ItemPropertyDefinition):
    m_def = Section()
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
    unit = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    value = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )


class DopingProperties(ItemPropertyDefinition):
    m_def = Section(
        a_eln={'hide': ['unit']},
    )
    id = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    doping_type = Quantity(
        type=MEnum(
            [
                'p',
                'n',
                'no',
            ]
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    value = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'ppm',
        },
        unit='ppm',
    )


class ItemShapeType(ArchiveSection):
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
        a_eln={'component': 'StringEditQuantity'},
    )


class ListOfItemPropertyDefinition(EntryData, ArchiveSection):
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
                ]
            }
        },
    )

    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    id = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    list_of_possible_properties = SubSection(
        section_def=ItemPropertyDefinition,
        repeats=True,
    )
    list_of_items_shape_type = SubSection(
        section_def=ItemShapeType,
        repeats=True,
    )


class StartingMaterial(Chemical, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': ['name', 'lab_id'],
            'properties': {
                'order': [
                    'wafer_material',
                    'chemical_formula',
                    'manufacturer_name',
                    'datetime',
                    'wafer_doping',
                ],
            },
        }
    )
    wafer_material = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    manufacturer_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    wafer_doping = Quantity(
        type=MEnum(
            'p',
            'n',
            'no',
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    elemental_composition = SubSection(section_def=ElementalComposition, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.chemical_formula:
            elements, counts = parse_chemical_formula(self.chemical_formula)
            total = 0
            for token in counts:
                total += int(token)
            if total != 0:
                elemental_fraction = np.array(counts) / total
                elementality = []
                i = 0
                for entry in elements:
                    elemental_try = ElementalComposition()
                    elemental_try.element = entry
                    elemental_try.atomic_fraction = elemental_fraction[i]
                    i += 1
                    elementality.append(elemental_try)
            else:
                print('No elements provided')
            self.elemental_composition = elementality


class Item(Entity, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'hide': ['lab_id', 'name'],
            'properties': {
                'order': [
                    'id_wafer_parent',
                    'datetime',
                    'itemShapeType',
                    'id',
                    'isAssembly',
                    'ids_components',
                ],
            },
        }
    )
    id_wafer_parent = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    datetime = Quantity(a_eln={'label': 'date of creation'})
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
    id = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    isAssembly = Quantity(
        type=bool,
        a_eln={'component': 'BoolEditQuantity'},
    )
    ids_components = Quantity(
        type=str,
        shape=['*'],
        a_eln={'component': 'StringEditQuantity'},
    )
    properties = SubSection(
        section_def=ItemPropertyDefinition,
        repeats=True,
    )


class SampleParenting(Entity, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'hide': ['lab_id'],
            'properties': {
                'order': [
                    'name',
                    'datetime',
                    'id',
                ],
            },
        }
    )
    inputs = SubSection(
        section_def=StartingMaterial,
        repeats=True,
    )
    parenting_steps = SubSection(section_def=ProcessStep, repeats=True)
    outputs = SubSection(
        section_def=Item,
        repeats=True,
    )


class SampleParentingLink(Link, ArchiveSection):
    m_def = Section()

    Section = Quantity(
        type=SampleParenting,
        a_eln={'component': 'ReferenceEditQuantity'},
    )


m_package.__init_metainfo__()
