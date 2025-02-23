from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemCustomQuantities,
    MenuItemPeriodicTable,
    MenuItemTerms,
    SearchQuantities,
)

dir = 'fabrication_facilities.schema_packages.fabrication_steps.FabricationProcess'
step = 'data.steps.step_type'
ec = 'data.steps.fluximeters.elemental_composition.element'
mec = 'data.steps.material_elemental_composition.element'
flux = 'data.steps.fluximeters'
processapp = App(
    label='Processes',
    path='processesapp',
    category='Fabrication facilities',
    description='App to search fabrication processes.',
    readme=' The findability reach the level of the step.',
    search_quantities=SearchQuantities(
        include=[f'*#{dir}'],
    ),
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
                ],
            ),
            Menu(
                title='Method',
                items=[
                    MenuItemTerms(
                        title='step type', type='terms', search_quantity=f'{step}#{dir}'
                    ),
                    MenuItemTerms(
                        title='ID item processed',
                        type='terms',
                        search_quantity=f'data.id_item_processed#{dir}',
                    ),
                ],
            ),
            Menu(
                title='Integration',
                items=[],
            ),
            Menu(
                title='synthesis',
                items=[
                    Menu(
                        title='CVD',
                        items=[
                            MenuItemPeriodicTable(
                                title='Elements of the target material',
                                type='periodic_table',
                                width=8,
                                search_quantity=f'{mec}#{dir}',
                            ),
                            MenuItemTerms(
                                title='Name of the target material',
                                type='term',
                                search_quantity=f'data.steps.short_name#{dir}',
                            ),
                            MenuItemTerms(
                                title='Formula of the target material',
                                type='term',
                                search_quantity=f'data.steps.chemical_formula#{dir}',
                            ),
                            MenuItemPeriodicTable(
                                title='Elements in the gases employed',
                                type='periodic_table',
                                width=8,
                                search_quantity=f'{ec}#{dir}',
                            ),
                            MenuItemTerms(
                                title='Formulas of the gases employed',
                                type='term',
                                search_quantity=f'{flux}.chemical_formula#{dir}',
                            ),
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
