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
from schema_packages.fabrication_utilities import (
    FabricationProcessStep,
)
from schema_packages.utils import (
    parse_chemical_formula,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Transform processes schema')

#######################################################################################
# Da questo punto in poi le classi non sono ancora state riviste con lo schema adottato
# di unit steps come sottosezioni degli effettivi steps che contengono informazioni
# generali sul tipo di step steguito.
#######################################################################################
# RIVEDERLI E POI DEPRECARE QUESTO FILE IN MANIERA CHE SI SEGUA LA TASSONOMIA
#######################################################################################


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
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'densification_type',
                    'short_name',
                    'chemical_formula',
                    'temperature_target',
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
    temperature_target = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    gas_flow = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
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
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'doping_type',
                    'temperature_target',
                    'duration_target',
                    'surface_resistance_measured',
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
    temperature_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    duration_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    surface_resistance_measured = Quantity(
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
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'wafer_label_position',
                    'wafer_label_name',
                    'wafer_cleaning_DI_ultrasound_required',
                    'wafer_cleaning_rca_required',
                    'wafer_cleaning_piranha_required',
                    'wafer_cleaning_dipHF_required',
                    'wafer_cleaning_rinse_spin_dryer_required',
                    'notes',
                ]
            },
        },
    )
    wafer_label_position = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    wafer_label_name = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
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
    wafer_cleaning_rinse_spin_dryer_required = Quantity(
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
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
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
                    'spin_angular_acceleration',
                    'spin_duration',
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
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
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


class Track(Chemical, FabricationProcessStep, ArchiveSection):
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
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'mask_set_name',
                    'mask_name',
                    'hdms_required',
                    'short_name',
                    'chemical_formula',
                    'thickness_target',
                    'dewetting_duration',
                    'dewetting_temperature',
                    'mask_aligner_name',
                    'alignment_type',
                    'mask_target',
                    'exposure_mask_contact_type',
                    'exposure_intensity',
                    'exposure_duration',
                    'developing_duration',
                    'developing_rinse_spin_dryer_required',
                    'peb_required',
                    'peb_duration',
                    'peb_temperature',
                    'softbake_required',
                    'softbake_duration',
                    'softbake_temperature',
                    'hardbake_required',
                    'hardbake_duration',
                    'hardbake_temperature',
                    'notes',
                ]
            },
        },
    )
    mask_set_name = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    mask_name = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    short_name = Quantity(
        type=str,
        description='Material to be deposited',
        a_eln={'component': 'StringEditQuantity', 'label': 'resist name'},
    )
    chemical_formula = Quantity(
        type=str,
        description='Inserted only if known',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    thickness_target = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'label': 'Resist thickness',
            'defaultDisplayUnit': 'um',
        },
        unit='um',
    )
    dewetting_duration = Quantity(
        type=np.float64,
        description='The duration of the dewetting',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )
    dewetting_temperature = Quantity(
        type=np.float64,
        description='The temperaure of the dewetting',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    hdms_required = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    mask_aligner_name = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    alignment_type = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    mask_target = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    exposure_mask_contact_type = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    exposure_intensity = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mwatt/cm^2'},
        unit='mwatt/cm^2',
    )
    exposure_duration = Quantity(
        type=np.float64,
        description='The duration of the exposure',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )
    developing_duration = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )
    developing_rinse_spin_dryer_required = Quantity(
        type=MEnum('Yes', 'No', 'Other (see Note)'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    peb_required = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
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
    softbake_required = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    softbake_duration = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )
    softbake_temperature = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    hardbake_required = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    hardbake_duration = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )
    hardbake_temperature = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    resist_elemental_composition = SubSection(
        section_def=ElementalComposition, repeats=True
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        # if self.exposure_required:
        #     self.exposure_duration = Quantity(
        #         type=np.float64,
        #         description='The duration of the exposure',
        #         a_eln={
        #             'component': 'NumberEditQuantity',
        #             'defaultDisplayUnit': 'minute',
        #         },
        #         unit='minute',
        #     )
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
            self.resist_elemental_composition = elementality


m_package.__init_metainfo__()
