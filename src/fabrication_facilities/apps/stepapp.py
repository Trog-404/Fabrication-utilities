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

from fabrication_facilities.apps.menu_steps import (
    menuadd_icpcvd,
    menuadd_spincoat,
    menuetchdrie,
    menuetchwetclean,
)

dir = 'fabrication_facilities.schema_packages.fabrication_utilities.FabricationProcessStep'
dir1 = 'fabrication_facilities.schema_packages.add.ICP_CVD'
dir2 = 'fabrication_facilities.schema_packages.add.Spin_Coating'
dir3 = 'fabrication_facilities.schema_packages.transform.EBL'
dir4 = 'fabrication_facilities.schema_packages.transform.FIB'
dir5 = 'fabrication_facilities.schema_packages.remove.DRIE'
dir6 = 'fabrication_facilities.schema_packages.remove.WetCleaning'
dir7 = 'fabrication_facilities.schema_packages.transform.ResistDevelopment'
schemas = [
    f'*#{dir}',
    f'*#{dir1}',
    f'*#{dir2}',
    f'*#{dir3}',
    f'*#{dir4}',
    f'*#{dir5}',
    f'*#{dir6}',
    f'*#{dir7}',
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
                        title='Integration',
                        items=[],
                    ),
                    Menu(
                        title='Sinthesys',
                        items=[
                            menuadd_icpcvd,
                            menuadd_spincoat,
                            Menu(
                                title='Spin Coating',
                                size='xl',
                                items=[
                                    MenuItemTerms(
                                        title='Lab location',
                                        type='terms',
                                        search_quantity=f'data.location#{dir2}',
                                    ),
                                    MenuItemTerms(
                                        title='ID item processed',
                                        type='terms',
                                        search_quantity=f'data.id_item_processed#{dir2}',
                                    ),
                                    MenuItemTerms(
                                        title='Name of the recipe',
                                        type='terms',
                                        search_quantity=f'data.recipe_name#{dir2}',
                                    ),
                                    MenuItemTerms(
                                        title='Resist to be deposited',
                                        type='terms',
                                        search_quantity=f'data.short_name#{dir2}',
                                    ),
                                    MenuItemPeriodicTable(
                                        title='Elements of the resist deposited',
                                        type='periodic_table',
                                        search_quantity=f'data.resist_elemental_composition.element#{dir2}',
                                    ),
                                    MenuItemHistogram(
                                        title='Desired thickness',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.thickness_target#{dir2}',
                                            title='thickness',
                                            unit='nm',
                                        ),
                                    ),
                                    MenuItemTerms(
                                        title='HDMS',
                                        type='terms',
                                        search_quantity=f'data.hdms_required#{dir2}',
                                    ),
                                    MenuItemTerms(
                                        title='PEB',
                                        type='terms',
                                        search_quantity=f'data.peb_required#{dir2}',
                                    ),
                                    MenuItemHistogram(
                                        title='PEB duration',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.peb_duration#{dir2}',
                                            title='peb duration',
                                            unit='minute',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='PEB temperature',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.peb_temperature#{dir2}',
                                            title='peb temperature',
                                            unit='celsius',
                                        ),
                                    ),
                                    MenuItemTerms(
                                        title='Exposure',
                                        type='terms',
                                        search_quantity=f'data.exposure_required#{dir2}',
                                    ),
                                    MenuItemHistogram(
                                        title='Exposure duration',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.exposure_duration#{dir2}',
                                            title='exposure duration',
                                            unit='sec',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='De-wetting duration',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.dewetting_duration#{dir2}',
                                            title='de-wetting duration',
                                            unit='minute',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='De-wetting temperature',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.dewetting_temperature#{dir2}',
                                            title='De-wetting temperature',
                                            unit='celsius',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Spinned volume',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.spin_dispensed_volume#{dir2}',
                                            title='volume dispensed',
                                            unit='milliliter',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Spin duration',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.spin_duration#{dir2}',
                                            title='spin duration',
                                            unit='sec',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Spin frequency',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.spin_frequency#{dir2}',
                                            title='frequency',
                                            unit='rpm',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Spin angular acceleration',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.spin_angular_acceleration#{dir2}',
                                            title='angular acceleration',
                                            unit='rpm/sec',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Baking duration',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.baking_duration#{dir2}',
                                            title='baking duration',
                                            unit='minute',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Baking temperature',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.baking_temperature#{dir2}',
                                            title='baking temperature',
                                            unit='celsius',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Thickness obtained',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.thickness_obtained#{dir2}',
                                            title='thickness obtained',
                                            unit='nm',
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            Menu(
                title='Transform steps',
                indentation=0,
                items=[
                    Menu(
                        title='Lithography',
                        items=[],
                    ),
                    Menu(
                        title='Solution modification',
                        items=[
                            Menu(
                                title='Resist development',
                                size='xl',
                                items=[
                                    MenuItemTerms(
                                        title='Lab location',
                                        type='terms',
                                        search_quantity=f'data.location#{dir7}',
                                    ),
                                    MenuItemTerms(
                                        title='ID item processed',
                                        type='terms',
                                        search_quantity=f'data.id_item_processed#{dir7}',
                                    ),
                                    MenuItemTerms(
                                        title='Name of the recipe',
                                        type='terms',
                                        search_quantity=f'data.recipe_name#{dir7}',
                                    ),
                                    MenuItemTerms(
                                        title='Developing solution',
                                        type='terms',
                                        search_quantity=f'data.developing_solution#{dir7}',
                                    ),
                                    MenuItemTerms(
                                        title='Removing solution proportions',
                                        type='terms',
                                        search_quantity=f'data.developing_solution_proportions#{dir7}',
                                    ),
                                    MenuItemHistogram(
                                        title='Developing duration',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.developing_duration#{dir7}',
                                            title='developing duration',
                                            unit='minute',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Developing temperature',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.developing_temperature#{dir7}',
                                            title='developing temperature',
                                            unit='celsius',
                                        ),
                                    ),
                                    MenuItemTerms(
                                        title='Cleaning solution',
                                        type='terms',
                                        search_quantity=f'data.cleaning_solution#{dir7}',
                                    ),
                                    MenuItemTerms(
                                        title='Cleaning solution proportions',
                                        type='terms',
                                        search_quantity=f'data.cleaning_solution_proportions#{dir7}',
                                    ),
                                    MenuItemHistogram(
                                        title='Cleaning duration',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.cleaning_duration#{dir7}',
                                            title='cleaning duration',
                                            unit='minute',
                                        ),
                                    ),
                                ],
                            )
                        ],
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
