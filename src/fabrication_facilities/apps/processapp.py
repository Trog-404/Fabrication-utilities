from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemCustomQuantities,
    MenuItemTerms,
    SearchQuantities,
)

dir = 'fabrication_facilities.schema_packages.fabrication_steps.FabricationProcess'
dir1 = 'fabrication_facilities.schema_packages.add.ICP_CVD'
processapp = App(
    label='Processes',
    path='processesapp',
    category='Fabrication facilities',
    description='App to search fabrication processes.',
    readme=' The findability reach the level of the step.',
    search_quantities=SearchQuantities(include=[f'*#{dir}', f'*#{dir1}']),
    columns=[
        Column(quantity='entry_name', selected=True),
        Column(quantity='entry_type', selected=True),
        Column(
            quantity=f'data.affiliation#{dir}',
            selected=True,
        ),
        Column(quantity='upload_create_time', selected=True),
    ],
    filters_locked={'section_defs.definition_qualified_name': dir},
    menu=Menu(
        items=[
            Menu(
                title='Infrastrucure',
                indentation=0,
                items=[
                    MenuItemTerms(
                        title='Affiliation',
                        type='terms',
                        search_quantity=f'data.affiliation#{dir}',
                    ),
                    MenuItemTerms(
                        title='ID proposal',
                        type='terms',
                        search_quantity=f'data.id_proposal#{dir}',
                    ),
                    MenuItemTerms(
                        title='Product Type',
                        type='terms',
                        search_quantity=f'data.generic_product_name#{dir}',
                    ),
                    MenuItemTerms(
                        title='ID item processed',
                        type='terms',
                        search_quantity=f'data.id_item_processed#{dir}',
                    ),
                ],
            ),
            Menu(
                title='synthesis',
                items=[
                    Menu(
                        title='Filters for ICP_CVD processes',
                        items=[
                            MenuItemTerms(
                                title='formula',
                                type='terms',
                                search_quantity=f"data.steps['section_defs.definition_qualified_name': dir1].chemical_formula#{dir}",
                            )
                        ],
                    )
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
