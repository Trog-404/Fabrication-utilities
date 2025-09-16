from nomad.config.models.plugins import SchemaPackageEntryPoint


class ItemsEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.Items import m_package

        return m_package


Items_entry_point = ItemsEntryPoint(
    name='FabricationItems',
    description='Schema package for describing items in fabrications.',
)


class UtilitiesEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.fabrication_utilities import (
            m_package,
        )

        return m_package


Utilities_entry_point = UtilitiesEntryPoint(
    name='FabricationBaseExtension',
    description='Schema package for describing base classes and steps in fabrication.',
)


# class TransformEntryPoint(SchemaPackageEntryPoint):
#    def load(self):
#        from schema_packages.steps.transform import m_package
#
#        return m_package
#
#
# Transform_entry_point = TransformEntryPoint(
#    name='Transoform processes',
#    description='Schema package for describing transform steps in fabrications.',
# )


class CharacterizationEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.character import m_package

        return m_package


Characterization_entry_point = CharacterizationEntryPoint(
    name='Characterization steps',
    description='Schema package for describing charac steps in fabrications.',
)


class CharacterizationEquipmentEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.equipments.character_equipment import (
            m_package,
        )

        return m_package


Characterization_Equipment_entry_point = CharacterizationEquipmentEntryPoint(
    name='Characterization tools',
    description="""
        Schema package to describe characterization tools used in fabrications to
         control process steps.'
    """,
)


class EquipmentsEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.equipments.equipments import (
            m_package,
        )

        return m_package


Equipments_entry_point = EquipmentsEntryPoint(
    name='FabricationEquipments',
    description='Schema package for describing various equipments for fabrication.',
)


class MaterialEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.materials import (
            m_package,
        )

        return m_package


materials_entry_point = MaterialEntryPoint(
    name='Fabrication Materials',
    description='Schema package for describing various raw materials properties.',
)


class AnalysisEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.calculus.calculus import (
            m_package,
        )

        return m_package


calculus_entry_point = AnalysisEntryPoint(
    name='Analysis sheets',
    description='Schema package for describing various analysis needed in CR.',
)
