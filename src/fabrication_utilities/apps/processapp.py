from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemCustomQuantities,
    MenuItemTerms,
    SearchQuantities,
)

dir0 = 'schema_packages.fabrication_utilities.FabricationProcess'
dir1 = 'schema_packages.materials.MaterialProductionProcess'

processapp = App(
    label='Processes',
    path='processesapp',
    category='Fabrication utilities',
    description='App to search fabrication processes.',
    readme="""
    This research app allows to search general information about fabrication processes.
    You can search products, affiliation of the project and the item processed
    """,
    search_quantities=SearchQuantities(include=[f'*#{dir0}', f'*#{dir1}']),
    columns=[
        Column(quantity='entry_name', selected=True),
        Column(quantity='entry_type'),
        Column(
            quantity=f'data.affiliation#{dir0}',
            selected=True,
        ),
        Column(
            quantity=f'data.id_proposal#{dir0}',
            selected=True,
        ),
        Column(
            quantity=f'data.generic_product_name#{dir0}',
            selected=True,
        ),
        Column(
            quantity=f'data.id_item_processed#{dir0}',
            selected=True,
        ),
        Column(quantity='upload_create_time', selected=True),
    ],
    filters_locked={'section_defs.definition_qualified_name': dir0},
    menu=Menu(
        items=[
            MenuItemTerms(
                title='Affiliation',
                type='terms',
                search_quantity=f'data.affiliation#{dir0}',
            ),
            MenuItemTerms(
                title='ID proposal',
                type='terms',
                search_quantity=f'data.id_proposal#{dir0}',
            ),
            MenuItemTerms(
                title='Product Type',
                type='terms',
                search_quantity=f'data.generic_product_name#{dir0}',
            ),
            MenuItemTerms(
                title='Author',
                type='terms',
                search_quantity=f'data.author#{dir0}',
            ),
            Menu(title='Materials produced'),
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
