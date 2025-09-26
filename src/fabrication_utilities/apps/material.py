from nomad.config.models.ui import (
    App,
    Axis,
    Column,
    Menu,
    MenuItemCustomQuantities,
    MenuItemHistogram,
    MenuItemPeriodicTable,
    MenuItemTerms,
    SearchQuantities,
)

dir0 = 'schema_packages.materials.MaterialProductionProcess'

materialapp = App(
    label='Raw materials',
    path='materialsapp',
    category='Fabrication utilities',
    description='App to search fabrication materials.',
    readme="""
    This research app allows to search general information about fabrication processes
    involved in the characterization of raw materials crucial in fabrications.
    """,
    search_quantities=SearchQuantities(include=[f'*#{dir0}']),
    columns=[
        Column(quantity='entry_name', selected=True),
        Column(quantity='entry_type'),
        Column(
            quantity=f'data.affiliation#{dir0}',
            selected=True,
        ),
        Column(
            quantity=f'data.id_proposal#{dir0}',
            selected=True,
        ),
        Column(
            quantity=f'data.generic_product_name#{dir0}',
            selected=True,
        ),
        Column(
            quantity=f'data.id_item_processed#{dir0}',
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
                title='ID proposal',
                type='terms',
                search_quantity=f'data.id_proposal#{dir0}',
            ),
            MenuItemTerms(
                title='Product Type',
                type='terms',
                search_quantity=f'data.generic_product_name#{dir0}',
            ),
            MenuItemTerms(
                title='Author',
                type='terms',
                search_quantity=f'data.author#{dir0}',
            ),
            Menu(
                title='Material properties',
                size='xl',
                items=[
                    MenuItemTerms(
                        title='Material name',
                        type='terms',
                        search_quantity=f'data.output.name#{dir0}',
                    ),
                    MenuItemTerms(
                        title='Material name',
                        type='terms',
                        search_quantity=f'data.output.location#{dir0}',
                    ),
                    MenuItemTerms(
                        title='Material chemical formula',
                        type='terms',
                        search_quantity=f'data.output.chemical_components.chemical_formula#{dir0}',
                    ),
                    MenuItemPeriodicTable(
                        title='Material elemental composition',
                        type='periodic_table',
                        search_quantity=f'data.output.chemical_components.elemental_composition.element#{dir0}',
                    ),
                    MenuItemHistogram(
                        title='Etching rate measured',
                        type='histogram',
                        n_bins=10,
                        x=Axis(
                            title='etching rate',
                            search_quantity=f'data.output.etching_properties.etching_results.etching_rate_measured#{dir0}',
                            unit='nm/minute',
                        ),
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
