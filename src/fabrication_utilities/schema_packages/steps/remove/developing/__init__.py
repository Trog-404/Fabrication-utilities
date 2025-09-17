from nomad.config.models.plugins import SchemaPackageEntryPoint


class DevelopEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.remove.developing.development import m_package

        return m_package


develop_entry_point = DevelopEntryPoint(
    name='Developing steps definitions',
    description='Schema package for describing developing steps in fabrication.',
)
