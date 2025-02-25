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
        Column(quantity='upload_create_time', selected=True),
    ],
    filters_locked={'section_defs.definition_qualified_name': dir},
    menu=Menu(
        items=[
            Menu(
                title='Add processes',
                indentation=0,
                items=[
                    Menu(
                        title='Integration',
                        items=[],
                    ),
                    Menu(
                        title='Sinthesys',
                        items=[
                            Menu(
                                title='ICP-CVD',
                                size='xl',
                                items=[
                                    MenuItemTerms(
                                        title='Lab location',
                                        type='terms',
                                        search_quantity=f'data.location#{dir1}',
                                    ),
                                    #                                    MenuItemTerms(
                                    #                                        title='ID item processed',
                                    #                                        type='terms',
                                    #                                        search_quantity=f'data.id_item_processed#{dir1}',
                                    #                                    ),
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
                                    MenuItemPeriodicTable(
                                        title='Elements of gases employed',
                                        type='periodic_table',
                                        search_quantity=f'data.fluximeters.elemental_composition.element#{dir1}',
                                    ),
                                    MenuItemTerms(
                                        title='Gases formulas',
                                        type='terms',
                                        search_quantity=f'data.fluximeters.name#{dir1}',
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
                                    MenuItemHistogram(
                                        title='Effective duration',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.duration_effective#{dir1}',
                                            title='effective duration',
                                            unit='minute',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Thickness obtained',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.thickness_obtained#{dir1}',
                                            title='thickness obtained',
                                            unit='nm',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Deposition rate obtained',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.deposition_rate_obtained#{dir1}',
                                            title='deposition rate obtained',
                                            unit='nm/minute',
                                        ),
                                    ),
                                ],
                            ),
                            Menu(
                                title='Spin Coating',
                                size='xl',
                                items=[
                                    MenuItemTerms(
                                        title='Lab location',
                                        type='terms',
                                        search_quantity=f'data.location#{dir2}',
                                    ),
                                    #                        MenuItemTerms(
                                    #                            title='ID item processed',
                                    #                            type='terms',
                                    #                            search_quantity=f'data.id_item_processed#{dir2}',
                                    #                        ),
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
                title='Transform processes',
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
                                    #                MenuItemTerms(
                                    #                    title='Lab location',
                                    #                    type='terms',
                                    #                    search_quantity=f'data.location#{dir7}',
                                    #                ),
                                    #                MenuItemTerms(
                                    #                    title='ID item processed',
                                    #                    type='terms',
                                    #                    search_quantity=f'data.id_item_processed#{dir7}',
                                    #                ),
                                    #                MenuItemTerms(
                                    #                    title='Name of the recipe',
                                    #                    type='terms',
                                    #                    search_quantity=f'data.recipe_name#{dir7}',
                                    #                ),
                                    #                MenuItemTerms(
                                    #                    title='Developing solution',
                                    #                    type='terms',
                                    #                    search_quantity=f'data.developing_solution#{dir7}',
                                    #                ),
                                    #                MenuItemTerms(
                                    #                    title='Removing solution proportions',
                                    #                   type='terms',
                                    #                    search_quantity=f'data.developing_solution_proportions#{dir7}',
                                    #                ),
                                    #                MenuItemHistogram(
                                    #                    title='Developing duration',
                                    #                    type='histogram',
                                    #                    n_bins=10,
                                    #                    x=Axis(
                                    #                        search_quantity=f'data.developing_duration#{dir7}',
                                    #                        title='developing duration',
                                    #                        unit='minute',
                                    #                    ),
                                    #                ),
                                    #                MenuItemHistogram(
                                    #                    title='Developing temperature',
                                    #                    type='histogram',
                                    #                    n_bins=10,
                                    #                    x=Axis(
                                    #                        search_quantity=f'data.developing_temperature#{dir7}',
                                    #                        title='developing temperature',
                                    #                         unit='celsius',
                                    #                    ),
                                    #                ),
                                    #                MenuItemTerms(
                                    #                    title='Cleaning solution',
                                    #                    type='terms',
                                    #                    search_quantity=f'data.rising_solution#{dir7}',
                                    #                ),
                                    #                MenuItemTerms(
                                    #                    title='Cleaning solution proportions',
                                    #                    type='terms',
                                    #                   search_quantity=f'data.cleaning_solution_proportions#{dir7}',
                                    #                ),
                                    #                 MenuItemHistogram(
                                    #                    title='Cleaning duration',
                                    #                    type='histogram',
                                    #                    n_bins=10,
                                    #                    x=Axis(
                                    #                        search_quantity=f'data.cleaning_duration#{dir7}',
                                    #                        title='cleaning duration',
                                    #                        unit='minute',
                                    #                    ),
                                    #                ),
                                ],
                            )
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
                                        title='Lab location',
                                        type='terms',
                                        search_quantity=f'data.location#{dir5}',
                                    ),
                                    #                                    MenuItemTerms(
                                    #                                        title='ID item processed',
                                    #                                        type='terms',
                                    #                                        search_quantity=f'data.id_item_processed#{dir5}',
                                    #                                    ),
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
                                        title='Desired depth',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.depth_target#{dir5}',
                                            title='depth',
                                            unit='nm',
                                        ),
                                    ),
                                    MenuItemPeriodicTable(
                                        title='Elements of gases employed',
                                        type='periodic_table',
                                        search_quantity=f'data.fluximeters.elemental_composition.element#{dir5}',
                                    ),
                                    MenuItemTerms(
                                        title='Gases formulas',
                                        type='terms',
                                        search_quantity=f'data.fluximeters.name#{dir5}',
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
                                    MenuItemHistogram(
                                        title='Effective duration',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.duration_effective#{dir5}',
                                            title='effective duration',
                                            unit='nm',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Depth obtained',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.depth_obtained#{dir5}',
                                            title='depth obtained',
                                            unit='nm',
                                        ),
                                    ),
                                    MenuItemHistogram(
                                        title='Etching rate obtained',
                                        type='histogram',
                                        n_bins=10,
                                        x=Axis(
                                            search_quantity=f'data.etching_rate_obtained#{dir5}',
                                            title='etching rate obtained',
                                            unit='nm/minute',
                                        ),
                                    ),
                                ],
                            ),
                            Menu(
                                title='Wet cleaning',
                                size='xl',
                                items=[
                                    #                                   MenuItemTerms(
                                    #                                       title='Lab location',
                                    #                                       type='terms',
                                    #                                       search_quantity=f'data.location#{dir6}',
                                    #                                   ),
                                    #                                   MenuItemTerms(
                                    #                                       title='ID item processed',
                                    #                                       type='terms',
                                    #                                       search_quantity=f'data.id_item_processed#{dir6}',
                                    #                                   ),
                                    #                                   MenuItemTerms(
                                    #                                       title='Name of the recipe',
                                    #                                       type='terms',
                                    #                                       search_quantity=f'data.recipe_name#{dir6}',
                                    #                                   ),
                                    #                                   MenuItemTerms(
                                    #                                       title='Removing solution',
                                    #                                       type='terms',
                                    #                                       search_quantity=f'data.removing_solution#{dir6}',
                                    #                                   ),
                                    #                                   MenuItemTerms(
                                    #                                       title='Removing solution proportions',
                                    #                                       type='terms',
                                    #                                       search_quantity=f'data.removing_solution_proportions#{dir6}',
                                    #                                   ),
                                    #                                   MenuItemHistogram(
                                    #                                       title='Removing duration',
                                    #                                       type='histogram',
                                    #                                       n_bins=10,
                                    #                                       x=Axis(
                                    #                                           search_quantity=f'data.removing_duration#{dir6}',
                                    #                                           title='removing duration',
                                    #                                           unit='minute',
                                    #                                       ),
                                    #                                    ),
                                    #                                    MenuItemHistogram(
                                    #                                        title='Removing temperature',
                                    #                                        type='histogram',
                                    #                                        n_bins=10,
                                    #                                        x=Axis(
                                    #                                            search_quantity=f'data.removing_temperature#{dir6}',
                                    #                                            title='removing temperature',
                                    #                                            unit='celsius',
                                    #                                        ),
                                    #                                    ),
                                    #                                    MenuItemTerms(
                                    #                                        title='Rising solution',
                                    #                                        type='terms',
                                    #                                        search_quantity=f'data.rising_solution#{dir6}',
                                    #                                    ),
                                    #                                    MenuItemTerms(
                                    #                                        title='Rising solution proportions',
                                    #                                        type='terms',
                                    #                                        search_quantity=f'data.rising_solution_proportions#{dir6}',
                                    #                                    ),
                                    #                                    MenuItemHistogram(
                                    #                                        title='Rising duration',
                                    #                                        type='histogram',
                                    #                                        n_bins=10,
                                    #                                        x=Axis(
                                    #                                            search_quantity=f'data.rising_duration#{dir6}',
                                    #                                            title='rising duration',
                                    #                                            unit='minute',
                                    #                                        ),
                                    #                                    ),
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
