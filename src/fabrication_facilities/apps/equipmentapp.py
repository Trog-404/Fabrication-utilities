from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemCustomQuantities,
    MenuItemTerms,
    MenuItemHistogram,
    Axis,
    SearchQuantities,
)

dir = 'fabrication_facilities.schema_packages.equipment.Equipment'
Mainstr = 'data.equipmentTechniques.techniqueMainCategory'
Substr = 'data.equipmentTechniques.techniqueSubCategory'
cap = 'data.capabilities'
itp = 'data.permittedItems'

equipmentapp = App(
    label='Equipments',
    path='equipmentapp',
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
        items=[
            Menu(
                title='Infrastrucure',
                indentation=0,
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
                title='Techniques',
                indentation=0,
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
            Menu(
                title='Capabilities',
                indentation=0,
                items=[
                    MenuItemTerms(
                        title='property',
                        type='terms',
                        search_quantity=f'{cap}.name#{dir}',
                    ),
                    MenuItemHistogram(
                        title='min value',
                        x=Axis(
                            search_quantity=f'{cap}.value_min#{dir}',
                            title='Min value',
                        ),
                        nbins=10,
                    ),
                    MenuItemHistogram(
                        title='max value',
                        x=Axis(
                            search_quantity=f'{cap}.value_max#{dir}',
                            title='Min value',
                        ),
                        nbins=10,
                    ),
                ],
            ),
            Menu(
                title='Items allowed',
                indentation=0,
                items=[
                    MenuItemTerms(
                        title='items shape',
                        type='terms',
                        search_quantity=f'{itp}.itemShapeType#{dir}',
                    ),
                    MenuItemTerms(
                        title='items property',
                        type='terms',
                        search_quantity=f'{itp}.properties.name#{dir}',
                    ),
                    MenuItemHistogram(
                        title='min value',
                        x=Axis(
                            search_quantity=f'{itp}.properties.value_min#{dir}',
                            title='Min value',
                        ),
                        nbins=10,
                    ),
                    MenuItemHistogram(
                        title='max value',
                        x=Axis(
                            search_quantity=f'{itp}.properties.value_max#{dir}',
                            title='Min value',
                        ),
                        nbins=10,
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
