from apps.directories import dir_path
from apps.menu_steps import (
    menuremove_driebosch,
    menuremove_icprie,
    menuremove_resistdev,
    menuremove_rie,
    menuremove_rinsingdrying,
    menuremove_spinresist,
    menuremove_stripping,
    menuremove_wetclean,
    menuremove_wetetching,
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
    if 'steps.remove' in path_value
]
fps = 'FabricationProcessStep'
dir0 = f'schema_packages.fabrication_utilities.{fps}'
schemas.append(f'*#{dir0}')

removeapp = App(
    label='Remove steps',
    path='removeapp',
    category='Fabrication utilities',
    description='App to search remove fabrication steps.',
    readme="""
    This app is intended to navigate around the ecosystem of clean room fabrication
    possible remove steps. At the beginning you will see all the fabrication steps
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
        Column(quantity=f'data.recipe_name#{dir0}'),
    ],
    filters_locked={'section_defs.definition_qualified_name': dir0},
    menu=Menu(
        items=[
            Menu(
                title='Etching',
                items=[
                    menuremove_rie,
                    menuremove_icprie,
                    menuremove_driebosch,
                    menuremove_wetetching,
                    menuremove_wetclean,
                    menuremove_stripping,
                ],
            ),
            Menu(
                title='Drying',
                items=[menuremove_rinsingdrying],
            ),
            Menu(
                title='Resist development',
                items=[menuremove_resistdev, menuremove_spinresist],
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
