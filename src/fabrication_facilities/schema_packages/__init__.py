from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class NewSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from fabrication_facilities.schema_packages.schema_package import m_package

        return m_package


schema_package_entry_point = NewSchemaPackageEntryPoint(
    name='NewSchemaPackage',
    description='New schema package entry point configuration.',
)


class ItemsEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from fabrication_facilities.schema_packages.Items import m_package

        return m_package


Items_entry_point = ItemsEntryPoint(
    name='FabricationItems',
    description='Schema package for describing items in fabrications.',
)


class EquipmentEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from fabrication_facilities.schema_packages.equipment import m_package

        return m_package


Equipment_entry_point = EquipmentEntryPoint(
    name='FabricationEquipments',
    description='Schema package for describing equipments in fabrications.',
)


class StepsEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from fabrication_facilities.schema_packages.fabrication_steps import m_package

        return m_package


Steps_entry_point = StepsEntryPoint(
    name='FabricationBaseSteps',
    description='Schema package for describing base steps in fabrications.',
)


class AddEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from fabrication_facilities.schema_packages.add import m_package

        return m_package


Add_entry_point = AddEntryPoint(
    name='Add processes',
    description='Schema package for describing add steps in fabrications.',
)


class TransformEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from fabrication_facilities.schema_packages.transform import m_package

        return m_package


Transform_entry_point = TransformEntryPoint(
    name='Transoform processes',
    description='Schema package for describing transform steps in fabrications.',
)


class RemoveEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from fabrication_facilities.schema_packages.remove import m_package

        return m_package


Remove_entry_point = RemoveEntryPoint(
    name='Add processes',
    description='Schema package for describing add steps in fabrications.',
)
