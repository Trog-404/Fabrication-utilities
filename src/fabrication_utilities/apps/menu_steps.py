from apps.directories import dir_path
from nomad.config.models.ui import (
    Axis,
    Menu,
    MenuItemHistogram,
    MenuItemPeriodicTable,
    MenuItemTerms,
)

mec = 'data.synthesis_steps.material_elemental_composition.element'
flux = 'data.synthesis_steps.fluximeters.elemental_composition.element'
fluxetch = 'data.etching_steps.fluximeters.elemental_composition.element'
rec = 'data.coating_steps.resist_material.elemental_composition.element'
dmec = 'data.doping_material_elemental_composition.element'
wc = 'wafer_cleaning'
dev = 'developing'
meec = 'materials_etched.elemental_composition.element'
rute = 'data.etching_steps.reactives_used_to_etch.elemental_composition.element'
ru = 'data.etching_steps.reactives_used_to_etch'
alias = 'data.synthesis_steps.material_deposited.chemical_formula'


menuadd_icpcvd = Menu(
    title='ICP-CVD',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir1"]}',
        ),
        MenuItemHistogram(
            title='Desired thickness',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir1"]}',
                title='thickness',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Required duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir1"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Deposition rate target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.deposition_rate_target#{dir_path["dir1"]}',
                title='deposition rate target',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Kind of step',
            type='terms',
            search_quantity=f'data.synthesis_steps.tag#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='Material to be deposited',
            type='terms',
            search_quantity=f'data.synthesis_steps.name#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='Formula of the material to be deposited',
            type='terms',
            search_quantity=f'{alias}#{dir_path["dir1"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements deposited',
            type='periodic_table',
            search_quantity=f'data.synthesis_steps.material_deposited.elemental_composition.element#{dir_path["dir1"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of gases employed',
            type='periodic_table',
            search_quantity=f'{flux}#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='Gases formulas',
            type='terms',
            search_quantity=f'data.synthesis_steps.fluximeters.chemical_formula#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='Gases name',
            type='terms',
            search_quantity=f'data.synthesis_steps.fluximeters.name#{dir_path["dir1"]}',
        ),
        MenuItemHistogram(
            title='Gases fluxes',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.fluximeters.massflow#{dir_path["dir1"]}',
                unit='centimeter^3/minute',
            ),
        ),
        MenuItemHistogram(
            title='Chamber temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chamber_temperature#{dir_path["dir1"]}',
                title='chamber temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chamber_pressure#{dir_path["dir1"]}',
                title='chamber pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck.chuck_temperature#{dir_path["dir1"]}',
                title='chuck temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Bias',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck.bias#{dir_path["dir1"]}',
                title='bias',
                unit='volt',
            ),
        ),
        MenuItemHistogram(
            title='Chuck Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck.chuck_power#{dir_path["dir1"]}',
                title='chuck power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='Chuck low frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck.chuck_low_frequency#{dir_path["dir1"]}',
                title='chuck low frequency',
                unit='MHz',
            ),
        ),
        MenuItemHistogram(
            title='Chuck high frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck.chuck_high_frequency#{dir_path["dir1"]}',
                title='chuck high frequency',
                unit='MHz',
            ),
        ),
        MenuItemHistogram(
            title='ICP Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.icp_column.icp_power#{dir_path["dir1"]}',
                title='icp power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='ICP Frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.icp_column.icp_frequency#{dir_path["dir1"]}',
                title='icp frequency',
                unit='MHz',
            ),
        ),
        MenuItemTerms(
            title='Clamping type',
            type='terms',
            search_quantity=f'data.synthesis_steps.chuck.clamping.clamping_type#{dir_path["dir1"]}',
        ),
        MenuItemHistogram(
            title='Clamping pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck.clamping.clamping_pressure#{dir_path["dir1"]}',
                title='clamping pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir1"]}',
                title='effective duration',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir1"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir1"]}',
        ),
    ],
)

menuadd_pecvd = Menu(
    title='PECVD',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir27"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir27"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir27"]}',
        ),
        MenuItemHistogram(
            title='Desired thickness',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir27"]}',
                title='thickness',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Required duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir27"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Deposition rate target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.deposition_rate_target#{dir_path["dir27"]}',
                title='deposition rate target',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Kind of step',
            type='terms',
            search_quantity=f'data.synthesis_steps.tag#{dir_path["dir27"]}',
        ),
        MenuItemTerms(
            title='Material to be deposited',
            type='terms',
            search_quantity=f'data.synthesis_steps.material_deposited.name#{dir_path["dir27"]}',
        ),
        MenuItemTerms(
            title='Formula of the material to be deposited',
            type='terms',
            search_quantity=f'{alias}#{dir_path["dir27"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements deposited',
            type='periodic_table',
            search_quantity=f'data.synthesis_steps.material_deposited.elemental_composition.element#{dir_path["dir27"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of gases employed',
            type='periodic_table',
            search_quantity=f'{flux}#{dir_path["dir27"]}',
        ),
        MenuItemTerms(
            title='Gases formulas',
            type='terms',
            search_quantity=f'data.synthesis_steps.fluximeters.chemical_formula#{dir_path["dir27"]}',
        ),
        MenuItemTerms(
            title='Gases name',
            type='terms',
            search_quantity=f'data.synthesis_steps.fluximeters.name#{dir_path["dir27"]}',
        ),
        MenuItemHistogram(
            title='Gases fluxes',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.fluximeters.massflow#{dir_path["dir27"]}',
                unit='centimeter^3/minute',
            ),
        ),
        MenuItemHistogram(
            title='Chamber temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chamber_temperature#{dir_path["dir27"]}',
                title='chamber temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chamber_pressure#{dir_path["dir27"]}',
                title='chamber pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck.chuck_temperature#{dir_path["dir27"]}',
                title='chuck_temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Chuck Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck.chuck_power#{dir_path["dir27"]}',
                title='chuck power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='Chuck low frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck.chuck_low_frequency#{dir_path["dir27"]}',
                title='chuck low frequency',
                unit='MHz',
            ),
        ),
        MenuItemHistogram(
            title='Chuck high frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck.chuck_high_frequency#{dir_path["dir27"]}',
                title='chuck high frequency',
                unit='MHz',
            ),
        ),
        MenuItemTerms(
            title='Clamping type',
            type='terms',
            search_quantity=f'data.synthesis_steps.chuck.clamping.clamping_type#{dir_path["dir27"]}',
        ),
        MenuItemHistogram(
            title='Clamping pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chuck.clamping.clamping_pressure#{dir_path["dir27"]}',
                title='clamping pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir27"]}',
                title='effective duration',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir27"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir27"]}',
        ),
    ],
)

menuadd_lpcvd = Menu(
    title='LPCVD',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir28"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir28"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir28"]}',
        ),
        MenuItemHistogram(
            title='Desired thickness',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir28"]}',
                title='thickness',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Required duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir28"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Deposition rate target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.deposition_rate_target#{dir_path["dir28"]}',
                title='deposition rate target',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Kind of step',
            type='terms',
            search_quantity=f'data.synthesis_steps.tag#{dir_path["dir28"]}',
        ),
        MenuItemTerms(
            title='Material to be deposited',
            type='terms',
            search_quantity=f'data.synthesis_steps.material_deposited.name#{dir_path["dir28"]}',
        ),
        MenuItemTerms(
            title='Formula of the material to be deposited',
            type='terms',
            search_quantity=f'{alias}#{dir_path["dir28"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements deposited',
            type='periodic_table',
            search_quantity=f'data.synthesis_steps.material_deposited.elemental_composition.element#{dir_path["dir28"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of gases employed',
            type='periodic_table',
            search_quantity=f'{flux}#{dir_path["dir28"]}',
        ),
        MenuItemTerms(
            title='Gases formulas',
            type='terms',
            search_quantity=f'data.synthesis_steps.fluximeters.chemical_formula#{dir_path["dir28"]}',
        ),
        MenuItemTerms(
            title='Gases name',
            type='terms',
            search_quantity=f'data.synthesis_steps.fluximeters.name#{dir_path["dir28"]}',
        ),
        MenuItemHistogram(
            title='Gases fluxes',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.fluximeters.massflow#{dir_path["dir28"]}',
                unit='centimeter^3/minute',
            ),
        ),
        MenuItemHistogram(
            title='Chamber temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chamber_temperature#{dir_path["dir28"]}',
                title='chamber temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.synthesis_steps.chamber_pressure#{dir_path["dir28"]}',
                title='chamber pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir28"]}',
                title='effective duration',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir28"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir28"]}',
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
            search_quantity=f'data.location#{dir_path["dir2"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir2"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir2"]}',
        ),
        MenuItemTerms(
            title='Resist to be deposited',
            type='terms',
            search_quantity=f'data.coating_steps.resist_material.name#{dir_path["dir2"]}',
        ),
        MenuItemTerms(
            title='Formulas of the resist',
            type='terms',
            search_quantity=f'data.coating_steps.resist_material.chemical_formula#{dir_path["dir2"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the resist deposited',
            type='periodic_table',
            search_quantity=f'{rec}#{dir_path["dir2"]}',
        ),
        MenuItemHistogram(
            title='Desired thickness',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir2"]}',
                title='thickness',
                unit='nm',
            ),
        ),
        MenuItemTerms(
            title='Primer type',
            type='terms',
            search_quantity=f'data.coating_steps.priming.primer_name#{dir_path["dir2"]}',
        ),
        MenuItemTerms(
            title='Primer physical phase',
            type='terms',
            search_quantity=f'data.coating_steps.priming.primer_physical_phase#{dir_path["dir2"]}',
        ),
        MenuItemHistogram(
            title='Primer temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.coating_steps.priming.primer_temperature#{dir_path["dir2"]}',
                title='primer temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Dispening mode',
            type='histogram',
            search_quantity=f'data.coating_steps.dispensing_mode#{dir_path["dir2"]}',
        ),
        MenuItemHistogram(
            title='Dispensed volume',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.coating_steps.dispensed_volume#{dir_path["dir2"]}',
                title='dispensed volume',
                unit='milliliter',
            ),
        ),
        MenuItemHistogram(
            title='Spin duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.coating_steps.spin_phase.spin_duration#{dir_path["dir2"]}',
                title='spin duration',
                unit='sec',
            ),
        ),
        MenuItemHistogram(
            title='Spin frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.coating_steps.spin_phase.spin_frequency#{dir_path["dir2"]}',
                title='frequency',
                unit='rpm',
            ),
        ),
        MenuItemHistogram(
            title='Spin angular acceleration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.coating_steps.spin_phase.spin_angular_acceleration#{dir_path["dir2"]}',
                title='angular acceleration',
                unit='rpm/sec',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir2"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir2"]}',
        ),
    ],
)
menuadd_bonding = Menu(
    title='Bonding',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Wafer bonding type',
            type='terms',
            search_quantity=f'data.bonding_steps.wafer_bonding_type#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Alignment required',
            type='terms',
            search_quantity=f'data.bonding_steps.alignment_required#{dir_path["dir8"]}',
        ),
        MenuItemHistogram(
            title='Alignment max error',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.bonding_steps.alignment_max_error#{dir_path["dir8"]}',
                title='alignment error',
                unit='nm',
            ),
        ),
        MenuItemTerms(
            title='Wafer stack 1 name',
            type='terms',
            search_quantity=f'data.bonding_steps.wafer_stack_1_name#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Wafer stack 2 name',
            type='terms',
            search_quantity=f'data.bonding_steps.wafer_stack_2_name#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Wafer space required',
            type='terms',
            search_quantity=f'data.bonding_steps.wafer_space_required#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Alignment target mask name',
            type='terms',
            search_quantity=f'data.bonding_steps.alignment_target_mask_name#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Alignment viewfinder mask name',
            type='terms',
            search_quantity=f'data.bonding_steps.alignment_viewfinder_mask_name#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Wafer bonded name',
            type='terms',
            search_quantity=f'data.outputs.wafer_bonded_name#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Wafer bonded id',
            type='terms',
            search_quantity=f'data.outputs.wafer_bonded_id#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir8"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir8"]}',
        ),
    ],
)
menutrans_ebl = Menu(
    title='E-Beam Lithography',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir3"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir3"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir3"]}',
        ),
        MenuItemHistogram(
            title='Area dose',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='area dose',
                unit='uC/cm^2',
                search_quantity=f'data.writing_steps.writing_settings.area_dose#{dir_path["dir3"]}',
            ),
        ),
        MenuItemHistogram(
            title='Line dose',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='line dose',
                unit='pC/cm',
                search_quantity=f'data.writing_steps.writing_settings.line_dose#{dir_path["dir3"]}',
            ),
        ),
        MenuItemHistogram(
            title='Dot dose',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='dot dose',
                unit='pC',
                search_quantity=f'data.writing_steps.writing_settings.dot_dose#{dir_path["dir3"]}',
            ),
        ),
        MenuItemHistogram(
            title='Writing field dimension',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='writing field dimension',
                unit='um^2',
                search_quantity=f'data.writing_steps.writing_settings.writing_field_dimension#{dir_path["dir3"]}',
            ),
        ),
        MenuItemHistogram(
            title='Horizontal address size',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='horizontal address size',
                unit='nm',
                search_quantity=f'data.writing_steps.writing_settings.address_size_x#{dir_path["dir3"]}',
            ),
        ),
        MenuItemHistogram(
            title='Vertical address size',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='vertical address size',
                unit='nm',
                search_quantity=f'data.writing_steps.writing_settings.address_size_y#{dir_path["dir3"]}',
            ),
        ),
        MenuItemHistogram(
            title='Settling time',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='settling time',
                unit='us',
                search_quantity=f'data.writing_steps.writing_settings.settling_time#{dir_path["dir3"]}',
            ),
        ),
        MenuItemHistogram(
            title='Current desired',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='current desired',
                unit='pA',
                search_quantity=f'data.writing_steps.beam_column.current_target#{dir_path["dir3"]}',
            ),
        ),
        MenuItemHistogram(
            title='Tension',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='tension',
                unit='kV',
                search_quantity=f'data.writing_steps.beam_column.tension#{dir_path["dir3"]}',
            ),
        ),
        MenuItemTerms(
            title='Alignment mode',
            type='terms',
            search_quantity=f'data.writing_steps.alignment.alignment_mode#{dir_path["dir3"]}',
        ),
        MenuItemHistogram(
            title='Max alignment error',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='max alignment error',
                unit='nm',
                search_quantity=f'data.writing_steps.alignment.alignment_max_error#{dir_path["dir3"]}',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir3"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir3"]}',
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
            search_quantity=f'data.location#{dir_path["dir4"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir4"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir4"]}',
        ),
        MenuItemTerms(
            title='Probe',
            type='terms',
            search_quantity=f'data.writing_steps.beam_column.beam_source.probe#{dir_path["dir4"]}',
        ),
        MenuItemHistogram(
            title='Area dose',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='area dose',
                unit='uC/cm^2',
                search_quantity=f'data.writing_steps.writing_settings.area_dose#{dir_path["dir4"]}',
            ),
        ),
        MenuItemHistogram(
            title='Line dose',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='line dose',
                unit='pC/cm',
                search_quantity=f'data.writing_steps.writing_settings.line_dose#{dir_path["dir4"]}',
            ),
        ),
        MenuItemHistogram(
            title='Dot dose',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='dot dose',
                unit='pC',
                search_quantity=f'data.writing_steps.writing_settings.dot_dose#{dir_path["dir4"]}',
            ),
        ),
        MenuItemHistogram(
            title='Writing field dimension',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='writing field dimension',
                unit='um^2',
                search_quantity=f'data.writing_steps.writing_settings.writing_field_dimension#{dir_path["dir4"]}',
            ),
        ),
        MenuItemHistogram(
            title='Horizontal address size',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='horizontal address size',
                unit='nm',
                search_quantity=f'data.writing_steps.writing_settings.address_size_x#{dir_path["dir4"]}',
            ),
        ),
        MenuItemHistogram(
            title='Vertical address size',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='vertical address size',
                unit='nm',
                search_quantity=f'data.writing_steps.writing_settings.address_size_y#{dir_path["dir4"]}',
            ),
        ),
        MenuItemHistogram(
            title='Settling time',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='settling time',
                unit='us',
                search_quantity=f'data.writing_steps.writing_settings.settling_time#{dir_path["dir4"]}',
            ),
        ),
        MenuItemHistogram(
            title='Current desired',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='current desired',
                unit='pA',
                search_quantity=f'data.writing_steps.beam_column.current_target#{dir_path["dir4"]}',
            ),
        ),
        MenuItemHistogram(
            title='Tension',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='tension',
                unit='kV',
                search_quantity=f'data.writing_steps.beam_column.tension#{dir_path["dir4"]}',
            ),
        ),
        MenuItemTerms(
            title='Alignment mode',
            type='terms',
            search_quantity=f'data.writing_steps.alignment.alignment_mode#{dir_path["dir4"]}',
        ),
        MenuItemHistogram(
            title='Max alignment error',
            type='histogram',
            n_bins=10,
            x=Axis(
                title='max alignment error',
                unit='nm',
                search_quantity=f'data.writing_steps.alignment.alignment_max_error#{dir_path["dir4"]}',
            ),
        ),
        MenuItemPeriodicTable(
            title='Elements of gases employed',
            type='periodic_table',
            search_quantity=f'data.writing_steps.fluximeters.elemental_composition.element#{dir_path["dir4"]}',
        ),
        MenuItemTerms(
            title='Gases formulas',
            type='terms',
            search_quantity=f'data.writing_steps.fluximeters.chemical_formula#{dir_path["dir4"]}',
        ),
        MenuItemTerms(
            title='Gases name',
            type='terms',
            search_quantity=f'data.writing_steps.fluximeters.name#{dir_path["dir4"]}',
        ),
        MenuItemHistogram(
            title='Gases fluxes',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.writing_steps.fluximeters.massflow#{dir_path["dir4"]}',
                unit='centimeter^3/minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir4"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir4"]}',
        ),
    ],
)
menuremove_resistdev = Menu(
    title='Resist development',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='Mode',
            type='terms',
            search_quantity=f'data.development_steps.developing_mode#{dir_path["dir7"]}',
        ),
        MenuItemHistogram(
            title='Developing temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.development_steps.developing_temperature#{dir_path["dir7"]}',
                title='developing temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Name of the material developed',
            type='terms',
            search_quantity=f'data.development_steps.materials_developed.name#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='Formula of the material developed',
            type='terms',
            search_quantity=f'data.development_steps.materials_developed.chemical_formula#{dir_path["dir7"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the material developed',
            type='periodic_table',
            search_quantity=f'data.development_steps.materials_developed.elemental_composition.element#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='Name of the developing solution components',
            type='terms',
            search_quantity=f'data.development_steps.developing_solution.developing_solution_components.name#{dir_path["dir7"]}',
        ),
        MenuItemHistogram(
            title='Developer dispensed volume',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.development_steps.developing_solution.dispensed_volume#{dir_path["dir7"]}',
                title='dispensed volume',
                unit='milliliter',
            ),
        ),
        MenuItemTerms(
            title='Name of the surfactant in the solution',
            type='terms',
            search_quantity=f'data.development_steps.developing_solution.surfactants.name#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='Rinsing mode',
            type='terms',
            search_quantity=f'data.development_steps.final_rinsing.rinsing_mode#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='Rinser name',
            type='terms',
            search_quantity=f'data.development_steps.final_rinsing.rinser_name#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir7"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir7"]}',
        ),
    ],
)

menuremove_icprie = Menu(
    title='ICP RIE',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir5"]}',
        ),
        MenuItemHistogram(
            title='Desired depth',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_target#{dir_path["dir5"]}',
                title='depth',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Required duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir5"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Etching rate target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_rate_target#{dir_path["dir5"]}',
                title='etching rate target',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Kind of step',
            type='terms',
            search_quantity=f'data.etching_steps.tag#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='Material to be etched',
            type='terms',
            search_quantity=f'data.etching_steps.materials_etched.name#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='Formulas of the etched material',
            type='terms',
            search_quantity=f'data.etching_steps.materials_etched.chemical_formula#{dir_path["dir5"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements etched',
            type='periodic_table',
            search_quantity=f'data.etching_steps.{meec}#{dir_path["dir5"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of gases employed',
            type='periodic_table',
            search_quantity=f'{fluxetch}#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='Gases formulas',
            type='terms',
            search_quantity=f'data.etching_steps.fluximeters.chemical_formula#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='Gases name',
            type='terms',
            search_quantity=f'data.etching_steps.fluximeters.name#{dir_path["dir5"]}',
        ),
        MenuItemHistogram(
            title='Gases fluxes',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.fluximeters.massflow#{dir_path["dir5"]}',
                unit='centimeter^3/minute',
            ),
        ),
        MenuItemHistogram(
            title='Chamber temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chamber_temperature#{dir_path["dir5"]}',
                title='chamber temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chamber_pressure#{dir_path["dir5"]}',
                title='chamber pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.chuck_temperature#{dir_path["dir5"]}'
                ),
                title='chuck temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Chuck Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.chuck_power#{dir_path["dir5"]}'
                ),
                title='chuck power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='Chuck high frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.chuck_high_frequency#{dir_path["dir5"]}'
                ),
                title='chuck high frequency',
                unit='MHz',
            ),
        ),
        MenuItemHistogram(
            title='Chuck low frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.chuck_low_frequency#{dir_path["dir5"]}'
                ),
                title='chuck low frequency',
                unit='MHz',
            ),
        ),
        MenuItemHistogram(
            title='Bias voltage',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(f'data.etching_steps.chuck.bias#{dir_path["dir5"]}'),
                title='bias voltage',
                unit='V',
            ),
        ),
        MenuItemHistogram(
            title='ICP Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.icp_column.icp_power#{dir_path["dir5"]}'
                ),
                title='icp power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='ICP Frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.icp_column.icp_frequency#{dir_path["dir5"]}'
                ),
                title='icp frequency',
                unit='MHz',
            ),
        ),
        MenuItemTerms(
            title='Clamping',
            type='terms',
            search_quantity=(
                f'data.etching_steps.chuck.clamping.clamping_type#{dir_path["dir5"]}'
            ),
        ),
        MenuItemHistogram(
            title='Clamping pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.clamping.clamping_pressure#{dir_path["dir5"]}'
                ),
                title='clamping pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir5"]}',
                title='effective duration',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir5"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir5"]}',
        ),
    ],
)
menuremove_wetclean = Menu(
    title='Wet cleaning',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir6"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir6"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir6"]}',
        ),
        MenuItemTerms(
            title='Cleaning tag',
            type='terms',
            search_quantity=f'data.cleaning_steps.tag#{dir_path["dir6"]}',
        ),
        MenuItemTerms(
            title='Material to be cleaned',
            type='terms',
            search_quantity=f'data.cleaning_steps.materials_etched.name#{dir_path["dir6"]}',
        ),
        MenuItemTerms(
            title='Formulas of the cleaned material',
            type='terms',
            search_quantity=(
                f'data.cleaning_steps.materials_etched.chemical_formula#{dir_path["dir6"]}'
            ),
        ),
        MenuItemPeriodicTable(
            title='Elements of the material',
            type='periodic_table',
            search_quantity=f'data.cleaning_steps.{meec}#{dir_path["dir6"]}',
        ),
        MenuItemTerms(
            title='Cleaning reactives',
            type='terms',
            search_quantity=f'data.cleaning_steps.reactives_used_to_etch.name#{dir_path["dir6"]}',
        ),
        MenuItemTerms(
            title='Formula of the reactives used to clean',
            type='terms',
            search_quantity=f'data.cleaning_steps.reactives_used_to_etch.chemical_formula#{dir_path["dir6"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the cleaning compounds',
            type='periodic_table',
            search_quantity=f'data.cleaning_steps.reactives_used_to_etch.elemental_composition.element#{dir_path["dir6"]}',
        ),
        MenuItemHistogram(
            title='Cleaning reactives concentration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.cleaning_steps.reactives_used_to_etch.solution_concentration#{dir_path["dir6"]}',
                title='cleaning reactives concentration(%)',
            ),
        ),
        MenuItemTerms(
            title='Wetting required',
            type='terms',
            search_quantity=f'data.cleaning_steps.wetting#{dir_path["dir6"]}',
        ),
        MenuItemHistogram(
            title='Cleaning temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.cleaning_steps.tank_temperature#{dir_path["dir6"]}',
                title='cleaning temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Resistivity cut off',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.cleaning_steps.resistivity_control.resistivity_target#{dir_path["dir6"]}',
                title='resistivity cut off',
                unit='ohm*cm',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir6"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir6"]}',
        ),
    ],
)
menutrans_annealing = Menu(
    title='Annealing',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir9"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir9"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir9"]}',
        ),
        MenuItemTerms(
            title='Material annealed',
            type='terms',
            search_quantity=f'data.annealing_steps.annealed_material.name#{dir_path["dir9"]}',
        ),
        MenuItemTerms(
            title='Material annealed formula',
            type='terms',
            search_quantity=f'data.annealing_steps.annealed_material.chemical_formula#{dir_path["dir9"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the material',
            type='periodic_table',
            search_quantity=f'data.annealing_steps.annealed_material.elemental_composition.element#{dir_path["dir9"]}',
        ),
        MenuItemTerms(
            title='Gas name',
            type='terms',
            search_quantity=f'data.annealing_steps.fluximeters.name#{dir_path["dir9"]}',
        ),
        MenuItemTerms(
            title='Gas formula',
            type='terms',
            search_quantity=f'data.annealing_steps.fluximeters.chemical_formula#{dir_path["dir9"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the gas',
            type='periodic_table',
            search_quantity=f'data.annealing_steps.fluximeters.elemental_composition.element#{dir_path["dir9"]}',
        ),
        MenuItemHistogram(
            title='Gas flow',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.annealing_steps.fluximeters.massflow#{dir_path["dir9"]}',
                title='gas flow',
                unit='centimeter^3/minute',
            ),
        ),
        MenuItemHistogram(
            title='Starting temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.annealing_steps.ramp_up.start_value#{dir_path["dir9"]}',
                title='starting temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Target final temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.annealing_steps.ramp_up.end_value#{dir_path["dir9"]}',
                title='target final temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Ramp up rate',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.annealing_steps.ramp_up.rate#{dir_path["dir9"]}',
                title='ramp up rate',
                unit='celsius/minute',
            ),
        ),
        MenuItemHistogram(
            title='Ramp down rate',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.annealing_steps.ramp_down.rate#{dir_path["dir9"]}',
                title='ramp down rate',
                unit='celsius/minute',
            ),
        ),
        MenuItemHistogram(
            title='Duration measured',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir9"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Final temperature measured',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.final_temperature_measured#{dir_path["dir9"]}',
                title='temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir9"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir9"]}',
        ),
    ],
)
# menutrans_ltodensification = Menu(
#     title='LTO Densification',
#     size='xl',
#     items=[
#         MenuItemTerms(
#             title='Lab location',
#             type='terms',
#             search_quantity=f'data.location#{dir_path["dir10"]}',
#         ),
#         MenuItemTerms(
#             title='ID item processed',
#             type='terms',
#             search_quantity=f'data.id_item_processed#{dir_path["dir10"]}',
#         ),
#         MenuItemTerms(
#             title='Name of the recipe',
#             type='terms',
#             search_quantity=f'data.recipe_name#{dir_path["dir10"]}',
#         ),
#         MenuItemTerms(
#             title='Densification type',
#             type='terms',
#             search_quantity=f'data.densification_type#{dir_path["dir10"]}',
#         ),
#         MenuItemTerms(
#             title='Densification gas',
#             type='terms',
#             search_quantity=f'data.short_name#{dir_path["dir10"]}',
#         ),
#         MenuItemPeriodicTable(
#             title='Elements of the gas',
#             type='periodic_table',
#             search_quantity=f'{gec}#{dir_path["dir10"]}',
#         ),
#         MenuItemHistogram(
#             title='Densification temperature',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.temperature_target#{dir_path["dir10"]}',
#                 title='densification temperature',
#                 unit='celsius',
#             ),
#         ),
#         MenuItemHistogram(
#             title='Gas flow',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.gas_flow#{dir_path["dir10"]}',
#                 title='gas flow',
#                 unit='centimeter^3/minute',
#             ),
#         ),
#         MenuItemHistogram(
#             title='Effective duration',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.duration_measured#{dir_path["dir10"]}',
#                 title='duration measured',
#                 unit='minute',
#             ),
#         ),
#         MenuItemTerms(
#             title='Name equipment used',
#             type='terms',
#             search_quantity=f'data.instruments.name#{dir_path["dir10"]}',
#         ),
#         MenuItemTerms(
#             title='ID equipment used',
#             type='terms',
#             search_quantity=f'data.instruments.id#{dir_path["dir10"]}',
#         ),
#     ],
# )
menutrans_thermaloxidation = Menu(
    title='Thermal Oxidation',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir11"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir11"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir11"]}',
        ),
        MenuItemHistogram(
            title='Thickness target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir11"]}',
                title='thickness',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Duration target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir11"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Oxidation rate target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.oxidation_rate_target#{dir_path["dir11"]}',
                title='oxidation rate',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Oxidation type',
            type='terms',
            search_quantity=f'data.oxidation_steps.oxidation_type#{dir_path["dir11"]}',
        ),
        MenuItemHistogram(
            title='Target final temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.oxidation_steps.temperature_final_target#{dir_path["dir11"]}',
                title='temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Thermal oxidation gas',
            type='terms',
            search_quantity=f'data.oxidation_steps.fluximeters.name#{dir_path["dir11"]}',
        ),
        MenuItemTerms(
            title='Thermal oxidation gas formula',
            type='terms',
            search_quantity=f'data.oxidation_steps.fluximeters.chemical_formula#{dir_path["dir11"]}',
        ),
        MenuItemHistogram(
            title='Thermal oxidation gas flow rate',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.oxidation_steps.fluximeters.massflow#{dir_path["dir11"]}',
                title='flow rate',
                unit='cm^3/minute',
            ),
        ),
        MenuItemPeriodicTable(
            title='Elements of the gas',
            type='periodic_table',
            search_quantity=f'data.oxidation_steps.fluximeters.elemental_composition.element#{dir_path["dir11"]}',
        ),
        MenuItemHistogram(
            title='Duration measured',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir11"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir11"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir11"]}',
        ),
    ],
)
menutrans_dicing = Menu(
    title='Dicing',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir12"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir12"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir12"]}',
        ),
        MenuItemTerms(
            title='Blade name',
            type='terms',
            search_quantity=f'data.dicing_blade_name#{dir_path["dir12"]}',
        ),
        MenuItemHistogram(
            title='Depth target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_target#{dir_path["dir12"]}',
                title='depth target',
                unit='um',
            ),
        ),
        MenuItemTerms(
            title='Protective film required',
            type='terms',
            search_quantity=f'data.dicing_steps.protective_film_required#{dir_path["dir12"]}',
        ),
        MenuItemHistogram(
            title='Spindle frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.dicing_steps.spindle_frequency#{dir_path["dir12"]}',
                title='spindle frequency',
                unit='rpm',
            ),
        ),
        MenuItemHistogram(
            title='Dicing feed rate',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.dicing_steps.dicing_feed_rate#{dir_path["dir12"]}',
                title='feed rate',
                unit='mm/s',
            ),
        ),
        MenuItemHistogram(
            title='Depth step 1',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.dicing_steps.depth_step#{dir_path["dir12"]}',
                title='depth step 1',
                unit='um',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir12"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir12"]}',
        ),
    ],
)
# menutrans_doping = Menu(
#     title='Doping',
#     size='xl',
#     items=[
#         MenuItemTerms(
#             title='Lab location',
#             type='terms',
#             search_quantity=f'data.location#{dir_path["dir13"]}',
#         ),
#         MenuItemTerms(
#             title='ID item processed',
#             type='terms',
#             search_quantity=f'data.id_item_processed#{dir_path["dir13"]}',
#         ),
#         MenuItemTerms(
#             title='Name of the recipe',
#             type='terms',
#             search_quantity=f'data.recipe_name#{dir_path["dir13"]}',
#         ),
#         MenuItemTerms(
#             title='Doping type',
#             type='terms',
#             search_quantity=f'data.doping_type#{dir_path["dir13"]}',
#         ),
#         MenuItemHistogram(
#             title='Doping temperature',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.temperature_target#{dir_path["dir13"]}',
#                 title='doping temperature',
#                 unit='celsius',
#             ),
#         ),
#         MenuItemHistogram(
#             title='Doping duration',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.duration_target#{dir_path["dir13"]}',
#                 title='doping duration',
#                 unit='minute',
#             ),
#         ),
#         MenuItemTerms(
#             title='Name equipment used',
#             type='terms',
#             search_quantity=f'data.instruments.name#{dir_path["dir13"]}',
#         ),
#         MenuItemTerms(
#             title='ID equipment used',
#             type='terms',
#             search_quantity=f'data.instruments.id#{dir_path["dir13"]}',
#         ),
#     ],
# )
# menutrans_labelingcleaning = Menu(
#     title='Labeling & Cleaning',
#     size='xl',
#     items=[
#         MenuItemTerms(
#             title='Lab location',
#             type='terms',
#             search_quantity=f'data.location#{dir_path["dir14"]}',
#         ),
#         MenuItemTerms(
#             title='ID item processed',
#             type='terms',
#             search_quantity=f'data.id_item_processed#{dir_path["dir14"]}',
#         ),
#         MenuItemTerms(
#             title='Name of the recipe',
#             type='terms',
#             search_quantity=f'data.recipe_name#{dir_path["dir14"]}',
#         ),
#         MenuItemTerms(
#             title='Wafer label position',
#             type='terms',
#             search_quantity=f'data.wafer_label_position#{dir_path["dir14"]}',
#         ),
#         MenuItemTerms(
#             title='Wafer label name',
#             type='terms',
#             search_quantity=f'data.wafer_label_name#{dir_path["dir14"]}',
#         ),
#         MenuItemTerms(
#             title='Cleaning with DI ultrasound?',
#             type='terms',
#             search_quantity=f'data.{wc}_DI_ultrasound_required#{dir_path["dir14"]}',
#         ),
#         MenuItemTerms(
#             title='RCA cleaning?',
#             type='terms',
#             search_quantity=f'data.{wc}_rca_required#{dir_path["dir14"]}',
#         ),
#         MenuItemTerms(
#             title='Piranha cleaning?',
#             type='terms',
#             search_quantity=f'data.{wc}_piranha_required#{dir_path["dir14"]}',
#         ),
#         MenuItemTerms(
#             title='Dip HF cleaning?',
#             type='terms',
#             search_quantity=f'data.{wc}_dipHF_required#{dir_path["dir14"]}',
#         ),
#         MenuItemTerms(
#             title='Name equipment used',
#             type='terms',
#             search_quantity=f'data.instruments.name#{dir_path["dir14"]}',
#         ),
#         MenuItemTerms(
#             title='ID equipment used',
#             type='terms',
#             search_quantity=f'data.instruments.id#{dir_path["dir14"]}',
#         ),
#     ],
# )
# menutrans_sod = Menu(
#     title='SOD',
#     size='xl',
#     items=[
#         MenuItemTerms(
#             title='Lab location',
#             type='terms',
#             search_quantity=f'data.location#{dir_path["dir15"]}',
#         ),
#         MenuItemTerms(
#             title='ID item processed',
#             type='terms',
#             search_quantity=f'data.id_item_processed#{dir_path["dir15"]}',
#         ),
#         MenuItemTerms(
#             title='Name of the recipe',
#             type='terms',
#             search_quantity=f'data.recipe_name#{dir_path["dir15"]}',
#         ),
#         MenuItemTerms(
#             title='Dopant solution (short name)',
#             type='terms',
#             search_quantity=f'data.short_name#{dir_path["dir15"]}',
#         ),
#         MenuItemPeriodicTable(
#             title='Elements of the solution',
#             type='periodic_table',
#             search_quantity=f'{dmec}#{dir_path["dir15"]}',
#         ),
#         MenuItemHistogram(
#             title='Volume dispensed',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.spin_dispensed_volume#{dir_path["dir15"]}',
#                 title='spin dispensed volume',
#                 unit='milliliter',
#             ),
#         ),
#         MenuItemHistogram(
#             title='Dip HF duration',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.spin_dipHF_duration#{dir_path["dir15"]}',
#                 title='dip HF duration',
#                 unit='sec',
#             ),
#         ),
#         MenuItemTerms(
#             title='Water rinse required?',
#             type='terms',
#             search_quantity=f'data.water_rinse_required#{dir_path["dir15"]}',
#         ),
#         MenuItemTerms(
#             title='Spin dryer required?',
#             type='terms',
#             search_quantity=f'data.spin_dryer_required#{dir_path["dir15"]}',
#         ),
#         MenuItemHistogram(
#             title='PEB duration',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.peb_duration#{dir_path["dir15"]}',
#                 title='peb duration',
#                 unit='sec',
#             ),
#         ),
#         MenuItemHistogram(
#             title='PEB temperature',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.peb_temperature#{dir_path["dir15"]}',
#                 title='peb temperature',
#                 unit='celsius',
#             ),
#         ),
#         MenuItemHistogram(
#             title='Spin duration',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.spin_duration#{dir_path["dir15"]}',
#                 title='spin duration',
#                 unit='sec',
#             ),
#         ),
#         MenuItemHistogram(
#             title='Spin frequency',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.spin_frequency#{dir_path["dir15"]}',
#                 title='spin frequency',
#                 unit='revolutions_per_minute',
#             ),
#         ),
#         MenuItemHistogram(
#             title='Spin angular acceleration',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.spin_angular_acceleration#{dir_path["dir15"]}',
#                 title='angular acceleration',
#                 unit='rpm/sec',
#             ),
#         ),
#         MenuItemTerms(
#             title='Name equipment used',
#             type='terms',
#             search_quantity=f'data.instruments.name#{dir_path["dir15"]}',
#         ),
#         MenuItemTerms(
#             title='ID equipment used',
#             type='terms',
#             search_quantity=f'data.instruments.id#{dir_path["dir15"]}',
#         ),
#     ],
# )
# menutrans_track = Menu(
#     title='Track',
#     size='xl',
#     items=[
#         MenuItemTerms(
#             title='Lab location',
#             type='terms',
#             search_quantity=f'data.location#{dir_path["dir16"]}',
#         ),
#         MenuItemTerms(
#             title='ID item processed',
#             type='terms',
#             search_quantity=f'data.id_item_processed#{dir_path["dir16"]}',
#         ),
#         MenuItemTerms(
#             title='Name of the recipe',
#             type='terms',
#             search_quantity=f'data.recipe_name#{dir_path["dir16"]}',
#         ),
#         MenuItemTerms(
#             title='Resist name',
#             type='terms',
#             search_quantity=f'data.short_name#{dir_path["dir16"]}',
#         ),
#         MenuItemPeriodicTable(
#             title='Elements of the resist',
#             type='periodic_table',
#             search_quantity=f'{rec}#{dir_path["dir16"]}',
#         ),
#         MenuItemHistogram(
#             title='Resist thickness (target)',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.thickness_target#{dir_path["dir16"]}',
#                 title='resist thickness',
#                 unit='um',
#             ),
#         ),
#         MenuItemHistogram(
#             title='De-wetting duration',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.dewetting_duration#{dir_path["dir16"]}',
#                 title='de-wetting duration',
#                 unit='minute',
#             ),
#         ),
#         MenuItemHistogram(
#             title='De-wetting temperature',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.dewetting_temperature#{dir_path["dir16"]}',
#                 title='de-wetting temperature',
#                 unit='celsius',
#             ),
#         ),
#         MenuItemTerms(
#             title='HDMS',
#             type='terms',
#             search_quantity=f'data.hdms_required#{dir_path["dir16"]}',
#         ),
#         MenuItemTerms(
#             title='Mask set name',
#             type='terms',
#             search_quantity=f'data.mask_set_name#{dir_path["dir16"]}',
#         ),
#         MenuItemTerms(
#             title='Mask name',
#             type='terms',
#             search_quantity=f'data.mask_name#{dir_path["dir16"]}',
#         ),
#         MenuItemTerms(
#             title='Mask aligner name',
#             type='terms',
#             search_quantity=f'data.mask_aligner_name#{dir_path["dir16"]}',
#         ),
#         MenuItemTerms(
#             title='Alignment type',
#             type='terms',
#             search_quantity=f'data.alignment_type#{dir_path["dir16"]}',
#         ),
#         MenuItemTerms(
#             title='Mask target',
#             type='terms',
#             search_quantity=f'data.mask_target#{dir_path["dir16"]}',
#         ),
#         MenuItemTerms(
#             title='Exposure mask contact type',
#             type='terms',
#             search_quantity=f'data.exposure_mask_contact_type#{dir_path["dir16"]}',
#         ),
#         MenuItemHistogram(
#             title='Exposure intensity',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.exposure_intensity#{dir_path["dir16"]}',
#                 title='exposure power density',
#                 unit='mwatt/cm^2',
#             ),
#         ),
#         MenuItemHistogram(
#             title='Exposure duration',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.exposure_duration#{dir_path["dir16"]}',
#                 title='exposure duration',
#                 unit='sec',
#             ),
#         ),
#         MenuItemHistogram(
#             title='Developing duration',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.developing_duration#{dir_path["dir16"]}',
#                 title='developing duration',
#                 unit='sec',
#             ),
#         ),
#         MenuItemTerms(
#             title='PEB required?',
#             type='terms',
#             search_quantity=f'data.peb_required#{dir_path["dir16"]}',
#         ),
#         MenuItemHistogram(
#             title='PEB duration',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.peb_duration#{dir_path["dir16"]}',
#                 title='peb duration',
#                 unit='sec',
#             ),
#         ),
#         MenuItemHistogram(
#             title='PEB temperature',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.peb_temperature#{dir_path["dir16"]}',
#                 title='peb temperature',
#                 unit='celsius',
#             ),
#         ),
#         MenuItemTerms(
#             title='Softbake required?',
#             type='terms',
#             search_quantity=f'data.softbake_required#{dir_path["dir16"]}',
#         ),
#         MenuItemHistogram(
#             title='Softbake duration',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.softbake_duration#{dir_path["dir16"]}',
#                 title='softbake duration',
#                 unit='sec',
#             ),
#         ),
#         MenuItemHistogram(
#             title='Softbake temperature',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.softbake_temperature#{dir_path["dir16"]}',
#                 title='softbake temperature',
#                 unit='celsius',
#             ),
#         ),
#         MenuItemTerms(
#             title='Hardbake required?',
#             type='terms',
#             search_quantity=f'data.hardbake_required#{dir_path["dir16"]}',
#         ),
#         MenuItemHistogram(
#             title='Hardbake duration',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.hardbake_duration#{dir_path["dir16"]}',
#                 title='hardbake duration',
#                 unit='sec',
#             ),
#         ),
#         MenuItemHistogram(
#             title='Hardbake temperature',
#             type='histogram',
#             n_bins=10,
#             x=Axis(
#                 search_quantity=f'data.hardbake_temperature#{dir_path["dir16"]}',
#                 title='hardbake temperature',
#                 unit='celsius',
#             ),
#         ),
#         MenuItemTerms(
#             title='Name equipment used',
#             type='terms',
#             search_quantity=f'data.instruments.name#{dir_path["dir16"]}',
#         ),
#         MenuItemTerms(
#             title='ID equipment used',
#             type='terms',
#             search_quantity=f'data.instruments.id#{dir_path["dir16"]}',
#         ),
#     ],
# )
menuadd_electrongun = Menu(
    title='Electron Gun',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir17"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir17"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir17"]}',
        ),
        MenuItemHistogram(
            title='Thickness target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir17"]}',
                title='thickness',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Duration target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir17"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Target material',
            type='terms',
            search_quantity=f'data.deposition_steps.material_deposited.name#{dir_path["dir17"]}',
        ),
        MenuItemTerms(
            title='Target material formula',
            type='terms',
            search_quantity=f'data.deposition_steps.material_deposited.chemical_formula#{dir_path["dir17"]}',
        ),
        MenuItemTerms(
            title='Target material',
            type='periodic_table',
            search_quantity=f'data.deposition_steps.material_deposited.elemental_composition.element#{dir_path["dir17"]}',
        ),
        MenuItemTerms(
            title='Wafer stack name',
            type='terms',
            search_quantity=f'data.deposition_steps.wafer_stack_name#{dir_path["dir17"]}',
        ),
        MenuItemHistogram(
            title='Deposition chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.deposition_steps.chamber_pressure#{dir_path["dir17"]}',
                title='chamber pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Spin frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.deposition_steps.spin_parameters.spin_frequency#{dir_path["dir17"]}',
                title='frequency',
                unit='rpm',
            ),
        ),
        MenuItemHistogram(
            title='Duration measured',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir17"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Gun voltage measured',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.gun_voltage_measured#{dir_path["dir17"]}',
                title='gun voltage',
                unit='V',
            ),
        ),
        MenuItemHistogram(
            title='Gun current measured',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.gun_current_measured#{dir_path["dir17"]}',
                title='gun current',
                unit='mampere',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir17"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir17"]}',
        ),
    ],
)
menuadd_sputtering = Menu(
    title='Sputtering',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir18"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir18"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir18"]}',
        ),
        MenuItemHistogram(
            title='Desired thickness',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir18"]}',
                title='thickness target',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Duration target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir18"]}',
                title='duration target',
                unit='nm/minute',
            ),
        ),
        MenuItemHistogram(
            title='Deposition rate target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.deposition_rate_target#{dir_path["dir18"]}',
                title='deposition rate',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Material target name',
            type='terms',
            search_quantity=f'data.sputtering_steps.material_deposited.name#{dir_path["dir18"]}',
        ),
        MenuItemTerms(
            title='Material target formula',
            type='terms',
            search_quantity=f'data.sputtering_steps.material_deposited.chemical_formula#{dir_path["dir18"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements deposited',
            type='periodic_table',
            search_quantity=f'data.sputtering_steps.material_deposited.elemental_composition.element#{dir_path["dir18"]}',
        ),
        MenuItemTerms(
            title='Item movement',
            type='terms',
            search_quantity=f'data.sputtering_steps.item_movement#{dir_path["dir18"]}',
        ),
        MenuItemHistogram(
            title='Movement frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.sputtering_steps.movement_frequency#{dir_path["dir18"]}',
                title='frequency',
                unit='Hz',
            ),
        ),
        MenuItemHistogram(
            title='Spin frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.sputtering_steps.spin_parameters.spin_frequency#{dir_path["dir18"]}',
                title='frequency',
                unit='revolutions_per_minute',
            ),
        ),
        MenuItemHistogram(
            title='Spin angular acceleration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.sputtering_steps.spin_parameters.spin_angular_acceleration#{dir_path["dir18"]}',
                title='angular acceleration',
                unit='revolutions_per_minute/sec',
            ),
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.sputtering_steps.chuck.chuck_temperature#{dir_path["dir18"]}',
                title='chuck temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Sputterer power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.sputtering_steps.power#{dir_path["dir18"]}',
                title='power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='Delay between stack layers',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.sputtering_steps.delay_between_stack_layers#{dir_path["dir18"]}',
                title='delay between stack layers',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir18"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir18"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir18"]}',
        ),
    ],
)
menuadd_sog = Menu(
    title='SOG',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir19"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir19"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir19"]}',
        ),
        MenuItemHistogram(
            title='Target thickness',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.thickness_target#{dir_path["dir19"]}',
                title='thickness target',
                unit='um',
            ),
        ),
        MenuItemTerms(
            title='Substrate material',
            type='terms',
            search_quantity=f'data.sog_steps.substrate_material.name#{dir_path["dir19"]}',
        ),
        MenuItemTerms(
            title='Substrate material formula',
            type='terms',
            search_quantity=f'data.sog_steps.substrate_material.chemical_formula#{dir_path["dir19"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the substrate',
            type='periodic_table',
            search_quantity=f'data.sog_steps.substrate_material.elemental_composition.element#{dir_path["dir19"]}',
        ),
        MenuItemTerms(
            title='Pre-cleaning method',
            type='terms',
            search_quantity=f'data.sog_steps.pre_cleaning#{dir_path["dir19"]}',
        ),
        MenuItemHistogram(
            title='De-wetting duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.sog_steps.dewetting_duration#{dir_path["dir19"]}',
                title='de-wetting duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='De-wetting temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.sog_steps.dewetting_temperature#{dir_path["dir19"]}',
                title='de-wetting temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Spin frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.sog_steps.spin_parameters.spin_frequency#{dir_path["dir19"]}',
                title='frequency',
                unit='revolutions_per_minute',
            ),
        ),
        MenuItemHistogram(
            title='Spin angular acceleration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.sog_steps.spin_parameters.spin_angular_acceleration#{dir_path["dir19"]}',
                title='angular acceleration',
                unit='revolutions_per_minute/sec',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir19"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir19"]}',
        ),
    ],
)
menuremove_rie = Menu(
    title='RIE',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir20"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir20"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir20"]}',
        ),
        MenuItemHistogram(
            title='Desired depth',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_target#{dir_path["dir20"]}',
                title='depth target',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Desired duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir20"]}',
                title='duration target',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Desired etching rate',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_rate_target#{dir_path["dir20"]}',
                title='etching rate target',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Kind of step',
            type='terms',
            search_quantity=f'data.etching_steps.tag#{dir_path["dir20"]}',
        ),
        MenuItemTerms(
            title='Material to be etched',
            type='terms',
            search_quantity=f'data.etching_steps.materials_etched.name#{dir_path["dir20"]}',
        ),
        MenuItemTerms(
            title='Formulas of the etched material',
            type='terms',
            search_quantity=f'data.etching_steps.materials_etched.chemical_formula#{dir_path["dir20"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements etched',
            type='periodic_table',
            search_quantity=f'data.etching_steps.{meec}#{dir_path["dir20"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of gases employed',
            type='periodic_table',
            search_quantity=f'{fluxetch}#{dir_path["dir20"]}',
        ),
        MenuItemTerms(
            title='Gases formulas',
            type='terms',
            search_quantity=f'data.etching_steps.fluximeters.chemical_formula#{dir_path["dir20"]}',
        ),
        MenuItemTerms(
            title='Gases name',
            type='terms',
            search_quantity=f'data.etching_steps.fluximeters.name#{dir_path["dir20"]}',
        ),
        MenuItemHistogram(
            title='Gases fluxes',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.fluximeters.massflow#{dir_path["dir20"]}',
                unit='centimeter^3/minute',
            ),
        ),
        MenuItemHistogram(
            title='Chamber temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chamber_temperature#{dir_path["dir20"]}',
                title='chamber temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chamber_pressure#{dir_path["dir20"]}',
                title='chamber pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.chuck_temperature#{dir_path["dir20"]}'
                ),
                title='chuck temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Chuck Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.chuck_power#{dir_path["dir20"]}'
                ),
                title='chuck power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='Chuck high frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.chuck_high_frequency#{dir_path["dir20"]}'
                ),
                title='chuck high frequency',
                unit='MHz',
            ),
        ),
        MenuItemHistogram(
            title='Chuck low frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.chuck_low_frequency#{dir_path["dir20"]}'
                ),
                title='chuck low frequency',
                unit='MHz',
            ),
        ),
        MenuItemHistogram(
            title='Bias voltage',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(f'data.etching_steps.chuck.bias#{dir_path["dir20"]}'),
                title='bias voltage',
                unit='V',
            ),
        ),
        MenuItemTerms(
            title='Clamping',
            type='terms',
            search_quantity=(
                f'data.etching_steps.chuck.clamping.clamping_type#{dir_path["dir20"]}'
            ),
        ),
        MenuItemHistogram(
            title='Clamping pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.clamping.clamping_pressure#{dir_path["dir20"]}'
                ),
                title='clamping pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir20"]}',
                title='duration measured',
                unit='sec',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir20"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir20"]}',
        ),
    ],
)
menuremove_wetetching = Menu(
    title='Wet Etching',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='Etching type',
            type='terms',
            search_quantity=f'data.etching_steps.tag#{dir_path["dir21"]}',
        ),
        MenuItemHistogram(
            title='Desired depth',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_target#{dir_path["dir21"]}',
                title='depth target',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Desired duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir21"]}',
                title='duration target',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Etching rate target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_rate_target#{dir_path["dir21"]}',
                title='etching rate target',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Material to be etched',
            type='terms',
            search_quantity=f'data.etching_steps.materials_etched.name#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='Formulas of the etched material',
            type='terms',
            search_quantity=(
                f'data.etching_steps.materials_etched.chemical_formula#{dir_path["dir21"]}'
            ),
        ),
        MenuItemPeriodicTable(
            title='Elements of the material',
            type='periodic_table',
            search_quantity=f'data.etching_steps.{meec}#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='Etching reactives',
            type='terms',
            search_quantity=f'{ru}.name#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='Formula of the reactives used to etch',
            type='terms',
            search_quantity=f'{ru}.chemical_formula#{dir_path["dir21"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the etching compounds',
            type='periodic_table',
            search_quantity=f'{rute}#{dir_path["dir21"]}',
        ),
        MenuItemHistogram(
            title='Etching reactives final concentration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'{ru}.solution_concentration#{dir_path["dir21"]}',
                title='etching reactives concentration(%)',
            ),
        ),
        MenuItemTerms(
            title='Wetting required',
            type='terms',
            search_quantity=f'data.etching_steps.wetting#{dir_path["dir21"]}',
        ),
        MenuItemHistogram(
            title='Etching temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.tank_temperature#{dir_path["dir21"]}',
                title='etching temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Resistivity cut off',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.resistivity_control.resistivity_target#{dir_path["dir21"]}',
                title='resistivity cut off',
                unit='ohm*cm',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir21"]}',
                title='duration measured',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir21"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir21"]}',
        ),
    ],
)
menuremove_stripping = Menu(
    title='Stripping',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir22"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir22"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir22"]}',
        ),
        MenuItemTerms(
            title='Stripping type',
            type='terms',
            search_quantity=f'data.stripping_steps.stripping_type#{dir_path["dir22"]}',
        ),
        MenuItemTerms(
            title='Resist to remove',
            type='terms',
            search_quantity=f'data.stripping_steps.resist_to_strip.name#{dir_path["dir22"]}',
        ),
        MenuItemTerms(
            title='Resist chemical formula',
            type='terms',
            search_quantity=f'data.stripping_steps.resist_to_strip.chemical_formula#{dir_path["dir22"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the resist',
            type='periodic_table',
            search_quantity=f'data.stripping_steps.resist_to_strip.elemental_composition.element#{dir_path["dir22"]}',
        ),
        MenuItemHistogram(
            title='Removing temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.stripping_steps.removing_temperature#{dir_path["dir22"]}',
                title='removing temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Ultrasound required?',
            type='terms',
            search_quantity=f'data.stripping_steps.ultrasound_required#{dir_path["dir22"]}',
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir22"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir22"]}',
        ),
    ],
)
menuremove_spinresist = Menu(
    title='Spin resist development',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir29"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir29"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir29"]}',
        ),
        MenuItemTerms(
            title='Mode',
            type='terms',
            search_quantity=f'data.development_steps.developing_mode#{dir_path["dir29"]}',
        ),
        MenuItemHistogram(
            title='Developing temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.development_steps.developing_temperature#{dir_path["dir29"]}',
                title='developing temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Name of the material developed',
            type='terms',
            search_quantity=f'data.development_steps.materials_developed.name#{dir_path["dir29"]}',
        ),
        MenuItemTerms(
            title='Formula of the material developed',
            type='terms',
            search_quantity=f'data.development_steps.materials_developed.chemical_formula#{dir_path["dir29"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of the material developed',
            type='periodic_table',
            search_quantity=f'data.development_steps.materials_developed.elemental_composition.element#{dir_path["dir29"]}',
        ),
        MenuItemTerms(
            title='Name of the developing solution components',
            type='terms',
            search_quantity=f'data.development_steps.developing_solution.developing_solution_components.name#{dir_path["dir29"]}',
        ),
        MenuItemHistogram(
            title='Developer dispensed volume',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.development_steps.developing_solution.dispensed_volume#{dir_path["dir29"]}',
                title='dispensed volume',
                unit='milliliter',
            ),
        ),
        MenuItemTerms(
            title='Name of the surfactant in the solution',
            type='terms',
            search_quantity=f'data.development_steps.developing_solution.surfactants.name#{dir_path["dir29"]}',
        ),
        MenuItemHistogram(
            title='Spin frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.development_steps.spin_parameters.spin_frequency#{dir_path["dir29"]}',
                title='spin frequency',
                unit='revolutions_per_minute',
            ),
        ),
        MenuItemHistogram(
            title='Spin angular acceleration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.development_steps.spin_parameters.spin_angular_acceleration#{dir_path["dir29"]}',
                title='spin angular acceleration',
                unit='revolutions_per_minute/sec',
            ),
        ),
        MenuItemTerms(
            title='Rinsing mode',
            type='terms',
            search_quantity=f'data.development_steps.final_rinsing.rinsing_mode#{dir_path["dir29"]}',
        ),
        MenuItemTerms(
            title='Rinser name',
            type='terms',
            search_quantity=f'data.development_steps.final_rinsing.rinser_name#{dir_path["dir29"]}',
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir29"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir29"]}',
        ),
    ],
)
menuremove_rinsingdrying = Menu(
    title='Rinsing drying',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir30"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir30"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir30"]}',
        ),
        MenuItemTerms(
            title='Rinsing mode',
            type='terms',
            search_quantity=f'data.rinsing_drying_steps.initial_rinsing_parameters.rinsing_mode#{dir_path["dir30"]}',
        ),
        MenuItemHistogram(
            title='Resistivity cut-off',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.rinsing_drying_steps.initial_rinsing_parameters.resistivity_control.resistivity_target#{dir_path["dir30"]}',
                title='resistivity cut off',
                unit='ohm*cm',
            ),
        ),
        MenuItemHistogram(
            title='Rinsing spin frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.rinsing_drying_steps.initial_rinsing_parameters.spinning_parameters.spin_frequency#{dir_path["dir30"]}',
                title='spin frequency',
                unit='revolutions_per_minute',
            ),
        ),
        MenuItemHistogram(
            title='Rinsing spin angular acceleration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.rinsing_drying_steps.initial_rinsing_parameters.spinning_parameters.spin_angular_acceleration#{dir_path["dir30"]}',
                title='spin angular acceleration',
                unit='revolutions_per_minute/sec',
            ),
        ),
        MenuItemTerms(
            title='Drying mode',
            type='terms',
            search_quantity=f'data.rinsing_drying_steps.drying_parameters.drying_mode#{dir_path["dir30"]}',
        ),
        MenuItemHistogram(
            title='Drying temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.rinsing_drying_steps.drying_parameters.drying_temperature#{dir_path["dir30"]}',
                title='temperature',
                unit='celsius',
            ),
        ),
        MenuItemTerms(
            title='Drying gas name',
            type='terms',
            search_quantity=f'data.rinsing_drying_steps.drying_parameters.drying_gas.name#{dir_path["dir30"]}',
        ),
        MenuItemTerms(
            title='Drying gas formula',
            type='terms',
            search_quantity=f'data.rinsing_drying_steps.drying_parameters.drying_gas.chemical_formula#{dir_path["dir30"]}',
        ),
        MenuItemHistogram(
            title='Drying gas flow',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.rinsing_drying_steps.drying_parameters.drying_gas.massflow#{dir_path["dir30"]}',
                title='massflow',
                unit='centimeter^3/minute',
            ),
        ),
        MenuItemHistogram(
            title='Drying gas temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.rinsing_drying_steps.drying_parameters.drying_gas.gas_temperature#{dir_path["dir30"]}',
                title='temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Drying spin frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.rinsing_drying_steps.drying_parameters.spinning_parameters.spin_frequency#{dir_path["dir30"]}',
                title='spin frequency',
                unit='revolutions_per_minute',
            ),
        ),
        MenuItemHistogram(
            title='Drying spin angular acceleration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.rinsing_drying_steps.drying_parameters.spinning_parameters.spin_angular_acceleration#{dir_path["dir30"]}',
                title='spin angular acceleration',
                unit='revolutions_per_minute/sec',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir30"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir30"]}',
        ),
    ],
)
menuutils_obsmeasurements = Menu(
    title='Observation Measurements',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='Equipment used',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='Activity type',
            type='terms',
            search_quantity=f'data.activity_type#{dir_path["dir23"]}',
        ),
        MenuItemHistogram(
            title='Target duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir23"]}',
                title='duration target',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Image name',
            type='terms',
            search_quantity=f'data.image_name#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='Thickness measurements',
            type='terms',
            search_quantity=f'data.thickness_measurements#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='Electrical measurements',
            type='terms',
            search_quantity=f'data.electrical_measurements#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir23"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir23"]}',
        ),
    ],
)
menuutils_startingmaterial = Menu(
    title='Starting Material',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir24"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir24"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir24"]}',
        ),
        MenuItemTerms(
            title='Wafer material (short name)',
            type='terms',
            search_quantity=f'data.short_name#{dir_path["dir24"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements in the wafer',
            type='periodic_table',
            search_quantity=f'data.elemental_composition.element#{dir_path["dir24"]}',
        ),
        MenuItemTerms(
            title='Manufacturer name',
            type='terms',
            search_quantity=f'data.manufacturer_name#{dir_path["dir24"]}',
        ),
        MenuItemHistogram(
            title='Wafer quantity',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.wafer_quantity#{dir_path["dir24"]}',
                title='quantity',
            ),
        ),
        MenuItemHistogram(
            title='Wafer resistivity',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.wafer_resistivity#{dir_path["dir24"]}',
                title='wafer resistivity',
                unit='ohm*cm',
            ),
        ),
        MenuItemTerms(
            title='Wafer orientation',
            type='terms',
            search_quantity=f'data.wafer_orientation#{dir_path["dir24"]}',
        ),
        MenuItemHistogram(
            title='Wafer thickness',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.wafer_thickness#{dir_path["dir24"]}',
                title='wafer thickness',
                unit='um',
            ),
        ),
        MenuItemTerms(
            title='Wafer surface finish',
            type='terms',
            search_quantity=f'data.wafer_surface_finish#{dir_path["dir24"]}',
        ),
        MenuItemHistogram(
            title='Wafer diameter',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.wafer_diameter#{dir_path["dir24"]}',
                title='wafer diameter',
                unit='mm',
            ),
        ),
        MenuItemTerms(
            title='Wafer doping',
            type='terms',
            search_quantity=f'data.wafer_doping#{dir_path["dir24"]}',
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir24"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir24"]}',
        ),
    ],
)
menutrans_baking = Menu(
    title='Baking',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir25"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir25"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir25"]}',
        ),
        MenuItemTerms(
            title='Baking type',
            type='terms',
            search_quantity=f'data.baking_steps.tag#{dir_path["dir25"]}',
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.baking_steps.baking_temperature#{dir_path["dir25"]}',
                title='temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.baking_steps.duration#{dir_path["dir25"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir25"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir25"]}',
        ),
    ],
)

menuremove_driebosch = Menu(
    title='DRIE BOSCH',
    size='xl',
    items=[
        MenuItemTerms(
            title='Lab location',
            type='terms',
            search_quantity=f'data.location#{dir_path["dir26"]}',
        ),
        MenuItemTerms(
            title='ID item processed',
            type='terms',
            search_quantity=f'data.id_item_processed#{dir_path["dir26"]}',
        ),
        MenuItemTerms(
            title='Name of the recipe',
            type='terms',
            search_quantity=f'data.recipe_name#{dir_path["dir26"]}',
        ),
        MenuItemHistogram(
            title='Desired depth',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.depth_target#{dir_path["dir26"]}',
                title='depth',
                unit='nm',
            ),
        ),
        MenuItemHistogram(
            title='Required duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.duration_target#{dir_path["dir26"]}',
                title='duration',
                unit='minute',
            ),
        ),
        MenuItemHistogram(
            title='Etching rate target',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_rate_target#{dir_path["dir26"]}',
                title='etching rate target',
                unit='nm/minute',
            ),
        ),
        MenuItemTerms(
            title='Kind of step',
            type='terms',
            search_quantity=f'data.etching_steps.tag#{dir_path["dir26"]}',
        ),
        MenuItemTerms(
            title='Material to be etched',
            type='terms',
            search_quantity=f'data.etching_steps.materials_etched.name#{dir_path["dir26"]}',
        ),
        MenuItemTerms(
            title='Formulas of the etched material',
            type='terms',
            search_quantity=f'data.etching_steps.materials_etched.chemical_formula#{dir_path["dir26"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements etched',
            type='periodic_table',
            search_quantity=f'data.etching_steps.{meec}#{dir_path["dir26"]}',
        ),
        MenuItemPeriodicTable(
            title='Elements of gases employed',
            type='periodic_table',
            search_quantity=f'{fluxetch}#{dir_path["dir26"]}',
        ),
        MenuItemTerms(
            title='Gases formulas',
            type='terms',
            search_quantity=f'data.etching_steps.fluximeters.chemical_formula#{dir_path["dir26"]}',
        ),
        MenuItemTerms(
            title='Gases name',
            type='terms',
            search_quantity=f'data.etching_steps.fluximeters.name#{dir_path["dir26"]}',
        ),
        MenuItemHistogram(
            title='Gases fluxes',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.fluximeters.massflow#{dir_path["dir26"]}',
                unit='centimeter^3/minute',
            ),
        ),
        MenuItemHistogram(
            title='Chamber temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chamber_temperature#{dir_path["dir26"]}',
                title='chamber temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Chamber pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.etching_steps.chamber_pressure#{dir_path["dir26"]}',
                title='chamber pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Chuck temperature',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.chuck_temperature#{dir_path["dir26"]}'
                ),
                title='chuck temperature',
                unit='celsius',
            ),
        ),
        MenuItemHistogram(
            title='Chuck high phase power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.high_chuck_power#{dir_path["dir26"]}'
                ),
                title='chuck high phase power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='Chuck low phase power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.low_chuck_power#{dir_path["dir26"]}'
                ),
                title='chuck low phase power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='Chuck high phase duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.high_chuck_power_duration#{dir_path["dir26"]}'
                ),
                title='chuck high phase duration',
                unit='sec',
            ),
        ),
        MenuItemHistogram(
            title='Chuck low phase duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.low_chuck_power_duration#{dir_path["dir26"]}'
                ),
                title='chuck low phase duration',
                unit='sec',
            ),
        ),
        MenuItemHistogram(
            title='Chuck high frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.chuck_high_frequency#{dir_path["dir26"]}'
                ),
                title='chuck high frequency',
                unit='MHz',
            ),
        ),
        MenuItemHistogram(
            title='Chuck low frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.chuck_low_frequency#{dir_path["dir26"]}'
                ),
                title='chuck low frequency',
                unit='MHz',
            ),
        ),
        MenuItemHistogram(
            title='Bias voltage',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(f'data.etching_steps.chuck.bias#{dir_path["dir26"]}'),
                title='bias voltage',
                unit='V',
            ),
        ),
        MenuItemHistogram(
            title='ICP Power',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.icp_column.icp_power#{dir_path["dir26"]}'
                ),
                title='icp power',
                unit='watt',
            ),
        ),
        MenuItemHistogram(
            title='ICP Frequency',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.icp_column.icp_frequency#{dir_path["dir26"]}'
                ),
                title='icp frequency',
                unit='MHz',
            ),
        ),
        MenuItemTerms(
            title='Clamping',
            type='terms',
            search_quantity=(
                f'data.etching_steps.chuck.clamping.clamping_type#{dir_path["dir26"]}'
            ),
        ),
        MenuItemHistogram(
            title='Clamping pressure',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=(
                    f'data.etching_steps.chuck.clamping.clamping_pressure#{dir_path["dir26"]}'
                ),
                title='clamping pressure',
                unit='mbar',
            ),
        ),
        MenuItemHistogram(
            title='Effective duration',
            type='histogram',
            n_bins=10,
            x=Axis(
                search_quantity=f'data.outputs.duration_measured#{dir_path["dir26"]}',
                title='effective duration',
                unit='minute',
            ),
        ),
        MenuItemTerms(
            title='Name equipment used',
            type='terms',
            search_quantity=f'data.instruments.name#{dir_path["dir26"]}',
        ),
        MenuItemTerms(
            title='ID equipment used',
            type='terms',
            search_quantity=f'data.instruments.id#{dir_path["dir26"]}',
        ),
    ],
)
