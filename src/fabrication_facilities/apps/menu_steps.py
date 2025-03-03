from nomad.config.models.ui import (
    Axis,
    Menu,
    MenuItemHistogram,
    MenuItemPeriodicTable,
    MenuItemTerms,
)

dir1 = 'fabrication_facilities.schema_packages.add.ICP_CVD'
dir2 = 'fabrication_facilities.schema_packages.add.Spin_Coating'
dir3 = 'fabrication_facilities.schema_packages.transform.EBL'
dir4 = 'fabrication_facilities.schema_packages.transform.FIB'
dir5 = 'fabrication_facilities.schema_packages.remove.DRIE'
dir6 = 'fabrication_facilities.schema_packages.remove.WetCleaning'
dir7 = 'fabrication_facilities.schema_packages.transform.ResistDevelopment'
dir8 = 'fabrication_facilities.schema_packages.add.Bonding'
dir9 = 'fabrication_facilities.schema_packages.transform.Annealing'

menuadd_icpcvd = Menu(
    title='ICP-CVD',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir1}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir1}',
        ),
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
                search_quantity=f'data.duration_measured#{dir1}',
                title='effective duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Thickness obtained',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_measured#{dir1}',
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
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir1}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir1}',
        ),
    ],
)

menuadd_spincoat = Menu(
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
                search_quantity=f'data.thickness_measured#{dir2}',
                title='thickness obtained',
                unit='nm',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir2}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir2}',
        ),
    ],
)
menuadd_bonding = Menu(title='Bonding', size='xl', items=[])
menutrans_ebl = Menu(
    title='E-Beam Lithography',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir3}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir3}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir3}',
        ),
        MenuItemHistogram(
            title='Dose',
            type='histogram',
            n_bins=10,
            x=Axis(title='dose', unit='uC/cm^2', search_quantity=f'data.dose#{dir3}'),
        ),
        MenuItemHistogram(
            title='Writing field dimension',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='writing field dimension',
                unit='um^2',
                search_quantity=f'data.writing_field_dimension#{dir3}',
            ),
        ),
        MenuItemHistogram(
            title='Address size',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='address size',
                unit='nm',
                search_quantity=f'data.address_size#{dir3}',
            ),
        ),
        MenuItemHistogram(
            title='Clock',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='clock',
                unit='MHz',
                search_quantity=f'data.clock#{dir3}',
            ),
        ),
        MenuItemHistogram(
            title='Current',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='current',
                unit='pA',
                search_quantity=f'data.current#{dir3}',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='chamber pressure',
                unit='mbar',
                search_quantity=f'data.chamber_pressure#{dir3}',
            ),
        ),
        MenuItemHistogram(
            title='Tension',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='tension',
                unit='V',
                search_quantity=f'data.tension#{dir3}',
            ),
        ),
        MenuItemTerms(
            title='Alignment required',
            type='terms',
            search_quantity=f'data.alignment_required#{dir3}',
        ),
        MenuItemHistogram(
            title='Max alignment error',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='max alignment error',
                unit='nm',
                search_quantity=f'data.alignment_max_error#{dir3}',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir3}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir3}',
        ),
    ],
)
menutrans_fib = Menu(
    title='Focused I-Beam Lithography',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir4}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir4}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir4}',
        ),
        MenuItemHistogram(
            title='Dose',
            type='histogram',
            n_bins=10,
            x=Axis(title='dose', unit='uC/cm^2', search_quantity=f'data.dose#{dir4}'),
        ),
        MenuItemHistogram(
            title='Writing field dimension',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='writing field dimension',
                unit='um^2',
                search_quantity=f'data.writing_field_dimension#{dir4}',
            ),
        ),
        MenuItemHistogram(
            title='Address size',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='address size',
                unit='nm',
                search_quantity=f'data.address_size#{dir4}',
            ),
        ),
        MenuItemHistogram(
            title='Clock',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='clock',
                unit='MHz',
                search_quantity=f'data.clock#{dir4}',
            ),
        ),
        MenuItemHistogram(
            title='Current',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='current',
                unit='pA',
                search_quantity=f'data.current#{dir4}',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='chamber pressure',
                unit='mbar',
                search_quantity=f'data.chamber_pressure#{dir4}',
            ),
        ),
        MenuItemHistogram(
            title='Tension',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='tension',
                unit='V',
                search_quantity=f'data.tension#{dir4}',
            ),
        ),
        MenuItemTerms(
            title='Alignment required',
            type='terms',
            search_quantity=f'data.alignment_required#{dir4}',
        ),
        MenuItemHistogram(
            title='Max alignment error',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='max alignment error',
                unit='nm',
                search_quantity=f'data.alignment_max_error#{dir3}',
            ),
        ),
        MenuItemHistogram(
            title='N° of loops',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='n° of loops',
                search_quantity=f'data.number_of_loops#{dir4}',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir4}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir4}',
        ),
    ],
)
menutrans_develop = Menu(
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
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir7}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir7}',
        ),
    ],
)

menuetchdrie = Menu(
    title='DRIE',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir5}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir5}',
        ),
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
            title='Required duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir5}',
                title='duration',
                unit='minute',
            ),
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
            search_quantity=f'data.fluximeters.chemical_formula#{dir5}',
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.chuck_temperature#{dir5}',
                title='chuck temperature',
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
                unit='V',
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
                title='power',
                unit='W',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_measured#{dir5}',
                title='effective duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Depth obtained',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_measured#{dir5}',
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
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir5}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir5}',
        ),
    ],
)
menuetchwetclean = Menu(
    title='Wet cleaning',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir6}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir6}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir6}',
        ),
        MenuItemTerms(
            title='Removing solution',
            type='terms',
            search_quantity=f'data.removing_solution#{dir6}',
        ),
        MenuItemTerms(
            title='Removing solution proportions',
            type='terms',
            search_quantity=f'data.removing_solution_proportions#{dir6}',
        ),
        MenuItemHistogram(
            title='Removing duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.removing_duration#{dir6}',
                title='removing duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Removing temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.removing_temperature#{dir6}',
                title='removing temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Rising solution',
            type='terms',
            search_quantity=f'data.rising_solution#{dir6}',
        ),
        MenuItemTerms(
            title='Rising solution proportions',
            type='terms',
            search_quantity=f'data.rising_solution_proportions#{dir6}',
        ),
        MenuItemHistogram(
            title='Rising duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.rising_duration#{dir6}',
                title='rising duration',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir6}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir6}',
        ),
    ],
)
