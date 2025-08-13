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
# py module dedicated to characterization tools based on
# equipments.py
from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import (
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.fabrication_utilities import Equipment
from fabrication_facilities.schema_packages.steps.character import (
    CharacterizationTechnique,
)

if TYPE_CHECKING:
    pass

m_package = Package(name='Characterization equipment specific definitions ')


#######################################################################################
################################ AFM ##################################################
#######################################################################################
class CharactEquipmentBase(Equipment):
    m_def = Section(
        a_eln={
            'hide': [
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'notes',
                ],
            },
        }
    )
    lab_id = Quantity(
        type=str,
        description='ID assigned by lab for findability',
        a_eln={'component': 'StringEditQuantity', 'label': 'id'},
    )
    inventary_code = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    affiliation = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    institution = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    manufacturer_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    product_model = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    automatic_loading = Quantity(
        type=bool,
        a_eln={'component': 'BoolEditQuantity'},
    )
    is_bookable = Quantity(
        type=bool,
        a_eln={'component': 'BoolEditQuantity'},
    )
    contamination_class = Quantity(
        type=int,
        description='Level of quality of the environment in the equipment',
        a_eln={'component': 'NumberEditQuantity'},
    )
    notes = Quantity(
        type=str,
        a_eln={
            'component': 'RichTextEditQuantity',
        },
    )
    equipmentTechniques = SubSection(
        section_def=CharacterizationTechnique,
        repeats=True,
    )


class AFM_System(CharactEquipmentBase, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'notes',
                    'afm_tip',
                    'afm_mode',
                    'afm_setpoint',
                ],
            },
        }
    )
    afm_tip = Quantity(
        type=str,
        description='the model of the probing tip',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    afm_mode = Quantity(
        type=str,
        description='if proxy or in contact, if linear or scanning',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    afm_setpoint = Quantity(
        type=np.float64,
        description='applied force',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='mA',
    )

class FourPointProbe_System(CharactEquipmentBase, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'lab_id',
                    'description',
                    'affiliation',
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'is_bookable',
                    'automatic_loading',
                    'contamination_class',
                    'notes',
                    'measured_sheet_resistance_min',
                    'measured_sheet_resistance_max',
                    'measured_resistivity_min',
                    'measured_resistivity_max',
                    'current_source_min',
                    'current_source_max',
                    'probe_head_pin_spacing',
                    'probe_head_pin_load',
                    'probe_head_pin_radius',
                    'needles_composition',
                    'needles_radius',
                ],
            },
        }
    )
    measured_sheet_resistance_min = Quantity(
        type=np.float64,
        description='minimum mesaurable sheet resistence',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        #unit='Ohm/sq',
    )
    measured_sheet_resistance_max = Quantity(
        type=np.float64,
        description='maximum mesaurable sheet resistence',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        #unit='Ohm/sq',
    )
    measured_resistivity_min = Quantity(
        type=np.float64,
        description='minimum mesaurable resistivity',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        #unit='Ohm*cm',
    )
    measured_resistivity_max = Quantity(
        type=np.float64,
        description='maximinimum mesaurable resistivity',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        #unit='Ohm*cm',
    )
    current_source_min = Quantity(
        type=np.float64,
        description='minimum applied current',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='A',
    )
    current_source_max = Quantity(
        type=np.float64,
        description='maximum applied current',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='A',
    )
    probe_head_pin_spacing = Quantity(
        type=np.float64,
        description='distance among needles',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        #unit='mils',
    )
    probe_head_pin_load_min = Quantity(
        type=np.float64,
        description='minumum applied pin load',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        #unit='g',
    )
    probe_head_pin_load_max = Quantity(
        type=np.float64,
        description='maximum applied pin load',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        #unit='g',
    )
    needles_composition = Quantity(
        type=str,
        description='needle materials',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    needles_radius = Quantity(
        type=np.float64,
        description='needle tip diameter',
        a_eln={
            'component': 'NumberEditQuantity',
        },
        unit='mm',
    )

