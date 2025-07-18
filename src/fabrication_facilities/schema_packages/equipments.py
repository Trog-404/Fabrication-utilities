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
from nomad.metainfo import (
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.fabrication_utilities import Equipment
from fabrication_facilities.schema_packages.utils import Massflow_controller

if TYPE_CHECKING:
    pass

m_package = Package(name='Equipments specific definitions ')


class Massflow_parameter(Massflow_controller, ArchiveSection):
    m_def = Section(
        description='Class to describe flux of gases in fluximeters',
        a_eln={'hide': ['lab_id', 'datetime', 'massflow']},
    )

    min_massflow = Quantity(
        type=np.float64,
        description='Minimum rate at which the gas flows',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )
    max_massflow = Quantity(
        type=np.float64,
        description='Macimum rate at which the gas flows',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )


class RIE_Etcher(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_wall_temperature',
                    'max_wall_temperature',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                    'min_chuck_power',
                    'max_chuck_power',
                    'min_chuck_frequency',
                    'max_chuck_frequency',
                    'min_bias',
                    'max_bias',
                    'mechanical_clamping',
                    'electrostatic_clamping',
                    # 'min_cooling_helium_massflow',
                    # 'max_cooling_helium_massflow',
                    # 'min_cooling_helium_temperature',
                    # 'max_cooling_helium_temperature',
                ],
            },
        },
        description='Base classes for etching instruments',
    )

    vacuum_system_name = Quantity(
        type=str,
        description='Type of vacuum pump adopted',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    min_chamber_pressure = Quantity(
        type=np.float64,
        description='Minimal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    max_chamber_pressure = Quantity(
        type=np.float64,
        description='Maximal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    min_wall_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature at disposal for the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_wall_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    min_chuck_power = Quantity(
        type=np.float64,
        description='Minimal power erogated on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    max_chuck_power = Quantity(
        type=np.float64,
        description='Maximal power erogated on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    min_chuck_frequency = Quantity(
        type=np.float64,
        description='Minimal frequency of current on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )
    max_chuck_frequency = Quantity(
        type=np.float64,
        description='Maximal frequency of current on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )

    min_bias = Quantity(
        type=np.float64,
        description='Minimal bias voltage in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'volt',
        },
        unit='volt',
    )

    max_bias = Quantity(
        type=np.float64,
        description='Maximal bias voltage in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'volt',
        },
        unit='volt',
    )

    electrostatic_clamping = Quantity(
        type=bool,
        description='Is electrostatic clamping available',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )

    mechanical_clamping = Quantity(
        type=bool,
        description='Is mechanical clamping available',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )

    gases = SubSection(
        section_def=Massflow_parameter,
        repeats=True,
    )


class ICP_Etcher(RIE_Etcher, ArchiveSection):
    m_def = Section(
        description='Dry etching class for instruments where a plasma is involved',
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_wall_temperature',
                    'max_wall_temperature',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                    'min_chuck_power',
                    'max_chuck_power',
                    'min_chuck_frequency',
                    'max_chuck_frequency',
                    'min_icp_power',
                    'max_icp_power',
                    'min_icp_frequency',
                    'max_icp_frequency',
                    'min_bias',
                    'max_bias',
                    'mechanical_clamping',
                    'electrostatic_clamping',
                    'min_cooling_helium_massflow',
                    'max_cooling_helium_massflow',
                    'min_cooling_helium_temperature',
                    'max_cooling_helium_temperature',
                ],
            },
        },
    )

    min_icp_power = Quantity(
        type=np.float64,
        description='Minimal power erogated in the region of the plasma',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    max_icp_power = Quantity(
        type=np.float64,
        description='Maximal power erogated in the region of the plasma',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    min_icp_frequency = Quantity(
        type=np.float64,
        description='Minimal frequency of current on the gases area',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )

    max_icp_frequency = Quantity(
        type=np.float64,
        description='Maximal frequency of current on the gases area',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )

    min_cooling_helium_massflow = Quantity(
        type=np.float64,
        description='Minimum rate at which the helium for cooling the chuck flows',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )
    max_cooling_helium_massflow = Quantity(
        type=np.float64,
        description='Maximum rate at which the helium for cooling the chuck flows',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )

    min_cooling_helium_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the cooling helium on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_cooling_helium_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the cooling helium on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    # electrostatic_clamping = Quantity(
    #     type=bool,
    #     description = 'Is electrostatic clamping available',
    #     a_eln={
    #         'component': 'BoolEditQuantity',
    #     },
    # )

    # mechanical_clamping = Quantity(
    #     type=bool,
    #     description = 'Is mechanical clamping available',
    #     a_eln={
    #         'component': 'BoolEditQuantity',
    #     },
    # )

    # gases = SubSection(
    #     section_def=Massflow_parameter,
    #     repeats=True,
    # )


###############
# In futuro si deve aggiungere una sezione per gli items permessi ma per farlo
# bisogna prima lavorare sugli items stessi...
###############


class DRIE_Etcher(ICP_Etcher, ArchiveSection):
    m_def = Section(
        description='Dry etching instrument for deep geometries',
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_wall_temperature',
                    'max_wall_temperature',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                    'min_chuck_power',
                    'max_chuck_power',
                    'min_chuck_frequency',
                    'max_chuck_frequency',
                    'min_icp_power',
                    'max_icp_power',
                    'min_icp_frequency',
                    'max_icp_frequency',
                    'min_third_power',
                    'max_third_power',
                    'min_third_frequency',
                    'max_third_frequency',
                    'min_bias',
                    'max_bias',
                    'mechanical_clamping',
                    'electrostatic_clamping',
                    'min_cooling_helium_massflow',
                    'max_cooling_helium_massflow',
                    'min_cooling_helium_temperature',
                    'max_cooling_helium_temperature',
                    'passivation_material',
                ],
            },
        },
    )

    min_third_power = Quantity(
        type=np.float64,
        description='Minimal power erogated in the region of the plasma',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    max_third_power = Quantity(
        type=np.float64,
        description='Maximal power erogated in the region of the plasma',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    min_third_frequency = Quantity(
        type=np.float64,
        description='Minimal frequency of current on the gases area',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )

    max_third_frequency = Quantity(
        type=np.float64,
        description='Maximal frequency of current on the gases area',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )

    passivation_material = Quantity(
        type=str,
        description='Material at disposal for passivation',
        a_eln={'component': 'StringEditQuantity'},
    )


# class DRIE_BOSCH_Etcher (DRIE_Etcher, ArchiveSection):
#     m_def = Section(
#         description='Dry etching instrument for deep geometries with BOSCH technology',
#         a_eln={
#             'hide': [
#                 'lab_id',
#                 'datetime',
#             ],
#             'properties': {
#                 'order': [
#                     'name',
#                     'inventary_code',
#                     'affiliation',
#                     'product_model',
#                     'institution',
#                     'manufacturer_name',
#                     'is_bookable',
#                     'automatic_loading',
#                     'description',
#                     'min_chamber_pressure',
#                     'max_chamber_pressure',
#                     'vacuum_system_name',
#                     'min_wall_temperature',
#                     'max_wall_temperature',
#                     'min_chuck_temperature',
#                     'max_chuck_temperature',
#                     'min_chuck_power',
#                     'max_chuck_power',
#                     'min_chuck_frequency',
#                     'max_chuck_frequency',
#                     'min_icp_power',
#                     'max_icp_power',
#                     'min_icp_frequency',
#                     'max_icp_frequency',
#                     'min_bias',
#                     'max_bias',
#                     'mechanical_clamping',
#                     'electrostatic_clamping',
#                     'min_cooling_helium_massflow',
#                     'max_cooling_helium_massflow',
#                     'min_cooling_helium_temperature',
#                     'max_cooling_helium_temperature',
#                 ],
#             },
#         }
#     )


class LPCVD_System(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_wall_temperature',
                    'max_wall_temperature',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                    'min_chuck_power',
                    'max_chuck_power',
                    'min_chuck_frequency',
                    'max_chuck_frequency',
                    'min_bias',
                    'max_bias',
                    'mechanical_clamping',
                    'electrostatic_clamping',
                    # 'min_cooling_helium_massflow',
                    # 'max_cooling_helium_massflow',
                    # 'min_cooling_helium_temperature',
                    # 'max_cooling_helium_temperature',
                ],
            },
        },
        description='Instrument used to perform LPCVD steps',
    )

    vacuum_system_name = Quantity(
        type=str,
        description='Type of vacuum pump adopted',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    min_chamber_pressure = Quantity(
        type=np.float64,
        description='Minimal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    max_chamber_pressure = Quantity(
        type=np.float64,
        description='Maximal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    min_wall_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature at disposal for the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_wall_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    electrostatic_clamping = Quantity(
        type=bool,
        description='Is electrostatic clamping available',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )

    mechanical_clamping = Quantity(
        type=bool,
        description='Is mechanical clamping available',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )

    gases = SubSection(
        section_def=Massflow_parameter,
        repeats=True,
    )


class PECVD_System(LPCVD_System, ArchiveSection):
    m_def = Section(
        description='Class instrument for PECVD procedures',
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_wall_temperature',
                    'max_wall_temperature',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                    'min_chuck_power',
                    'max_chuck_power',
                    'min_chuck_frequency',
                    'max_chuck_frequency',
                    'min_bias',
                    'max_bias',
                    'mechanical_clamping',
                    'electrostatic_clamping',
                    'min_cooling_helium_massflow',
                    'max_cooling_helium_massflow',
                    'min_cooling_helium_temperature',
                    'max_cooling_helium_temperature',
                ],
            },
        },
    )

    min_chuck_power = Quantity(
        type=np.float64,
        description='Minimal power erogated on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    max_chuck_power = Quantity(
        type=np.float64,
        description='Maximal power erogated on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    min_chuck_frequency = Quantity(
        type=np.float64,
        description='Minimal frequency of current on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )
    max_chuck_frequency = Quantity(
        type=np.float64,
        description='Maximal frequency of current on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )

    min_bias = Quantity(
        type=np.float64,
        description='Minimal bias voltage in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'volt',
        },
        unit='volt',
    )

    max_bias = Quantity(
        type=np.float64,
        description='Maximal bias voltage in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'volt',
        },
        unit='volt',
    )

    min_cooling_helium_massflow = Quantity(
        type=np.float64,
        description='Minimum rate at which the helium for cooling the chuck flows',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )
    max_cooling_helium_massflow = Quantity(
        type=np.float64,
        description='Maximum rate at which the helium for cooling the chuck flows',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )

    min_cooling_helium_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the cooling helium on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_cooling_helium_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the cooling helium on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )


class ICP_CVD_System(PECVD_System, ArchiveSection):
    m_def = Section(
        description='Class for instruments devoted to ICP_CVD procedures',
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_wall_temperature',
                    'max_wall_temperature',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                    'min_chuck_power',
                    'max_chuck_power',
                    'min_chuck_frequency',
                    'max_chuck_frequency',
                    'min_icp_power',
                    'max_icp_power',
                    'min_icp_frequency',
                    'max_icp_frequency',
                    'min_bias',
                    'max_bias',
                    'mechanical_clamping',
                    'electrostatic_clamping',
                    'min_cooling_helium_massflow',
                    'max_cooling_helium_massflow',
                    'min_cooling_helium_temperature',
                    'max_cooling_helium_temperature',
                ],
            },
        },
    )

    min_icp_power = Quantity(
        type=np.float64,
        description='Minimal power erogated in the region of the plasma',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    max_icp_power = Quantity(
        type=np.float64,
        description='Maximal power erogated in the region of the plasma',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    min_icp_frequency = Quantity(
        type=np.float64,
        description='Minimal frequency of current on the gases area',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )

    max_icp_frequency = Quantity(
        type=np.float64,
        description='Maximal frequency of current on the gases area',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )


class BakingFurnace(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                ],
            },
        }
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )


class ElectronBeamLithographer(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                    'min_dose',
                    'max_dose',
                    'min_writing_field_dimension',
                    'max_writing_field_dimension',
                    'min_address_size',
                    'max_address_size',
                    'min_clock',
                    'max_clock',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'min_tension',
                    'max_tension',
                    'min_current',
                    'max_current',
                ],
            },
        }
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    min_tension = Quantity(
        type=np.float64,
        description='Minimal voltage in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'volt',
        },
        unit='volt',
    )

    max_tension = Quantity(
        type=np.float64,
        description='Maximal voltage in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'volt',
        },
        unit='volt',
    )

    min_chamber_pressure = Quantity(
        type=np.float64,
        description='Minimal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    max_chamber_pressure = Quantity(
        type=np.float64,
        description='Maximal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    min_dose = Quantity(
        type=np.float64,
        description='Minimal dose to use in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter^2',
        },
        unit='uC/centimeter^2',
    )

    max_dose = Quantity(
        type=np.float64,
        description='Maximal dose to use in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter^2',
        },
        unit='uC/centimeter^2',
    )

    min_writing_field_dimension = Quantity(
        type=np.float64,
        description='Lower area covered globally in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um^2',
        },
        unit='um^2',
    )

    max_writing_field_dimension = Quantity(
        type=np.float64,
        description='Maximum area covered globally in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um^2',
        },
        unit='um^2',
    )
    min_address_size = Quantity(
        type=np.float64,
        description='The minimum distance covered per step in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )

    max_address_size = Quantity(
        type=np.float64,
        description='The minimum distance covered per step in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )
    min_clock = Quantity(
        type=np.float64,
        description='Minimum frequency at disposal',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )
    max_clock = Quantity(
        type=np.float64,
        description='Maximum frequency at disposal',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )
    min_current = Quantity(
        type=np.float64,
        description='Current provided',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'pampere',
        },
        unit='pampere',
    )
    max_current = Quantity(
        type=np.float64,
        description='Current provided',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'pampere',
        },
        unit='pampere',
    )


class FocusedIonBeamLithographer(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                    'min_dose',
                    'max_dose',
                    'min_writing_field_dimension',
                    'max_writing_field_dimension',
                    'min_address_size',
                    'max_address_size',
                    'min_clock',
                    'max_clock',
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'min_tension',
                    'max_tension',
                    'min_current',
                    'max_current',
                ],
            },
        }
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    min_tension = Quantity(
        type=np.float64,
        description='Minimal voltage in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'volt',
        },
        unit='volt',
    )

    max_tension = Quantity(
        type=np.float64,
        description='Maximal voltage in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'volt',
        },
        unit='volt',
    )

    min_chamber_pressure = Quantity(
        type=np.float64,
        description='Minimal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    max_chamber_pressure = Quantity(
        type=np.float64,
        description='Maximal pressure available',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    min_dose = Quantity(
        type=np.float64,
        description='Minimal dose to use in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter^2',
        },
        unit='uC/centimeter^2',
    )

    max_dose = Quantity(
        type=np.float64,
        description='Maximal dose to use in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter^2',
        },
        unit='uC/centimeter^2',
    )

    min_writing_field_dimension = Quantity(
        type=np.float64,
        description='Lower area covered globally in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um^2',
        },
        unit='um^2',
    )

    max_writing_field_dimension = Quantity(
        type=np.float64,
        description='Maximum area covered globally in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um^2',
        },
        unit='um^2',
    )
    min_address_size = Quantity(
        type=np.float64,
        description='The minimum distance covered per step in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )

    max_address_size = Quantity(
        type=np.float64,
        description='The minimum distance covered per step in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )
    min_clock = Quantity(
        type=np.float64,
        description='Minimum frequency at disposal',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )
    max_clock = Quantity(
        type=np.float64,
        description='Maximum frequency at disposal',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )
    min_current = Quantity(
        type=np.float64,
        description='Current provided',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'pampere',
        },
        unit='pampere',
    )
    max_current = Quantity(
        type=np.float64,
        description='Current provided',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'pampere',
        },
        unit='pampere',
    )


class ResistDeveloper(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                ],
            },
        }
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )


class Spinner(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                ],
            },
        }
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )


class Rinser(Equipment, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                    'min_chuck_temperature',
                    'max_chuck_temperature',
                ],
            },
        }
    )

    min_chuck_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chuck_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
