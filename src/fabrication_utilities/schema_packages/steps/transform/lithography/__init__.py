from nomad.config.models.plugins import SchemaPackageEntryPoint


class EBLEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.transform.lithography.ebl import m_package

        return m_package


EBL_entry_point = EBLEntryPoint(
    name='EBL steps definitions',
    description='Schema package for describing ebl steps in fabrication.',
)


class FIBEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.transform.lithography.fib import m_package

        return m_package


FIB_entry_point = FIBEntryPoint(
    name='FIB steps definitions',
    description='Schema package for describing fib steps in fabrication.',
)


class LabelingEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from schema_packages.steps.transform.lithography.labeling import m_package

        return m_package


Labeling_entry_point = LabelingEntryPoint(
    name='Labeling steps definitions',
    description='Schema package for describing labeling steps in fabrication.',
)
