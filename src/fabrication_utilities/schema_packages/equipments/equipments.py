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
from nomad.datamodel.data import ArchiveSection, EntryData
from nomad.datamodel.metainfo.eln import Instrument
from nomad.metainfo import (
    Package,
    Quantity,
    Section,
    SubSection,
)
from schema_packages.equipments.utils import (
    BeamColumnCapabilites,
    CarrierDescription,
    ChuckCapabilities,
    DryerGasParameter,
    ICP_ColumnCapabilities,
    Massflow_parameter,
    ResistivityControlSystem,
    SpinnerSpinParameters,
    WetSolutionComponents,
    WritingCapabilities,
)
from schema_packages.fabrication_utilities import Equipment
from schema_packages.utils import FabricationChemical

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Equipments specific definitions ')

#######################################################################################
########################### ANCILLARY TECHNIQUES EQUIPMENTS ###########################
#######################################################################################


class Spinner(Equipment):
    m_def = Section(
        description='Class for instruments devoted to spinning procedures.',
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
                ]
            },
        },
    )

    spin_capabilities = SubSection(
        section_def=SpinnerSpinParameters,
        repeats=False,
    )


class SpinCoater(Spinner):
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
                    'back_rinsing',
                    'side_rinsing',
                    'notes',
                ]
            },
        }
    )

    back_rinsing = Quantity(
        type=bool,
        description="""
        At the end of the resist deposition is there a phase of polishing on the back?
        """,
        a_eln={'component': 'BoolEditQuantity'},
    )
    side_rinsing = Quantity(
        type=bool,
        description="""
        At the end of the resist deposition is there a phase of polishing on the sides?
        """,
        a_eln={'component': 'BoolEditQuantity'},
    )

    primers_available = SubSection(section_def=FabricationChemical, repeats=True)

    resist_available = SubSection(section_def=FabricationChemical, repeats=True)


class ResistDeveloper(Equipment):
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

    developers_available = SubSection(section_def=FabricationChemical, repeats=True)


class ResistSpinDeveloper(ResistDeveloper, Spinner):
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


class Rinser_Dryer(Spinner):
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
                    'max_temperature',
                    'notes',
                ],
            },
        }
    )

    max_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature to dry directly on the carrier',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    available_resistivity_settings = SubSection(
        section_def=ResistivityControlSystem, repeats=False
    )

    drying_gas = SubSection(section_def=DryerGasParameter, repeats=False)


class BakingFurnace(Equipment):
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
                    'min_baking_temperature',
                    'max_baking_temperature',
                    'min_baking_pressure',
                    'max_baking_pressure',
                    'notes',
                ],
            },
        }
    )

    min_baking_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature available in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_baking_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature available in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    min_baking_pressure = Quantity(
        type=np.float64,
        description='Minimal pressure available in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    max_baking_pressure = Quantity(
        type=np.float64,
        description='Maximal pressure available in the chamber',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )


#######################################################################################
################################ DRY ETCHING EQUIPMENTS ###############################
#######################################################################################


class RIE_Etcher(Equipment):
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
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_chamber_temperature',
                    'max_chamber_temperature',
                    'notes',
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

    min_chamber_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature at disposal for the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chamber_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    gases = SubSection(
        section_def=Massflow_parameter,
        repeats=True,
    )

    chuck = SubSection(
        section_def=ChuckCapabilities,
        repeats=False,
    )


class ICP_RIE_Etcher(RIE_Etcher):
    m_def = Section(
        description='Dry etching class for instruments where a plasma is involved',
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
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_chamber_temperature',
                    'max_chamber_temperature',
                    'notes',
                ],
            },
        },
    )

    icp_parameters = SubSection(
        section_def=ICP_ColumnCapabilities,
        repeats=False,
    )


class DRIE_BOSCH_Etcher(ICP_RIE_Etcher):
    m_def = Section(
        description='Dry etching instrument for deep geometries',
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
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_chamber_temperature',
                    'max_chamber_temperature',
                    'notes',
                ],
            },
        },
    )


#######################################################################################
################################ WET STEPS EQUIPMENTS #################################
#######################################################################################


class Wet_Bench_Unit(Equipment):
    m_def = Section(
        description="""
        Bath containing a chemical solution or pure substance to perform wet processes,
        """,
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
                    'hood_system',
                    'volume_of_solution',
                    'min_bath_temperature',
                    'max_bath_temperature',
                    'max_overflow_time',
                    'pumping_mechanism',
                    'solution_renewal',
                    'max_number_of_repetitions',
                    'max_time_of_usage',
                    'notes',
                ]
            },
        },
    )

    hood_system = Quantity(
        type=str,
        description="""
        Name of the hood system used for safety. It could be used also to identify the
        location of each tank in the labs.
        """,
        a_eln={'component': 'StringEditQuantity'},
    )

    volume_of_solution = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'liter'},
        unit='liter',
    )

    min_bath_temperature = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    max_bath_temperature = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    max_overflow_time = Quantity(
        type=np.float64,
        description='Maximum amount of time flow imposed',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )

    pumping_mechanism = Quantity(
        type=bool,
        description='There is a filtering system for the bath?',
        a_eln={'component': 'BoolEditQuantity'},
    )

    # recycle_mechanism = Quantity(
    #     type=bool,
    #     description='There is a filtering system for the bath?',
    #     a_eln={'component': 'BoolEditQuantity'},
    # )

    solution_renewal = Quantity(
        type=str,
        description='Frequency of the renewal of the solution in the bath',
        a_eln={'component': 'StringEditQuantity'},
    )

    max_number_of_repetitions = Quantity(
        type=int,
        description='Maximum number of successive steps allowed for that well',
        a_eln={'component': 'NumberEditQuantity'},
    )

    max_time_of_usage = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )

    reactives = SubSection(section_def=WetSolutionComponents, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        if self.volume_of_solution is not None and self.reactives:
            super().normalize(archive, logger)
            water_from_token = 0
            for token in self.reactives:
                token.final_solution_concentration = (
                    token.initial_concentration
                    * token.dispensed_volume
                    / (self.volume_of_solution)
                )
                if 'water' in token.name.lower() or token.chemical_formula == 'H2O':
                    water_from_token += (
                        token.initial_concentration
                        * token.dispensed_volume
                        / self.volume_of_solution
                    )
                else:
                    water_from_token += (
                        (100 - token.initial_concentration)
                        * token.dispensed_volume
                        / (self.volume_of_solution)
                    )
            element = next(
                (
                    x
                    for x in self.reactives
                    if (x.chemical_formula == 'H2O' or 'water' in x.name.lower())
                ),
                None,
            )
            if element is not None:
                element.final_solution_concentration = water_from_token
            else:
                water_field = WetSolutionComponents()
                water_field.name = 'Deio water'
                water_field.chemical_formula = 'H2O'
                water_field.initial_concentration = 100
                volume_to_remove = 0
                concentration_to_remove = 0
                for token in self.reactives:
                    volume_to_remove += token.dispensed_volume
                    concentration_to_remove += token.final_solution_concentration
                water_field.dispensed_volume = (
                    self.volume_of_solution - volume_to_remove
                )
                water_field.final_solution_concentration = 100 - concentration_to_remove
                self.reactives.append(water_field)
                raise Exception("""
                    Assumed remaining volume to be water. New field in reactives now.
                    Control the water field and in case confirm renormalizing the enry.
                    """)


class Dump_Rinser(Equipment):
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
                    'max_overflow_time',
                    'resistivity_cut_off',
                    'notes',
                ]
            },
        }
    )

    # min_resistivity_cut_off = Quantity(
    #     type=np.float64,
    #     description='Minimum Value available as target to stop the process',
    #     a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'ohm*cm'},
    #     unit='ohm*cm',
    # )

    # max_resistivity_cut_off = Quantity(
    #     type=np.float64,
    #     description='Maximum value available as target to stop the process',
    #     a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'ohm*cm'},
    #     unit='ohm*cm',
    # )

    max_overflow_time = Quantity(
        type=np.float64,
        description='Maximum amount of flow at disposal',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )

    available_resistivity_setting = SubSection(
        section_def=ResistivityControlSystem, repeats=False
    )


class Wet_Bench(Instrument, EntryData, ArchiveSection):
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
                    'institution',
                    'product_model',
                    'manufacturer_name',
                    'inventary_code',
                    'notes',
                ]
            },
        }
    )

    lab_id = Quantity(
        type=str,
        description='ID assigned by lab for findability',
        a_eln={'component': 'StringEditQuantity', 'label': 'id'},
    )
    inventary_code = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
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

    notes = Quantity(
        type=str,
        a_eln={
            'component': 'RichTextEditQuantity',
        },
    )

    tanks = SubSection(section_def=Wet_Bench_Unit, repeats=True)
    dumping_rinsers = SubSection(section_def=Dump_Rinser, repeats=True)


#######################################################################################
################################ DEPOSITION EQUIPMENTS ################################
#######################################################################################


class LPCVD_System(Equipment):
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
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_chamber_temperature',
                    'max_chamber_temperature',
                    'notes',
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

    min_chamber_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature at disposal for the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chamber_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    gases = SubSection(
        section_def=Massflow_parameter,
        repeats=True,
    )

    allowed_carriers = SubSection(
        section_def=CarrierDescription,
        repeats=True,
    )


class PECVD_System(Equipment):
    m_def = Section(
        description='Class instrument for PECVD procedures',
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
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_chamebr_temperature',
                    'max_chamber_temperature',
                    'notes',
                ],
            },
        },
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

    min_chamber_temperature = Quantity(
        type=np.float64,
        description='Minimal temperature at disposal for the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    max_chamber_temperature = Quantity(
        type=np.float64,
        description='Maximal temperature of the wall',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    gases = SubSection(
        section_def=Massflow_parameter,
        repeats=True,
    )

    chuck = SubSection(
        section_def=ChuckCapabilities,
        repeats=False,
    )


class ICP_CVD_System(PECVD_System):
    m_def = Section(
        description='Class for instruments devoted to ICP_CVD procedures',
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
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'vacuum_system_name',
                    'min_chamber_temperature',
                    'max_chamber_temperature',
                    'notes',
                ],
            },
        },
    )

    icp_parameters = SubSection(section_def=ICP_ColumnCapabilities, repeats=False)


#######################################################################################
################################ LITHOGRAPHY EQUIPMENTS ###############################
#######################################################################################


class ElectronBeamLithographer(Equipment):
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
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'notes',
                ],
            },
        }
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

    beam_column_capabilities = SubSection(
        section_def=BeamColumnCapabilites, repeats=False
    )

    writing_capabilities = SubSection(section_def=WritingCapabilities, repeats=False)


class FocusedIonBeamLithographer(ElectronBeamLithographer):
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
                    'min_chamber_pressure',
                    'max_chamber_pressure',
                    'notes',
                ],
            },
        }
    )


# Devo migliorare il fib per cui capire la differenza vera con ebl non solo e o atomi
