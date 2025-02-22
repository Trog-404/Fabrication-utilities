from nomad.config.models.plugins import AppEntryPoint
from fabrication_facilities.apps.equipmentapp import equipmentapp

equipment_app_entry_point = AppEntryPoint(
    name='Fabrication_equipment_search',
    description='New app for equipment of fabrication facilities.',
    app=equipmentapp,
)
