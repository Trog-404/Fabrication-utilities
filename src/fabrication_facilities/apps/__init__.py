from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    SearchQuantities,
    Column,
    Menu,
    MenuItemCustomQuantities,
    MenuItemHistogram,
    MenuItemTerms,
)

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
                quantity='data.institution#fabrication_facilities.schema_packages.equipment.Equipment',
                selected=True,
            ),
            Column(quantity='upload_create_time', selected=True),
        ],
        menu=Menu(
            title='General informations',
            items=[
                Menu(
                    title='Institution',
                    indentation=2,
                    items=[
                        MenuItemCustomQuantities(
                            title='Institution', type='custom_quantities'
                        ),
                    ],
                ),
                #                    search_quantity='data.institution#fabrication_facilities.schema_packages.equipment.Equipment',
            ],
        ),
        # This is a submenu whose items become visible once selected. It
        # contains three items: one full-width histogram and two terms items
        # which are displayed side-by-side.
        # Menu(
        # title='Submenu',
        # size='md',
        # items=[
        # MenuItemHistogram(search_quantity='upload_create_time'),
        # These items target data from a custom schema
        # MenuItemTerms(
        #    width=6,
        #    search_quantity='data.quantity1#nomad_example.schema_packages.mypackage.MySchema',
        # ),
        # MenuItemTerms(
        #    width=6,
        #    search_quantity='data.quantity2#nomad_example.schema_packages.mypackage.MySchema',
        # ),
        #    ],
        #    ),
        #            ],
        #        ),
    ),
)
