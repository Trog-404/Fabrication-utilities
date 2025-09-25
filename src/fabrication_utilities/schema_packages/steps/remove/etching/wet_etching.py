#######################################################################################
##################################### WET ETCHING #####################################
#######################################################################################

from typing import TYPE_CHECKING

import numpy as np
from nomad.metainfo import (
    Package,
    Quantity,
    Section,
    SubSection,
)
from schema_packages.fabrication_utilities import (
    FabricationProcessStep,
    FabricationProcessStepBase,
)
from schema_packages.steps.utils import (
    DeIonizedWaterDumping,
    ResistivityControl,
    WetEtchingOutputs,
    WetReactiveComponents,
)
from schema_packages.utils import FabricationChemical

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

m_package = Package(name='Wet etching steps shemas definitions for fabrication')


class WetEtchingbase(FabricationProcessStepBase):
    m_def = Section(
        description='Atomistic component of a wet etching or cleaning step',
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'tag',
                    'starting_date',
                    'ending_date',
                    'duration',
                    'pump',
                    'wetting',
                    'wetting_duration',
                    'tank_temperature',
                    'ultrasounds_required',
                    'ultrasounds_frequency',
                    'ultrasounds_duration',
                    'notes',
                ]
            },
        },
    )

    pump = Quantity(
        type=bool,
        description='During the process is the pump in action?',
        a_eln={'component': 'BoolEditQuantity'},
    )
    tank_temperature = Quantity(
        type=np.float64,
        description='Temperature set for the bath',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    wetting = Quantity(
        type=bool,
        description='Is a wetting needed before the etching?',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )
    wetting_duration = Quantity(
        type=np.float64,
        description='Duration of the wetting phase',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )
    ultrasounds_required = Quantity(
        type=bool,
        description="""
        The bath is equipped with an ultrasounds system to speed the process?
        """,
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )
    ultrasounds_frequency = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'MHz',
        },
        unit='MHz',
    )
    ultrasounds_duration = Quantity(
        type=np.float64,
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )

    resistivity_control = SubSection(
        section_def=ResistivityControl,
        description="""
        If the bath uses a resistivity control system it can be described here.
        """,
        repeats=False,
    )

    materials_etched = SubSection(
        section_def=FabricationChemical,
        description='Section to describe the material or the materials etched',
        repeats=True,
    )
    reactives_used_to_etch = SubSection(
        section_def=WetReactiveComponents,
        description="""
        Section to describe the reactives and their concentrations in the bath
        """,
        repeats=True,
    )

    cleaning_dumping = SubSection(
        section_def=DeIonizedWaterDumping,
        description='Section to describe dumping in water deio after the etching phase',
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class WetEtching(FabricationProcessStep):
    m_def = Section(
        description="""
        Wet etching is a material removal process that uses liquid chemicals or etchants
        to remove materials from a wafer. The specific patterns are defined by masks on
        the wafer. Materials that are not protected by the masks are etched away by
        liquid chemicals. A wet etching process involves multiple chemical reactions
        that consume the original reactants and produce new reactants. The wet etch
        process can be described by three basic steps. (1) Diffusion of the liquid
        etchant to the structure that is to be removed. (2) The reaction between the
        liquid etchant and the material being etched away. A reduction-oxidation (redox)
        reaction usually occurs. This reaction entails the oxidation of the material
        then dissolving the oxidized material. (3) Diffusion of the byproducts in the
        reaction from the reacted surface.
        """,
        a_eln={
            'hide': ['duration', 'tag'],
            'properties': {
                'order': [
                    'name',
                    'step_id',
                    'description',
                    'affiliation',
                    'location',
                    'institution',
                    'facility',
                    'laboratory',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'depth_target',
                    'duration_target',
                    'erching_rate_target',
                    'endpoint',
                    'notes',
                ]
            },
        },
    )

    depth_target = Quantity(
        type=np.float64,
        description='Amount of material to be etched',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    duration_target = Quantity(
        type=np.float64,
        description='Time prescribed by the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    etching_rate_target = Quantity(
        type=np.float64,
        description='Etching rate prescribed by the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm/minute'},
        unit='nm/minute',
    )
    endpoint = Quantity(
        type=bool,
        description="""
        The process uses a time or is performed with an endpoint for some parameters
        """,
        a_eln={'component': 'BoolEditQuantity'},
    )

    etching_steps = SubSection(
        section_def=WetEtchingbase,
        description="""
        Section to describe single or multiple activities performed in the step
        """,
        repeats=True,
    )

    outputs = SubSection(
        section_def=WetEtchingOutputs,
        description='Section containing some paremeters obtained as output of the step',
        repeats=False,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


class WetCleaning(FabricationProcessStep):
    m_def = Section(
        description="""
        Fabrication process step where an item is washed with a solution of wet
        reactives. It is ideally similar to the wet etching, so the atomistic step
        is a wet etching base but differently to that the objective of the
        procedure is not remove a material from a layer but eliminating the
        impurities of previous steps.
        """,
        a_eln={
            'hide': ['duration', 'tag'],
            'properties': {
                'order': [
                    'name',
                    'step_id',
                    'description',
                    'affiliation',
                    'location',
                    'institution',
                    'facility',
                    'laboratory',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'endpoint',
                    'notes',
                ]
            },
        },
    )

    endpoint = Quantity(
        type=bool,
        description="""
        The process uses a time or is performed with an endpoint for some parameters
        """,
        a_eln={'component': 'BoolEditQuantity'},
    )

    cleaning_steps = SubSection(
        section_def=WetEtchingbase,
        description="""
        Section to describe single or multiple activities performed in the step
        """,
        repeats=True,
    )

    outputs = SubSection(
        section_def=WetEtchingOutputs,
        description='Section containing some paremeters obtained as output of the step',
        repeats=False,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
