from nomad.config.models.plugins import SchemaPackageEntryPoint


class BondingEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.add.integration.bonding import m_package

        return m_package


Bonding_entry_point = BondingEntryPoint(
    name='Bonding steps definitions',
    description='Schema package for describing bonding steps in fabrication.',
)
