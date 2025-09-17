from nomad.config.models.plugins import SchemaPackageEntryPoint


class CVDsEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.add.synthesis.CVD import m_package

        return m_package


CVDs_entry_point = CVDsEntryPoint(
    name='CVDs steps definitions',
    description='Schema package for describing cvd steps in fabrication.',
)


class CoatingEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.add.synthesis.coating import m_package

        return m_package


Coating_entry_point = CoatingEntryPoint(
    name='Coating steps definitions',
    description='Schema package for describing coating steps in fabrication.',
)


class ElectronGunEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.add.synthesis.electron_gun import m_package

        return m_package


ElectronGun_entry_point = ElectronGunEntryPoint(
    name='Electron gun steps definitions',
    description='Schema package for describing electron gun steps in fabrication.',
)


class SputteringEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.add.synthesis.sputtering import m_package

        return m_package


Sputtering_entry_point = SputteringEntryPoint(
    name='Sputtering steps definitions',
    description='Schema package for describing sputtering steps in fabrication.',
)


class SOGEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.add.synthesis.sog import m_package

        return m_package


SOG_entry_point = SOGEntryPoint(
    name='SOG steps definitions',
    description='Schema package for describing sog steps in fabrication.',
)
