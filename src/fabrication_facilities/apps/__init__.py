from nomad.config.models.plugins import AppEntryPoint
from fabrication_facilities.apps.equipmentapp import equipmentapp
from fabrication_facilities.apps.removeapp import processapp

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
