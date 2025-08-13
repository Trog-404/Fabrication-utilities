# This app is managing NOMAD explore menus to search characterization tools
# It shows both common fields/parameters and custom fields/parameters - 
# only some for each tools has been defined
# All tool parameters are searchable in the "User defined" section
# To be fixed: units for most of the custom parameters, like Ohm/sq, for sheet resistance
# and many others
from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemCustomQuantities,
    MenuItemTerms,
    SearchQuantities,
)

dir0 = 'fabrication_facilities.schema_packages.equipments.character_equipment.CharactEquipmentBase'
dir1 = 'fabrication_facilities.schema_packages.equipments.character_equipment.AFM_System'
dir2 = 'fabrication_facilities.schema_packages.equipments.character_equipment.FourPointProbe_System'


Mainstr = 'data.equipmentTechniques.techniqueMainCategory'
Substr = 'data.equipmentTechniques.techniqueSubCategory'
gen = 'data.equipmentTechniques.genericEquipmentName'

charact_equipmentapp = App(
    label='Characterization equipments&Techniques',
    path='charact_equipmentapp',
    category='Characterization facilities',
    description='App to search characterization equipments and useful techniques',
    readme="""
    This app allows to navigate through the equipments and techniques available in a
    clean room system. You can search the techniques available and than the availability
    of each instrument that has the desired technique included. At the end also the
    instrument's location is findable.
    """,
    search_quantities=SearchQuantities(
        include=[f'*#{dir0}',f'*#{dir1}',f'*#{dir2}'],
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
            Menu(
                title='AFM',
                items=[ 
                    MenuItemTerms(
                        title='Affiliation',
                        type='terms',
                        search_quantity=f'data.affiliation#{dir1}',
                    ),
                    MenuItemTerms(
                        title='Institution',
                        type='terms',
                        search_quantity=f'data.institution#{dir1}',
                    ),
                    MenuItemTerms(
                        title='Availability',
                        type='terms',
                        search_quantity=f'data.is_bookable#{dir1}',
                    ),
                    Menu(
                        title='Techniques',
                        indentation=0,
                        items=[
                            MenuItemTerms(
                                title='Equipment class',
                                type='terms',
                                search_quantity=f'{gen}#{dir1}',
                            ),
                            MenuItemTerms(
                                title='MainTechnique',
                                type='terms',
                                search_quantity=f'{Mainstr}#{dir1}',
                            ),
                            MenuItemTerms(
                                title='characterization step',
                                type='terms',
                                search_quantity=f'{Substr}#{dir1}',
                            ),
                        ],
                    ),
                    Menu(
                        title='AFM capabilities',
                        indentation=0,
                        items=[
                            MenuItemTerms(
                                title='afm tip',
                                type='terms',
                                search_quantity=f'data.afm_tip#{dir1}',
                            ),
                            MenuItemTerms(
                                title='afm mode',
                                type='terms',
                                search_quantity=f'data.afm_mode#{dir1}',
                            ),
                        ],
                    ),
               ],
            ),
            Menu(
                title='FourPointProbe',
                items=[ 
                    MenuItemTerms(
                        title='Affiliation',
                        type='terms',
                        search_quantity=f'data.affiliation#{dir2}',
                    ),
                    MenuItemTerms(
                        title='Institution',
                        type='terms',
                        search_quantity=f'data.institution#{dir2}',
                    ),
                    MenuItemTerms(
                        title='Availability',
                        type='terms',
                        search_quantity=f'data.is_bookable#{dir2}',
                    ),
                    Menu(
                        title='Techniques',
                        indentation=0,
                        items=[
                            MenuItemTerms(
                                title='Equipment class',
                                type='terms',
                                search_quantity=f'{gen}#{dir2}',
                            ),
                            MenuItemTerms(
                                title='MainTechnique',
                                type='terms',
                                search_quantity=f'{Mainstr}#{dir2}',
                            ),
                            MenuItemTerms(
                                title='characterization step',
                                type='terms',
                                search_quantity=f'{Substr}#{dir2}',
                            ),
                        ],
                    ),
                    Menu(
                        title='Four point probe capabilities',
                        indentation=0,
                        items=[
                            MenuItemTerms(
                                title='needles composition',
                                type='terms',
                                search_quantity=f'data.needles_composition#{dir2}',
                            ),
                        ],
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