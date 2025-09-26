from apps.directories import dir_path
from apps.menu_steps import (
    menuadd_bonding,
    menuadd_coat,
    menuadd_electrongun,
    menuadd_icpcvd,
    menuadd_lpcvd,
    menuadd_pecvd,
    menuadd_sog,
    menuadd_spincoat,
    menuadd_sputtering,
)
from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemCustomQuantities,
    SearchQuantities,
)

schemas = [
    f'*#{path_value}' for path_value in dir_path.values() if 'steps.add' in path_value
]
fps = 'FabricationProcessStep'
dir0 = f'schema_packages.fabrication_utilities.{fps}'
schemas.append(f'*#{dir0}')

addapp = App(
    label='Add steps',
    path='addapp',
    category='Fabrication utilities',
    description='App to search add fabrication steps.',
    readme="""
    This app is intended to navigate around the ecosystem of clean room fabrication
    possible add steps. At the beginning you will see all the fabrication steps
    available in nomad and than through the filters on the left you can specialize
    the research per single technique. Navigation across multiple technique is not
    allowed.
    """,
    search_quantities=SearchQuantities(include=schemas),
    columns=[
        Column(quantity='entry_name', selected=True),
        Column(quantity='entry_type', selected=True),
        Column(
            quantity=f'data.affiliation#{dir0}',
            selected=True,
        ),
        Column(
            quantity=f'data.location#{dir0}',
            selected=True,
        ),
        Column(quantity='upload_create_time', selected=True),
        Column(quantity=f'data.step_id#{dir0}', selected=True),
        Column(quantity=f'data.recipe_name#{dir0}'),
    ],
    filters_locked={'section_defs.definition_qualified_name': dir0},
    menu=Menu(
        items=[
            Menu(
                title='Integration',
                items=[
                    menuadd_bonding,
                ],
            ),
            Menu(
                title='Synthesis',
                items=[
                    menuadd_lpcvd,
                    menuadd_pecvd,
                    menuadd_icpcvd,
                    menuadd_coat,
                    menuadd_spincoat,
                    menuadd_electrongun,
                    menuadd_sputtering,
                    menuadd_sog,
                ],
            ),
            Menu(
                title='User defined quantities',
                items=[
                    MenuItemCustomQuantities(
                        title='Costumer user quantities',
                        type='custom_quantities',
                    ),
                ],
            ),
        ],
    ),
)
