from nomad.config.models.plugins import SchemaPackageEntryPoint


class DicingEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.transform.dicing.dicing import m_package

        return m_package


Dicing_entry_point = DicingEntryPoint(
    name='Dicing steps definitions',
    description='Schema package for describing dicing steps in fabrication.',
)
