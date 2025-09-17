from apps.directories import dir_path
from apps.menu_steps import (
    menutrans_annealing,
    menutrans_baking,
    menutrans_dicing,
    menutrans_doping,
    menutrans_ebl,
    menutrans_fib,
    menutrans_labelingcleaning,
    menutrans_ltodensification,
    menutrans_sod,
    menutrans_thermaloxidation,
    menutrans_track,
)
from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemCustomQuantities,
    SearchQuantities,
)

schemas = [
    f'*#{path_value}'
    for path_value in dir_path.values()
    if 'steps.transform' in path_value
]
fps = 'FabricationProcessStep'
dir0 = f'schema_packages.fabrication_utilities.{fps}'
schemas.append(f'*#{dir0}')

transapp = App(
    label='Transform steps',
    path='transapp',
    category='Fabrication utilities',
    description='App to search transform fabrication steps.',
    readme="""
    This app is intended to navigate around the ecosystem of clean room fabrication
    possible transform steps. At the beginning you will see all the fabrication
    steps available in nomad and than through the filters on the left you can
    specialize the research per single technique. Navigation across multiple technique
    is not allowed.
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
        Column(quantity=f'data.recipe_name#{dir0}'),
    ],
    filters_locked={'section_defs.definition_qualified_name': dir0},
    menu=Menu(
        items=[
            Menu(
                title='Dicing',
                items=[
                    menutrans_dicing,
                ],
            ),
            Menu(
                title='Doping',
                items=[
                    menutrans_doping,
                    menutrans_sod,
                ],
            ),
            Menu(
                title='Lithography',
                items=[
                    menutrans_ebl,
                    menutrans_fib,
                    menutrans_track,
                ],
            ),
            Menu(
                title='Thermal processing',
                items=[
                    menutrans_annealing,
                    menutrans_ltodensification,
                    menutrans_thermaloxidation,
                    menutrans_baking,
                ],
            ),
            Menu(
                title='Labeling',
                items=[
                    menutrans_labelingcleaning,
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
