#######################################################################################
# In questo file inserisco tutte le funzionalità e le sezioni che mi saranno utili per#
#  la descrizione degli steps istanze particolari di ogni superclasse. Ad esempio qui #
#   definirò la sezione contenente tutti i parametri relativi a una colonna ICP utile #
#                 sia per alcuni processi RIE e alcnui processi CVD.                  #
#######################################################################################

from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import MEnum, Quantity, Section, SubSection
from schema_packages.Items import ItemPlacement
from schema_packages.utils import (
    BeamSource,
    FabricationChemical,
    TimeRampMassflow,
    TimeRampPressure,
    TimeRampRotation,
    TimeRampTemperature,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

#######################################################################################
### Currently only one class is included to describe carriers for multiwafers steps ###
#######################################################################################


class Carrier(ArchiveSection):
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

    position_of_item = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
        description="""
        Number of the slot where the item is located. 1 is the the first
        slot which enter in the process chamber.
        """,
    )

    position_of_dummy_wafers = Quantity(
        type=int,
        shape=['*'],
        a_eln={'component': 'NumberEditQuantity'},
        description="""
        Dummy wafers are used to reach uniformity in the chamber. If the
        step do not require dummy wafers or they are not important this field could be
        void.
        """,
    )


#######################################################################################
## Classes used to describe components, mostrly electrical related in add and remove ##
#######################################################################################


class ICP_Column(ArchiveSection):
    m_def = Section(
        description="""
        Section used to describe component to obtain the inductively coupled plasma
        """
    )

    icp_power = Quantity(
        type=np.float64,
        description='Power erogated in the region of the plasma',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )
    icp_frequency = Quantity(
        type=np.float64,
        description='Frequency of current on the gases area',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )


class Clamping_System(ArchiveSection):
    m_def = Section(
        description="""
        Class describing all parameters useful for clamping, if used during the step.
        """
    )

    clamping_type = Quantity(
        type=MEnum(
            [
                'None',
                'Mechanical',
                'Electrostatic',
            ]
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )

    clamping_pressure = Quantity(
        type=np.float64,
        description='Adhesion pressure generated on the chuck',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    pressure_ramps = SubSection(
        section_def=TimeRampPressure,
        repeats=True,
    )


class Chuck(ArchiveSection):
    m_def = Section(
        description="""
        Section containing all parameters relative to the chuck.
        """
    )

    chuck_temperature = Quantity(
        type=np.float64,
        description='Temperature imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    chuck_power = Quantity(
        type=np.float64,
        description='Power erogated on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'W'},
        unit='W',
    )

    chuck_high_frequency = Quantity(
        type=np.float64,
        description='High frequency impulse imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'MHz'},
        unit='MHz',
    )

    chuck_low_frequency = Quantity(
        type=np.float64,
        description='Low frequency impulse imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'MHz'},
        unit='MHz',
    )

    bias = Quantity(
        type=np.float64,
        description='Voltage imposed on the sample by electrodes',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )

    temperature_ramps = SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    clamping = SubSection(section_def=Clamping_System, repeats=False)

    item_placement = SubSection(
        section_def=ItemPlacement,
        description="""If the placement of the item could be crucial for the outputs, 
        it can be roughly described here
        """,
        repeats=False,
    )


class DRIE_Chuck(ArchiveSection):
    m_def = Section(
        description="""
        Section containing all parameters relative to the chuck in a DRIE process. The
        main property is the existence of an alternate powering for electrical data,
        so also the duration of each phase is reported.
        """
    )

    chuck_temperature = Quantity(
        type=np.float64,
        description='Temperature imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    high_chuck_power = Quantity(
        type=np.float64,
        description='Power erogated on the chuck in the high phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    low_chuck_power = Quantity(
        type=np.float64,
        description='Power erogated on the chuck in the low phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'watt',
        },
        unit='watt',
    )

    high_chuck_power_duration = Quantity(
        type=np.float64,
        description='Power erogated on the chuck in the high phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )

    low_chuck_power_duration = Quantity(
        type=np.float64,
        description='Duration of the low phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )

    chuck_high_frequency = Quantity(
        type=np.float64,
        description='High frequency impulse imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'MHz'},
        unit='MHz',
    )

    chuck_low_frequency = Quantity(
        type=np.float64,
        description='Low frequency impulse imposed on the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'MHz'},
        unit='MHz',
    )

    bias = Quantity(
        type=np.float64,
        description='Voltage imposed on the sample by electrodes',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )

    temperature_ramps = SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    clamping = SubSection(section_def=Clamping_System, repeats=False)

    item_placement = SubSection(
        section_def=ItemPlacement,
        repeats=False,
    )


#######################################################################################
############ Classes used to describe gases flux components and parameters ############
#######################################################################################


class Massflow_controller(FabricationChemical):
    m_def = Section(
        a_eln={'overview': True, 'hide': ['lab_id', 'datetime']},
    )
    massflow = Quantity(
        type=np.float64,
        description='Rate at which the gas flows',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )

    gaseous_massflow_ramps = SubSection(
        section_def=TimeRampMassflow,
        repeats=True,
    )


class DRIE_Massflow_controller(Massflow_controller):
    m_def = Section(
        a_eln={'overview': True, 'hide': ['lab_id', 'datetime', 'massflow']},
    )

    priority = Quantity(
        type=str,
        description='Parameter describing the ordering in the chemical reactivity',
        a_eln={'component': 'StringEditQuantity'},
    )

    inactive_state_massflow = Quantity(
        type=np.float64,
        description='Rate at which the gas flows in the inactive phase of DRIE',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )

    active_state_massflow = Quantity(
        type=np.float64,
        description='Rate at which the gas flows in the inactive phase of DRIE',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )

    pulse_time = Quantity(
        type=np.float64,
        description='Atomistic time of activity for the gas',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )


#######################################################################################
####################### Utils for wet fabrication steps ###############################
#######################################################################################


class WetReactiveComponents(FabricationChemical):
    m_def = Section(
        definition='Chemicals for wet fabrication steps',
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
                    'solution_concentration',
                ],
            },
        },
    )

    solution_concentration = Quantity(
        type=np.float64,
        description='Volume percentage of the reactive in the solution',
        a_eln={'component': 'NumberEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class DevelopingSolution(ArchiveSection):
    m_def = Section()

    dispensed_volume = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'milliliter'},
        unit='milliliter',
    )

    developing_solution_components = SubSection(
        section_def=WetReactiveComponents,
        repeats=True,
    )

    surfactants = SubSection(section_def=WetReactiveComponents, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class ResistivityControl(ArchiveSection):
    m_def = Section(
        description='Section used in case of resistivity feedbacks',
    )

    resistivity_target = Quantity(
        type=np.float64,
        description='Value used as target to stop the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'ohm*cm'},
        unit='ohm*cm',
    )


#######################################################################################
# Resist coating utils and SpinningComponent the most widely used also in other utils #
#######################################################################################


class ResistDescription(FabricationChemical):
    m_def = Section(
        a_eln={
            'hide': ['datetime', 'lab_id'],
            'properties': {
                'order': ['name', 'chemical_formula', 'resist_type', 'description']
            },
        }
    )

    resist_type = Quantity(
        type=MEnum(
            'positive',
            'negative',
            'lift_off',
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )


class SpinningComponent(ArchiveSection):
    m_def = Section()

    spin_frequency = Quantity(
        type=np.float64,
        description='Velocity of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'revolutions_per_minute',
        },
        unit='revolutions_per_minute',
    )
    spin_angular_acceleration = Quantity(
        type=np.float64,
        description='Acceleration of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'revolutions_per_minute/sec',
        },
        unit='revolutions_per_minute/sec',
    )
    spin_duration = Quantity(
        type=np.float64,
        description='Acceleration of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )

    rotation_ramp = SubSection(
        section_def=TimeRampRotation,
        description='If a ramp to rotation can be setted describe it here',
        repeats=False,
    )


class Priming(ArchiveSection):
    m_def = Section()

    primer_name = Quantity(
        type=str,
        description='Name of the primer used, e.g. hmds',
        a_eln={'component': 'StringEditQuantity'},
    )
    primer_physical_phase = Quantity(
        type=MEnum(
            'gas',
            'liquid',
        ),
        description='Form of the primer used tipically liquid or gaseous',
        a_eln={'component': 'EnumEditQuantity'},
    )
    primer_temperature = Quantity(
        type=np.float64,
        description='Temperature of the primer',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    priming_duration = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    final_cooling_tempereature = Quantity(
        type=np.float64,
        description="""
        Due to the typical high temperature of the primer, item could be cooled at the 
        end of the process
        """,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    final_cooling_duration = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )


#######################################################################################
################################ Direct writing utilities #############################
#######################################################################################


class BeamColumn(ArchiveSection):
    m_def = Section()

    tension = Quantity(
        type=np.float64,
        description='Voltage accelerating the electrons',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'kV',
        },
        unit='kV',
    )

    current_target = Quantity(
        type=np.float64,
        description='Current provided',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'pampere',
        },
        unit='pampere',
    )

    beam_source = SubSection(section_def=BeamSource, repeats=False)


class Alignment(ArchiveSection):
    m_def = Section()

    alignment_mode = Quantity(
        type=MEnum(
            'No alignment',
            'Manual',
            'Auto',
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    alignment_max_error = Quantity(
        type=np.float64,
        description='Maximum error allowed in the alignment',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )


class WritingParameters(ArchiveSection):
    m_def = Section()

    area_dose = Quantity(
        type=np.float64,
        description='Dose per area used in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter^2',
        },
        unit='uC/centimeter^2',
    )
    line_dose = Quantity(
        type=np.float64,
        description='Dose per length used in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter',
        },
        unit='pC/centimeter',
    )
    dot_dose = Quantity(
        type=np.float64,
        description='Dose used in the process for single points',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'pC',
        },
        unit='pC',
    )
    writing_field_dimension = Quantity(
        type=np.float64,
        description='Area covered globally in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um^2',
        },
        unit='um^2',
    )
    address_size = Quantity(
        type=np.float64,
        description='The minimum distance covered per step in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm',
        },
        unit='nm',
    )
    settling_time = Quantity(
        type=np.float64,
        description='Time occurred to align the beam at the end of the writing field',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'us',
        },
        unit='us',
    )
    # clock = Quantity(
    #     type=np.float64,
    #     description='Frequency used',
    #     a_eln={
    #         'component': 'NumberEditQuantity',
    #         'defaultDisplayUnit': 'MHz',
    #     },
    #     unit='MHz',
    # )


#######################################################################################
############################# Rinsing and dryer utilities #############################
#######################################################################################


class Rinsingbase(ArchiveSection):
    m_def = Section(
        description="""
        With ringing is intended an ancillary polishing step tipically used to stop
        undesired reactions with a bath or lesser quantities of a reactive to wash away
        impurities or residuals too.
        """
    )

    rinsing_cycles = Quantity(
        type=int,
        description='Number of repetitions of the rinsing procedure',
        a_eln={'component': 'NumberEditQuantity'},
    )
    rinsing_mode = Quantity(
        type=MEnum('Auto', 'Manual'),
        description="""
        Field to describe if the rinsing is performed manually or automatically
        """,
        a_eln={'component': 'EnumEditQuantity'},
    )
    rinser_name = Quantity(
        type=str,
        description='Name of the substance used to rinse the item',
        a_eln={'component': 'StringEditQuantity'},
    )
    rinsing_duration = Quantity(
        type=np.float64,
        description='Duration of the apllied rinsing substance',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    draining_duration = Quantity(
        type=np.float64,
        description='Time of draining of residual rinser in the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )

    resistivity_control = SubSection(
        section_def=ResistivityControl,
        description='If the rinsing has a resistivity cut-off can be inserted here',
        repeats=False,
    )


class SpinRinsingbase(Rinsingbase):
    m_def = Section(
        description="""
        Rinsing phase imporvede by a rotation of the item to remove the excess of water.
        It should be also help the successive drying phase if expected.
        """,
    )
    spinning_parameters = SubSection(section_def=SpinningComponent, repeats=False)


class DeIonizedWaterDumping(ArchiveSection):
    m_def = Section(
        description="""
        Phase of rinsing, tipically used to stop undesired reactions with a bath in de -
        ionized water to wash away impurities or residuals.
        """
    )

    dumping_cycles = Quantity(
        type=int,
        description='Number of repetitions of the dumping procedure',
        a_eln={'component': 'NumberEditQuantity'},
    )
    dumping_mode = Quantity(
        type=MEnum('Auto', 'Manual'),
        description="""
        Field to describe if the dumping is performed manually or automatically
        """,
        a_eln={'component': 'EnumEditQuantity'},
    )
    dumper_name = Quantity(
        type=str,
        description='Name of the species used to dump items, by default deio water',
        a_eln={'component': 'StringEditQuantity'},
        default='De ionized water',
    )
    dumping_duration = Quantity(
        type=np.float64,
        description='Duration for each cycle',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )
    draining_duration = Quantity(
        type=np.float64,
        description='Time needed setted to eliminate water by the bath',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class DryerGas(Massflow_controller):
    m_def = Section(
        description='Section to use to describe an hot gas used to dry an item',
        a_eln={'hide': ['lab_id', 'datetime']},
    )

    gas_temperature = Quantity(
        type=np.float64,
        description='Temperature of the gas used to dry',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )


class Dryingbase(ArchiveSection):
    m_def = Section(
        description="""
        Section useful to describe repeatable entries where both or single direct wafer
        drying or gas assisted drying could be used
        """
    )

    drying_mode = Quantity(
        type=MEnum('Auto', 'Manual'),
        description='How is the drying performed?',
        a_eln={'component': 'EnumEditQuantity'},
    )

    drying_temperature = Quantity(
        type=np.float64,
        description='Temperature to dry directly on the carrier or chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    drying_duration = Quantity(
        type=np.float64,
        description='Time used in the drying phase',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )

    drying_gas = SubSection(
        section_def=DryerGas,
        description='If the drying is enanched by an hot gas can be described here',
        repeats=False,
    )


class SpinDryingbase(Dryingbase):
    m_def = Section(
        description="""
        Section describing a drying step where a spinning component is used to remove
        residuals
        """,
    )

    spinning_parameters = SubSection(section_def=SpinningComponent, repeats=False)


################################### OUTPUT SECTIONS ###################################


class BaseOutputs(ArchiveSection):
    m_def = Section(description='Section for simple steps that return only a job id')

    job_number = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )


class SynthesisOutputs(ArchiveSection):
    m_def = Section(
        description='Class describing all possible output data in synthesis steps',
    )

    job_number = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )

    duration_measured = Quantity(
        type=np.float64,
        description='Real time employed',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )

    control_parameter_profile = SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class EtchingOutputs(ArchiveSection):
    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'job_number',
                    'duration_measured',
                ],
            }
        },
        description='Set of parameters obtained in a dry etching process',
    )

    job_number = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )

    duration_measured = Quantity(
        type=np.float64,
        description='Real time of the process ad output',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )

    control_parameter_profile = SubSection(
        section_def=TimeRampTemperature,
        repeats=True,
    )


class WetEtchingOutputs(ArchiveSection):
    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'job_number',
                    'duration_measured',
                    'bath_number',
                ],
            }
        },
        description='Set of parameters obtained in a wet process',
    )

    job_number = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )

    duration_measured = Quantity(
        type=np.float64,
        description='Real time of the process ad output',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )

    bath_number = Quantity(
        type=int,
        description='Chronological number from the last solution renewal',
        a_eln={'component': 'NumberEditQuantity'},
    )


class BondingOutputs(ArchiveSection):
    m_def = Section()

    job_number = Quantity(
        type=int,
        description='Progressive number associated to the process',
        a_eln={'component': 'NumberEditQuantity'},
    )

    wafer_bonded_name = Quantity(
        type=str,
        description='Name of the bonded item',
        a_eln={'component': 'StringEditQuantity'},
    )

    wafer_bonded_id = Quantity(
        type=str,
        description='Id of the bonded item',
        a_eln={'component': 'StringEditQuantity'},
    )


class DicingOutputs(ArchiveSection):
    m_def = Section()

    job_number = Quantity(
        type=int,
        description='Progressive number associated to the process',
        a_eln={'component': 'NumberEditQuantity'},
    )

    wafer_dice_name = Quantity(
        type=str,
        shape=['*'],
        description='Name of the diced item',
        a_eln={'component': 'StringEditQuantity'},
    )

    wafer_diced_id = Quantity(
        type=str,
        shape=['*'],
        description='Name of the diced item',
        a_eln={'component': 'StringEditQuantity'},
    )


class ElectronGunOutputs(SynthesisOutputs):
    m_def = Section()

    gun_voltage_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'V'},
        unit='V',
    )

    gun_current_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mampere'},
        unit='mampere',
    )


class OxidationOutputs(ArchiveSection):
    m_def = Section()

    job_number = Quantity(type=int, a_eln={'component': 'NumberEditQuantity'})

    duration_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 's'},
        unit='s',
    )


class DirectLitoOutputs(ArchiveSection):
    m_def = Section()

    job_number = Quantity(type=int, a_eln={'component': 'NumberEditQuantity'})

    current_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'pC'},
        unit='pC',
    )

    duration_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )

    # angular_intensity = Quantity(
    #     type=np.float64,
    #     a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mampere/sr'},
    #     unit='mampere/sr',
    # )
