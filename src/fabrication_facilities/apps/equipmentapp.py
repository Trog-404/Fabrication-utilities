from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemCustomQuantities,
    MenuItemTerms,
    SearchQuantities,
)

dir = 'fabrication_facilities.schema_packages.equipment.Equipment'
Mainstr = 'data.equipmentTechniques.techniqueMainCategory'
Substr = 'data.equipmentTechniques.techniqueSubCategory'
gen = 'data.equipmentTechniques.genericEquipmentName'

equipmentapp = App(
    label='Equipments&Techniques',
    path='equipmentapp',
    category='Fabrication facilities',
    description='App to search fabrication equipments and useful techniques',
    readme="""
    This app allows to navigate through the equipments and techniques available in a
    clean room system. You can search the techniques available and than the availability
    of each instrument that has that technique included and the instrument's location
    """,
    search_quantities=SearchQuantities(
        include=['*#fabrication_facilities.schema_packages.equipment.Equipment'],
    ),
    columns=[
        Column(quantity='entry_name', selected=True),
        Column(quantity='entry_type'),
        Column(
            quantity=f'data.affiliation#{dir}',
            selected=True,
        ),
        Column(
            quantity=f'data.institution#{dir}',
            selected=True,
        ),
        Column(
            quantity=f'data.is_bookable#{dir}',
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
                        title='Equipment class',
                        type='terms',
                        search_quantity=f'{gen}#{dir}',
                    ),
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
