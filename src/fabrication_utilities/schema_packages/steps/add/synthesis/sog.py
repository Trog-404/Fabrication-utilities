from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.metainfo import Package, Quantity, Section, SubSection
from schema_packages.fabrication_utilities import (
    FabricationProcessStep,
    FabricationProcessStepBase,
)
from schema_packages.steps.utils import SpinningComponent, SynthesisOutputs
from schema_packages.utils import FabricationChemical

if TYPE_CHECKING:
    pass

m_package = Package(name='Schema to describe sog steps')

# In futuro per essere conformi alla tassonomia e allo splitting dei passi nei propri
# componenti bisgnorebbe descrivere il de wetting con un baking e il precleaning con
# l'apposito passo.


class SOGbase(FabricationProcessStepBase):
    m_def = Section()

    pre_cleaning = Quantity(
        type=str,
        description='Name to understand what kind of precleaning perform',
        a_eln={
            'component': 'StringEditQuantity',
        },
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

    substrate_material = SubSection(section_def=FabricationChemical, repeats=False)

    spin_parameters = SubSection(section_def=SpinningComponent, repeats=False)


class SOG(FabricationProcessStep):
    m_def = Section(
        a_eln={
            'hide': [
                'tag',
                'duration',
            ],
            'properties': {
                'order': [
                    'name',
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
                    'step_id',
                    'definition_of_process_step',
                    'keywords',
                    'recipe_name',
                    'recipe_file',
                    'recipe_preview',
                    'thickness_target',
                    'notes',
                ]
            },
        },
    )

    thickness_target = Quantity(
        type=np.float64,
        description='Amount of material to be deposited',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )

    sog_steps = SubSection(section_def=SOGbase, repeats=True)

    outputs = SubSection(section_def=SynthesisOutputs, repeats=False)


m_package.__init_metainfo__()
