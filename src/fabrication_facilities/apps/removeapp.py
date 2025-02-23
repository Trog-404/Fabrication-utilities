from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemCustomQuantities,
    MenuItemPeriodicTable,
    MenuItemTerms,
    SearchQuantities,
)

schema = [
    '*#fabrication_facilities.schema_packages.fabrication_steps.FabricationProcess',
    '*#fabrication_facilities.schema_packages.fabrication_steps.add.SpinCoating',
    '*#fabrication_facilities.schema_packages.fabrication_steps.add.ICP_CVD',
]
dir = 'fabrication_facilities.schema_packages.fabrication_steps.FabricationProcess'
dir1 = 'fabrication_facilities.schema_packages.fabrication_steps.add.ICP_CVD'
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
    search_quantities=SearchQuantities(include=schema),
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
                title='synthesis',
                items=[
                    Menu(
                        title='CVD',
                        items=[
                            MenuItemPeriodicTable(
                                title='Elements of the target material',
                                type='periodic_table',
                                width=8,
                                search_quantity=f'{mec}#{dir1}',
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
#            Menu(
#                title='Integration',
#                items=[],
#            ),
