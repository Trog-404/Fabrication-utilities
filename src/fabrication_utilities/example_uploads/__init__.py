from nomad.config.models.plugins import ExampleUploadEntryPoint

process_upload_entry_point = ExampleUploadEntryPoint(
    title='Fabrication process and steps',
    category='Fabrication examples',
    description="""
        This example upload show the method of storing raw data in nomad for fabrication
        processes. This should be help a FAIR pipeline for data stored in Nomad.
    """,
    resources=['processes/*'],
)
