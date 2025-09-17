from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import MEnum, Quantity, Section, SubSection
from schema_packages.utils import BeamSource, FabricationChemical

if TYPE_CHECKING:
    pass

#######################################################################################
############ Classes of gaseous chemicals reporting maximal values allowed ############
#######################################################################################


class Massflow_parameter(FabricationChemical):
    m_def = Section(
        description='Class to describe flux of gases in fluximeters',
        a_eln={'hide': ['lab_id', 'datetime']},
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


class DryerGasParameter(Massflow_parameter):
    m_def = Section(
        a_eln={'hide': ['lab_id', 'datetime']},
    )

    min_gas_temperature = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    max_gas_temperature = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )


#######################################################################################
############### Classes used to describe capabilities of some chambers ################
#######################################################################################


class Clamping_Capabilities(ArchiveSection):
    m_def = Section(
        description="""
        Class describing all parameters useful for clamping capabilites.
        """
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

    min_clamping_pressure = Quantity(
        type=np.float64,
        description='Minimum pressure needed on chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )
    max_clamping_pressure = Quantity(
        type=np.float64,
        description='Maximum pressure needed on chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )


class ChuckCapabilities(ArchiveSection):
    m_def = Section(
        description="""
        Section containing all parameters relative to the chuck.
        """
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

    clamping = SubSection(section_def=Clamping_Capabilities, repeats=False)


class ICP_ColumnCapabilities(ArchiveSection):
    m_def = Section(
        description="""
        Section used to describe available parameters  in the icp region
        """
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


class CarrierDescription(ArchiveSection):
    m_def = Section(
        description="""
        Section describing a component used to carry vertically one or more wafers
        """
    )

    slots = Quantity(
        type=int,
        description='Total number of possible positioning for wafers',
        a_eln={'component': 'NumberEditQuantity'},
    )


class SpinnerSpinParameters(ArchiveSection):
    m_def = Section()

    min_spin_frequency = Quantity(
        type=np.float64,
        description='Mnimum velocity of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'revolutions_per_minute',
        },
        unit='revolutions_per_minute',
    )

    max_spin_frequency = Quantity(
        type=np.float64,
        description='Maximal velocity of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'revolutions_per_minute',
        },
        unit='revolutions_per_minute',
    )
    max_spin_angular_acceleration = Quantity(
        type=np.float64,
        description='Maximal acceleration of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'revolutions_per_minute/sec',
        },
        unit='revolutions_per_minute/sec',
    )


#######################################################################################
########################## Classes for lithography equipment ##########################
#######################################################################################


class BeamColumnCapabilites(ArchiveSection):
    m_def = Section()

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
    min_current = Quantity(
        type=np.float64,
        description='Minimal current provided',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'pampere',
        },
        unit='pampere',
    )
    max_current = Quantity(
        type=np.float64,
        description='Maximal current provided',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'pampere',
        },
        unit='pampere',
    )

    beam_source_available = SubSection(section_def=BeamSource, repeats=False)


class WritingCapabilities(ArchiveSection):
    m_def = Section()

    min_area_dose = Quantity(
        type=np.float64,
        description='Minimal dose to use in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter^2',
        },
        unit='uC/centimeter^2',
    )

    max_area_dose = Quantity(
        type=np.float64,
        description='Maximal dose to use in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter^2',
        },
        unit='uC/centimeter^2',
    )
    min_line_dose = Quantity(
        type=np.float64,
        description='Minimal dose to use in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter',
        },
        unit='uC/centimeter',
    )

    max_line_dose = Quantity(
        type=np.float64,
        description='Maximal dose to use in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter',
        },
        unit='uC/centimeter',
    )
    min_dot_dose = Quantity(
        type=np.float64,
        description='Minimal dose to use in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC',
        },
        unit='uC',
    )

    max_dot_dose = Quantity(
        type=np.float64,
        description='Maximal dose to use in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC',
        },
        unit='uC',
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


#######################################################################################
########### Sections to describe wet modular components in fabrication labs ###########
#######################################################################################


class WetSolutionComponents(FabricationChemical):
    m_def = Section(
        definition='Chemicals for describe solutions used in wet fabrication unity',
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'chemical_formula',
                    'description',
                    'purity_level',
                    'initial_concentration',
                    'dispensed_volume',
                    'final_solution_concentration',
                ],
            },
        },
    )

    purity_level = Quantity(
        description='Purity level of the starting reactives by manufacturer',
        type=MEnum(
            'VLSI',
            'ULSI',
            'SLSI',
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )

    initial_concentration = Quantity(
        type=np.float64,
        description='Initial volume percentage of the reactives by manufacturer',
        a_eln={'component': 'NumberEditQuantity'},
    )

    dispensed_volume = Quantity(
        type=np.float64,
        description='Volume of reactive used to generate the final solution',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'liter'},
        unit='liter',
    )

    final_solution_concentration = Quantity(
        type=np.float64,
        description='Final volume percentage of the reactive in the solution',
        a_eln={'component': 'NumberEditQuantity'},
    )


class ResistivityControlSystem(ArchiveSection):
    m_def = Section(
        description="""
        Section used to describe the available option in setting a cut-off resistivity
        system control.
        """
    )

    min_resistivity_cut_off = Quantity(
        type=np.float64,
        description='Minimum Value available as target to stop the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'ohm*cm'},
        unit='ohm*cm',
    )

    max_resistivity_cut_off = Quantity(
        type=np.float64,
        description='Maximum value available as target to stop the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'ohm*cm'},
        unit='ohm*cm',
    )
