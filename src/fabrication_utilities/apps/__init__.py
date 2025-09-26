from apps.addapp import addapp
from apps.equipmentapp import equipmentapp
from apps.material import materialapp
from apps.processapp import processapp
from apps.removeapp import removeapp
from apps.transapp import transapp
from nomad.config.models.plugins import AppEntryPoint

equipment_app_entry_point = AppEntryPoint(
    name='Fabrication_equipment_search',
    description='New app for equipment of fabrication facilities.',
    app=equipmentapp,
)

process_app_entry_point = AppEntryPoint(
    name='Fabrication_process_search',
    description='New app for equipment of fabrication facilities.',
    app=processapp,
)

app_remove_entry_point = AppEntryPoint(
    name='Remove steps research app',
    description='App for searching remove steps like etching, drying, etc.',
    app=removeapp,
)

app_add_entry_point = AppEntryPoint(
    name='Add steps research app',
    description='App for researching add steps like synthesis, bonding, etc.',
    app=addapp,
)

app_trans_entry_point = AppEntryPoint(
    name='Transform steps research app',
    description='App for searching transform steps like lithography, oxydation, etc.',
    app=transapp,
)

app_material_entry_point = AppEntryPoint(
    name='Materials research app',
    description='App for searching materials employed in fabrication',
    app=materialapp,
)

app_entry_point_to_test = app_remove_entry_point
