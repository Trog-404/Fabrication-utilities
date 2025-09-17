from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemCustomQuantities,
    MenuItemTerms,
    SearchQuantities,
)

dir0 = 'schema_packages.fabrication_utilities.Equipment'
Mainstr = 'data.equipmentTechniques.techniqueMainCategory'
Substr = 'data.equipmentTechniques.techniqueSubCategory'
gen = 'data.equipmentTechniques.genericEquipmentName'

equipmentapp = App(
    label='Fabrication equipments&Techniques',
    path='equipmentapp',
    category='Fabrication utilities',
    description='App to search fabrication equipments and useful techniques',
    readme="""
    This app allows to navigate through the equipments and techniques available in a
    clean room system. You can search the techniques available and than the availability
    of each instrument that has the desired technique included. At the end also the
    instrument's location is findable.
    """,
    search_quantities=SearchQuantities(
        include=[f'*#{dir0}'],
    ),
    columns=[
        Column(quantity='entry_name', selected=True),
        Column(quantity='entry_type'),
        Column(
            quantity=f'data.affiliation#{dir0}',
            selected=True,
        ),
        Column(
            quantity=f'data.institution#{dir0}',
            selected=True,
        ),
        Column(
            quantity=f'data.is_bookable#{dir0}',
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
                title='Institution',
                type='terms',
                search_quantity=f'data.institution#{dir0}',
            ),
            MenuItemTerms(
                title='Availability',
                type='terms',
                search_quantity=f'data.is_bookable#{dir0}',
            ),
            Menu(
                title='Techniques',
                indentation=0,
                items=[
                    MenuItemTerms(
                        title='Equipment class',
                        type='terms',
                        search_quantity=f'{gen}#{dir0}',
                    ),
                    MenuItemTerms(
                        title='MainTechnique',
                        type='terms',
                        search_quantity=f'{Mainstr}#{dir0}',
                    ),
                    MenuItemTerms(
                        title='fabrication step',
                        type='terms',
                        search_quantity=f'{Substr}#{dir0}',
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
