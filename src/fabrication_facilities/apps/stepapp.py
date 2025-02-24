from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemCustomQuantities,
    MenuItemTerms,
    SearchQuantities,
)

dir = 'fabrication_facilities.schema_packages.fabrication_utilities.FabricationProcessStep'
schemas = [
    '*#fabrication_facilities.schema_packages.fabrication_utilities.FabricationProcessStep',
    '*#fabrication_facilities.schema_packages.add.ICP_CVD',
    '*#fabrication_facilities.schema_packages.add.Spin_Coating',
]
stepapp = App(
    label='Fabrication steps',
    path='stepapp',
    category='Fabrication facilities',
    description='App to search fabrication processes.',
    readme=' The findability reach the level of the step.',
    search_quantities=SearchQuantities(include=schemas),
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
                title='General informations',
                indentation=0,
                items=[
                    MenuItemTerms(
                        title='Lab location',
                        type='terms',
                        search_quantity=f'data.location#{dir}',
                    ),
                    MenuItemTerms(
                        title='Step type',
                        type='terms',
                        search_quantity=f'data.step_type#{dir}',
                    ),
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
