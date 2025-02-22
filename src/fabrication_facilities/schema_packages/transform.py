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
from nomad.datamodel.metainfo.basesections import ElementalComposition
from fabrication_facilities.schema_packages.fabrication_steps import (
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


class ElectronBeamLithography(FabricationProcessStep, ArchiveSection):
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
                    'deposition_rate_from_recipe',
                    'chamber_pressure',
                    'chuck_temperature',
                    'tension',
                    'currentalignment_required',
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
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um*um'},
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


class FocusedIonBeamLithography(FabricationProcessStep, ArchiveSection):
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
                    'deposition_rate_from_recipe',
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
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um*um'},
        unit='um*um',
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


class DevelopingStep(FabricationProcessStep, ArchiveSection):
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
                    'oxygen_percentage',
                    'oxygen_flow',
                    'temperature_final_measured',
                    'duration_effective',
                    'temperature_ramp_up_rate',
                    'temperature_ramp_down_rate',
                    'notes',
                ]
            },
        },
    )

    short_name = Quantity(
        type=str, a_eln={'component': 'StringEditQuantity', 'label': 'target material'}
    )
    recipe_name = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})
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
    oxigen_percentage = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    oxigen_flow = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    temperature_final_measured = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    duration_effective = Quantity(
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


m_package.__init_metainfo__()
