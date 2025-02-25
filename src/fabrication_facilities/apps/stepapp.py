from nomad.config.models.ui import (
    App,
    Column,
    Axis,
    Menu,
    MenuItemHistogram,
    MenuItemPeriodicTable,
    MenuItemCustomQuantities,
    MenuItemTerms,
    SearchQuantities,
)

dir = 'fabrication_facilities.schema_packages.fabrication_utilities.FabricationProcessStep'
dir1 = 'fabrication_facilities.schema_packages.add.ICP_CVD'
dir2 = 'fabrication_facilities.schema_packages.add.Spin_Coating'
dir3 = 'fabrication_facilities.schema_packages.transform.EBL'
dir4 = 'fabrication_facilities.schema_packages.transform.FIB'
dir5 = 'fabrication_facilities.schema_packages.remove.DRIE'
schemas = [
    f'*#{dir}',
    f'*#{dir1}',
    f'*#{dir2}',
    f'*#{dir3}',
    f'*#{dir4}',
    f'*#{dir5}',
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
                title='Add processes',
                indentation=0,
                items=[
                    Menu(
                        title='Integration',
                        size='xl',
                        items=[],
                    ),
                    Menu(
                        title='Sinthesys',
                        size='xl',
                        items=[
                            MenuItemTerms(
                                title='Name of the recipe',
                                type='terms',
                                search_quantity=f'data.recipe_name#{dir1}',
                            ),
                            MenuItemTerms(
                                title='Material to be deposited',
                                type='terms',
                                search_quantity=f'data.short_name#{dir1}',
                            ),
                            MenuItemPeriodicTable(
                                title='Elements deposited',
                                type='periodic_table',
                                search_quantity=f'data.material_elemental_composition.element#{dir1}',
                            ),
                            MenuItemHistogram(
                                title='Desired thickness',
                                type='histogram',
                                n_bins=10,
                                x=Axis(
                                    search_quantity=f'data.thickness_target#{dir1}',
                                    title='thickness',
                                    unit='nm',
                                ),
                            ),
                            MenuItemHistogram(
                                title='Chuck temperature',
                                type='histogram',
                                n_bins=10,
                                x=Axis(
                                    search_quantity=f'data.chuck_temperature#{dir1}',
                                    title='chuck_temperature',
                                    unit='celsius',
                                ),
                            ),
                            MenuItemHistogram(
                                title='Bias',
                                type='histogram',
                                n_bins=10,
                                x=Axis(
                                    search_quantity=f'data.bias#{dir1}',
                                    title='bias',
                                    unit='volt',
                                ),
                            ),
                            MenuItemHistogram(
                                title='Chamber pressure',
                                type='histogram',
                                n_bins=10,
                                x=Axis(
                                    search_quantity=f'data.chamber_pressure#{dir1}',
                                    title='chamber_pressure',
                                    unit='mbar',
                                ),
                            ),
                            MenuItemHistogram(
                                title='Power',
                                type='histogram',
                                n_bins=10,
                                x=Axis(
                                    search_quantity=f'data.power#{dir1}',
                                    title='chamber_pressure',
                                    unit='watt',
                                ),
                            ),
                        ],
                    ),
                ],
            ),
            Menu(
                title='Transform processes',
                indentation=0,
                items=[
                    Menu(
                        title='Lithography',
                        items=[
                            #                            Menu(
                            #                                title='EBL',
                            #                                size='xl',
                            #                                items=[
                            #                                    MenuItemTerms(
                            #                                        title='Name of the recipe',
                            #                                        type='terms',
                            #                                        search_quantity=f'data.recipe_name#{dir1}',
                            #                                    ),
                            #                                    MenuItemHistogram(
                            #                                        title='Desired thickness',
                            #                                        type='histogram',
                            #                                        n_bins=10,
                            #                                        x=Axis(
                            #                                            search_quantity=f'data.thickness_target#{dir1}',
                            #                                            title='thickness',
                            #                                            unit='nm',
                            #                                        ),
                            #                                    ),
                            #                                    MenuItemHistogram(
                            #                                        title='Chuck temperature',
                            #                                        type='histogram',
                            #                                        n_bins=10,
                            #                                        x=Axis(
                            #                                            search_quantity=f'data.chuck_temperature#{dir1}',
                            #                                            title='chuck_temperature',
                            #                                            unit='celsius',
                            #                                        ),
                            #                                    ),
                            #                                    MenuItemHistogram(
                            #                                        title='Bias',
                            #                                        type='histogram',
                            #                                        n_bins=10,
                            #                                        x=Axis(
                            #                                            search_quantity=f'data.bias#{dir1}',
                            #                                            title='bias',
                            #                                            unit='volt',
                            #                                        ),
                            #                                    ),
                            #                                    MenuItemHistogram(
                            #                                        title='Chamber pressure',
                            #                                        type='histogram',
                            #                                        n_bins=10,
                            #                                        x=Axis(
                            #                                            search_quantity=f'data.chamber_pressure#{dir1}',
                            #                                            title='chamber_pressure',
                            #                                            unit='mbar',
                            #                                        ),
                            #                                    ),
                            #                                    MenuItemHistogram(
                            #                                        title='Power',
                            #                                        type='histogram',
                            #                                        n_bins=10,
                            #                                        x=Axis(
                            #                                            search_quantity=f'data.power#{dir1}',
                            #                                            title='chamber_pressure',
                            #                                            unit='watt',
                            #                                        ),
                            #                                    ),
                            #                                ],
                            #                            ),
                        ],
                    ),
                ],
            ),
            Menu(
                title='Remove processes',
                indentation=0,
                items=[
                    Menu(
                        title='Etching',
                        items=[
                            Menu(
                                title='DRIE',
                                size='xl',
                                items=[
                                    MenuItemTerms(
                                        title='Name of the recipe',
                                        type='terms',
                                        search_quantity=f'data.recipe_name#{dir5}',
                                    ),
                                    MenuItemTerms(
                                        title='Material to be deposited',
                                        type='terms',
                                        search_quantity=f'data.short_name#{dir5}',
                                    ),
                                    MenuItemPeriodicTable(
                                        title='Elements deposited',
                                        type='periodic_table',
                                        search_quantity=f'data.material_elemental_composition.element#{dir5}',
                                    ),
                                    MenuItemHistogram(
                                        title='Desired thickness',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.thickness_target#{dir5}',
                                            title='thickness',
                                            unit='nm',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Chuck temperature',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.chuck_temperature#{dir5}',
                                            title='chuck_temperature',
                                            unit='celsius',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Bias',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.bias#{dir5}',
                                            title='bias',
                                            unit='volt',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Chamber pressure',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.chamber_pressure#{dir5}',
                                            title='chamber_pressure',
                                            unit='mbar',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Power',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.power#{dir5}',
                                            title='chamber_pressure',
                                            unit='watt',
                                        ),
                                    ),
                                ],
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
