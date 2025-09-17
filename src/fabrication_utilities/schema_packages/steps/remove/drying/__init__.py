from nomad.config.models.plugins import SchemaPackageEntryPoint


class DryingEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.remove.drying.drying import m_package

        return m_package


drying_entry_point = DryingEntryPoint(
    name='Developing steps definitions',
    description='Schema package for describing drying steps in fabrication.',
)
