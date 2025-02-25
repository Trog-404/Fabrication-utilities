from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemCustomQuantities,
    SearchQuantities,
)

from fabrication_facilities.apps.menu_steps import (
    menuadd_bonding,
    menuadd_icpcvd,
    menuadd_spincoat,
    menuetchdrie,
    menuetchwetclean,
    menutrans_develop,
    menutrans_ebl,
    menutrans_fib,
)

dir = """
fabrication_facilities.schema_packages.fabrication_utilities.FabricationProcessStep
"""
dir1 = 'fabrication_facilities.schema_packages.add.ICP_CVD'
dir2 = 'fabrication_facilities.schema_packages.add.Spin_Coating'
dir3 = 'fabrication_facilities.schema_packages.transform.EBL'
dir4 = 'fabrication_facilities.schema_packages.transform.FIB'
dir5 = 'fabrication_facilities.schema_packages.remove.DRIE'
dir6 = 'fabrication_facilities.schema_packages.remove.WetCleaning'
dir7 = 'fabrication_facilities.schema_packages.transform.ResistDevelopment'
dir8 = 'fabrication_facilities.schema_packages.add.Bonding'
dir9 = 'fabrication_facilities.schema_packages.transform.Annealing'

schemas = [
    f'*#{dir}',
    f'*#{dir1}',
    f'*#{dir2}',
    f'*#{dir3}',
    f'*#{dir4}',
    f'*#{dir5}',
    f'*#{dir6}',
    f'*#{dir7}',
    f'*#{dir8}',
    f'*#{dir9}',
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
        Column(
            quantity=f'data.location#{dir}',
            selected=True,
        ),
        Column(quantity='upload_create_time', selected=True),
    ],
    filters_locked={'section_defs.definition_qualified_name': dir},
    menu=Menu(
        items=[
            Menu(
                title='Add steps',
                indentation=0,
                items=[
                    Menu(
                        title='Bonding',
                        items=[menuadd_bonding],
                    ),
                    Menu(
                        title='Integration',
                        items=[],
                    ),
                    Menu(
                        title='Sinthesys',
                        items=[
                            menuadd_icpcvd,
                            menuadd_spincoat,
                        ],
                    ),
                ],
            ),
            Menu(
                title='Transform steps',
                indentation=0,
                items=[
                    Menu(
                        title='Dicing',
                        items=[],
                    ),
                    Menu(
                        title='Doping',
                        items=[],
                    ),
                    Menu(
                        title='Lithography',
                        items=[
                            menutrans_ebl,
                            menutrans_fib,
                        ],
                    ),
                    Menu(
                        title='Solution modification',
                        items=[
                            menutrans_develop,
                        ],
                    ),
                    Menu(
                        title='Thermal processing',
                        items=[],
                    ),
                ],
            ),
            Menu(
                title='Remove steps',
                indentation=0,
                items=[
                    Menu(
                        title='Etching',
                        items=[
                            menuetchdrie,
                            menuetchwetclean,
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
