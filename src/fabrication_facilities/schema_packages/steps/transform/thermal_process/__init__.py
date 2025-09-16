from nomad.config.models.plugins import SchemaPackageEntryPoint


class BakingEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.transform.thermal_process.baking import m_package

        return m_package


Baking_entry_point = BakingEntryPoint(
    name='Baking steps definitions',
    description='Schema package for describing baking steps in fabrication.',
)


class OxidationEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.transform.thermal_process.thermal_oxidation import (
            m_package,
        )

        return m_package


ThermalOxidation_entry_point = OxidationEntryPoint(
    name='Thermal oxidation steps definitions',
    description='Schema package for describing thermal oxidation steps in fabrication.',
)
