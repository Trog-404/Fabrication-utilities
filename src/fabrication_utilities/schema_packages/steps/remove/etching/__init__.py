from nomad.config.models.plugins import SchemaPackageEntryPoint


class DryEtchEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.remove.etching.dry_etching import m_package

        return m_package


dryetch_entry_point = DryEtchEntryPoint(
    name='Dry etching steps definitions',
    description='Schema package for describing dry etching steps in fabrication.',
)


class WetEtchEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.remove.etching.wet_etching import m_package

        return m_package


wetetch_entry_point = WetEtchEntryPoint(
    name='Wet etching steps definitions',
    description='Schema package for describing wet etching steps in fabrication.',
)


class StripEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.remove.etching.stripping import m_package

        return m_package


strip_entry_point = StripEntryPoint(
    name='Stripping steps definitions',
    description='Schema package for describing stripping steps in fabrication.',
)
