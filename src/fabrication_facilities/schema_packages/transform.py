from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import (
    ArchiveSection,
)
from nomad.datamodel.metainfo.basesections import ElementalComposition
from nomad.datamodel.metainfo.eln import Chemical
from nomad.metainfo import (
    MEnum,
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.fabrication_utilities import (
    FabricationProcessStep,
)
from fabrication_facilities.schema_packages.utils import (
    parse_chemical_formula,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Add processes schema')


class EBL(FabricationProcessStep, ArchiveSection):
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
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'dose',
                    'writing_field_dimension',
                    'address_size',
                    'clock',
                    'chamber_pressure',
                    'chuck_temperature',
                    'tension',
                    'current',
                    'alignment_required',
                    'alignment_max_error',
                    'notes',
                ]
            },
        },
    )
    recipe_name = Quantity(
        type=str,
        description='Name of the file that contains the geometry to impress',
        a_eln={
            'label': 'file CAD name',
            'component': 'StringEditQuantity',
        },
    )
    dose = Quantity(
        type=np.float64,
        description='Dose used in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter^2',
        },
        unit='uC/centimeter^2',
    )
    writing_field_dimension = Quantity(
        type=np.float64,
        description='Area covered globally in the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um^2'},
        unit='um^2',
    )
    address_size = Quantity(
        type=np.float64,
        description='The minimum distance covered per step in the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    clock = Quantity(
        type=np.float64,
        description='Frequency used',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'MHz'},
        unit='MHz',
    )
    current = Quantity(
        type=np.float64,
        description='Current provided',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'pampere'},
        unit='pampere',
    )
    chamber_pressure = Quantity(
        type=np.float64,
        description='Pressure in the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )
    tension = Quantity(
        type=np.float64,
        description='Voltage accelerating the electrons',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'volt'},
        unit='volt',
    )
    alignment_required = Quantity(
        type=bool,
        description='Amount of material deposited as described in the recipe',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )
    alignment_max_error = Quantity(
        type=np.float64,
        description='Maximum error allowed in the alignment',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um'},
        unit='um',
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


class FIB(FabricationProcessStep, ArchiveSection):
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
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'dose',
                    'writing_field_dimension',
                    'address_size',
                    'clock',
                    'chamber_pressure',
                    'chuck_temperature',
                    'tension',
                    'current',
                    'alignment_required',
                    'alignment_max_error',
                    'number_of_loops',
                    'notes',
                ]
            },
        },
    )
    recipe_name = Quantity(
        type=str,
        description='Name of the file that contains the geometry to impress',
        a_eln={
            'label': 'file CAD name',
            'component': 'StringEditQuantity',
        },
    )
    dose = Quantity(
        type=np.float64,
        description='Dose used in the process',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'uC/centimeter^2',
        },
        unit='uC/centimeter^2',
    )
    writing_field_dimension = Quantity(
        type=np.float64,
        description='Area covered globally in the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um^2'},
        unit='um^2',
    )
    address_size = Quantity(
        type=np.float64,
        description='The minimum distance covered per step in the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    clock = Quantity(
        type=np.float64,
        description='Frequency used',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'MHz'},
        unit='MHz',
    )
    current = Quantity(
        type=np.float64,
        description='Current provided',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'pampere'},
        unit='pampere',
    )
    chamber_pressure = Quantity(
        type=np.float64,
        description='Pressure in the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )
    tension = Quantity(
        type=np.float64,
        description='Voltage accelerating the electrons',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'volt'},
        unit='volt',
    )
    alignment_required = Quantity(
        type=bool,
        description='Amount of material deposited as described in the recipe',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )
    alignment_max_error = Quantity(
        type=np.float64,
        description='Maximum error allowed in the alignment',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    number_of_loops = Quantity(
        type=int,
        description='Iteration of the process',
        a_eln={'component': 'NumberEditQuantity'},
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


class ResistDevelopment(FabricationProcessStep, ArchiveSection):
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
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'developing_solution',
                    'developing_solution_proportions',
                    'developing_duration',
                    'developing_temperature',
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
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    developing_solution_proportions = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    developing_duration = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    developing_temperature = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    cleaning_solution = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    cleaning_solution_proportions = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    cleaning_duration = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
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


class Annealing(Chemical, FabricationProcessStep, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'short_name',
                    'chemical_formula',
                    'temperature_start',
                    'temperature_final_target',
                    'gas_namegas_percentage',
                    'gas_flow',
                    'temperature_final_measured',
                    'duration_measured',
                    'temperature_ramp_up_rate',
                    'temperature_ramp_down_rate',
                    'notes',
                ]
            },
        },
    )

    short_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity', 'label': 'target/annealed material'},
    )
    temperature_start = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    temperature_final_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    gas_name = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    gas_percentage = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    gas_flow = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    temperature_final_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    duration_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    temperature_ramp_up_rate = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius/minunte',
        },
        unit='celsius/minute',
    )
    temperature_ramp_down_rate = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius/minunte',
        },
        unit='celsius/minute',
    )

    material_elemental_composition = SubSection(
        section_def=ElementalComposition, repeats=True
    )

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
            self.material_elemental_composition = elementality


class LTODensification(Chemical, FabricationProcessStep, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'densification_type',
                    'short_name',
                    'chemical_formula',
                    'densification_temperature',
                    'duration_measured',
                    'gas_flow',
                    'notes',
                ]
            },
        },
    )

    densification_type = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    short_name = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'densification gas',
        },
    )
    densification_temperature = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    gas_flow = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    duration_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    gas_elemental_composition = SubSection(
        section_def=ElementalComposition, repeats=True
    )

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
            self.gas_elemental_composition = elementality


class ThermalOxidation(Chemical, FabricationProcessStep, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'oxidation_type',
                    'short_name',
                    'chemical_formula',
                    'temperature_final_target',
                    'thickness_target',
                    'duration_measured',
                    'thickness_measured',
                    'gas_flow',
                    'notes',
                ]
            },
        },
    )

    oxidation_type = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    short_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity', 'label': 'thermal oxidation gas'},
    )
    thermal_oxidation_gas = Quantity(
        type=str, a_eln={'component': 'StringEditQuantity', 'label': 'target material'}
    )
    temperature_final_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    thickness_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    thickness_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    duration_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 's'},
        unit='s',
    )

    gas_elemental_composition = SubSection(
        section_def=ElementalComposition, repeats=True
    )

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
            self.gas_elemental_composition = elementality


class Dicing(FabricationProcessStep, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'blade_name',
                    'depth_target',
                    'protective_film_required',
                    'file_name',
                    'spindle_frequency',
                    'dicing_feed_rate',
                    'depth_step_1',
                    'depth_step_2',
                    'depth_step_3',
                    'dicing_edge_chipping_measured',
                    'notes',
                ]
            },
        },
    )
    dicing_blade_name = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    depth_target = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um',
        },
        unit='um',
    )
    protective_film_required = Quantity(
        type=bool,
        a_eln={
            'label': 'Protective film',
            'component': 'BoolEditQuantity',
        },
    )
    file_name = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    spindle_frequency = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'rpm',
        },
        unit='rpm',
    )
    dicing_feed_rate = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mm/s',
        },
        unit='mm/s',
    )
    depth_step_1 = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um',
        },
        unit='um',
    )
    depth_step_2 = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um',
        },
        unit='um',
    )
    depth_step_3 = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um',
        },
        unit='um',
    )
    dicing_edge_chipping_measured = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'um',
        },
        unit='um',
    )


class Doping(FabricationProcessStep, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'doping_type',
                    'doping_temperature',
                    'doping_duration',
                    'doping_surfaceresistance_measured',
                    'notes',
                ]
            },
        },
    )
    doping_type = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    doping_temperature = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    doping_duration = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    doping_surfaceresistance_measured = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'ohm',
        },
        unit='ohm',
    )


class LabelingCleaning(FabricationProcessStep, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'wafer_label_position',
                    'wafer_label_name',
                    'wafer_cleaning_DI_ultrasound_required',
                    'wafer_cleaning_rca_required',
                    'wafer_cleaning_piranha_required',
                    'wafer_cleaning_dipHF_required',
                    'wafer_cleaning_rinse_spin__driyer_required',
                    'notes',
                ]
            },
        },
    )
    wafer_label_position = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    wafer_label_name = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    wafer_cleaning_DI_ultrasound_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    wafer_cleaning_rca_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    wafer_cleaning_piranha_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    wafer_cleaning_dipHF_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    wafer_cleaning_rinse_spin__driyer_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )


class SOD(Chemical, FabricationProcessStep, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'short_name',
                    'chemical_formula',
                    'spin_dispensed_volume',
                    'dipping_HFsolution_proportions',
                    'spin_dipHF_duration',
                    'water_rinse_required',
                    'spin_dryer_required',
                    'peb_duration',
                    'peb_temperature',
                    'spin_frequency',
                    'notes',
                ]
            },
        },
    )
    short_name = Quantity(
        type=str,
        description='dopant solution',
        a_eln={'component': 'StringEditQuantity', 'label': 'dopant solution'},
    )
    dipping_HFsolution_proportions = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    spin_dipHF_duration = Quantity(
        type=int,
        a_eln={
            'component': 'NumberEditQuantity',
        },
    )
    water_rinse_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    spin_dryer_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    peb_duration = Quantity(
        type=np.float64,
        description='The duration of the peb',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )
    peb_temperature = Quantity(
        type=np.float64,
        description='The temperature of the peb',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    spin_dispensed_volume = Quantity(
        type=np.float64,
        description='Solution dispensed',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'milliliter',
        },
        unit='milliliter',
    )
    spin_frequency = Quantity(
        type=np.float64,
        description='Velocity of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'revolutions_per_minute',
        },
        unit='revolutions_per_minute',
    )
    doping_material_elemental_composition = SubSection(
        section_def=ElementalComposition, repeats=True
    )

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
            self.doping_material_elemental_composition = elementality


m_package.__init_metainfo__()
