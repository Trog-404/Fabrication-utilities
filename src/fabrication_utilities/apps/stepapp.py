from apps.directories import dir_path
from apps.menu_steps import (
    menuutils_obsmeasurements,
    menuutils_startingmaterial,
)
from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    SearchQuantities,
)

schemas = [f'*#{path_value}' for path_value in dir_path.values()]
fps = 'FabricationProcessStep'
dir0 = f'schema_packages.fabrication_utilities.{fps}'
schemas.append(f'*#{dir0}')

stepapp = App(
    label='Fabrication steps (next deprecated)',
    path='stepapp',
    category='Fabrication facilities',
    description='App to search fabrication steps.',
    readme="""
    This app is intended to navigate around the ecosystem of clean room fabrication
    possible steps. At the beginning you can see all the fabrication steps available
    in nomad and than through the filters you can specialize the research per single
    technique. Navigation that consists in multiple technique is not allowed.
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
                title='Characterization steps',
                indentation=0,
                items=[
                    Menu(
                        title='Measurements',
                        items=[
                            menuutils_obsmeasurements,
                        ],
                    ),
                ],
            ),
            Menu(
                title='Starting material',
                items=[
                    menuutils_startingmaterial,
                ],
            ),
        ]
    ),
)
