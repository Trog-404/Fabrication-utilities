from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemTerms,
    SearchQuantities,
)

dir = 'fabrication_facilities.schema_packages.equipment.Equipment'
Mainstr = 'data.equipmentTechniques.techniqueMainCategory'
Substr = 'data.equipmentTechniques.techniqueSubCategory'
app_entry_point = AppEntryPoint(
    name='Fabrication findability',
    description='New app entry point configuration for fabrication facilities.',
    app=App(
        label='Equipments',
        path='app',
        category='Fabrication facilities',
        description='App to search fabrication equipments.',
        readme=' The findability reach the level of the single technique at disposal.',
        search_quantities=SearchQuantities(
            include=['*#fabrication_facilities.schema_packages.equipment.Equipment'],
        ),
        columns=[
            Column(quantity='entry_name', selected=True),
            Column(quantity='entry_type', selected=True),
            Column(
                quantity=f'data.institution#{dir}',
                selected=True,
            ),
            Column(quantity='upload_create_time', selected=True),
        ],
        filters_locked={'section_defs.definition_qualified_name': dir},
        menu=Menu(
            title='General informations',
            type='nested_object',
            items=[
                Menu(
                    title='Infrastrucure',
                    indentation=2,
                    items=[
                        MenuItemTerms(
                            title='Institution',
                            type='terms',
                            search_quantity=f'data.institution#{dir}',
                        ),
                        MenuItemTerms(
                            title='Availability',
                            type='terms',
                            search_quantity=f'data.is_bookable#{dir}',
                        ),
                    ],
                ),
                Menu(
                    title='Technique',
                    indentation=2,
                    items=[
                        MenuItemTerms(
                            title='MainTechnique',
                            type='terms',
                            search_quantity=f'{Mainstr}#{dir}',
                        ),
                        MenuItemTerms(
                            title='fabrication step',
                            type='terms',
                            search_quantity=f'{Substr}#{dir}',
                        ),
                    ],
                ),
            ],
        ),
    ),
)
