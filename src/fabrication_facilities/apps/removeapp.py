from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemCustomQuantities,
    MenuItemDefinitions,
    MenuItemTerms,
    SearchQuantities,
)

dir = 'fabrication_facilities.schema_packages.fabrication_steps.FabricationProcess'
Mainstr = 'data.equipmentTechniques.techniqueMainCategory'
Substr = 'data.equipmentTechniques.techniqueSubCategory'
cap = 'data.capabilities'
itp = 'data.permittedItems'

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
                    MenuItemDefinitions(title='prova', type='definitions'),
                    #                    MenuItemTerms(
                    #                        title='Product Type',
                    #                        type='terms',
                    #
                    #                    ),
                    # Menu(
                    #    title='Prova',
                    #    items=[
                    #        MenuItemTerms(
                    #            title='date',
                    #            type='terms',
                    #            search_quantity=f'data.starting_date#{dir}',
                    #        )
                    #    ],
                    # ),
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
