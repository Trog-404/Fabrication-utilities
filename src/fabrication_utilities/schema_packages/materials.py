from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import (
    ArchiveSection,
)
from nomad.metainfo import (
    Package,
    Quantity,
    Section,
    SubSection,
)
from schema_packages.calculus.calculus import EtchingRate
from schema_packages.fabrication_utilities import (
    FabricationOutput,
    FabricationProcess,
    FabricationProcessStep,
)
from schema_packages.utils import FabricationChemical

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(
    name='Materials plugin', description='Plugin to describe raw materials properties'
)


class EtchingMeasures(ArchiveSection):
    m_def = Section(
        description='Class describing etching properties characterized for materials',
        a_eln={
            'properties': {
                'order': [
                    'recipe_name',
                    'link_to_step',
                    'etching_rate_measured',
                ],
            },
        },
    )

    recipe_name = Quantity(
        type=str,
        description='Recipe used to measure etching rate in the process',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    link_to_step = Quantity(
        type=FabricationProcessStep,
        description='Link to reach the step with the parameters used',
        a_eln={'component': 'ReferenceEditQuantity'},
    )

    etching_rate_measured = Quantity(
        type=np.float64,
        description='Value obtained for the etching rate',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'nm/minute',
        },
        unit='nm/minute',
    )

    etching_calculations = SubSection(
        section_def=EtchingRate,
        description="""
        Instead of using your notebook here you can enter input data to obtain the
        etching rate needed
        """,
        repeats=False,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.etching_calculations.output.etching_rate_value is not None:
            result = self.etching_calculations.output.etching_rate_value
            self.etching_rate_measured = result


class EtchingProperties(ArchiveSection):
    etching_results = SubSection(
        section_def=EtchingMeasures,
        repeats=True,
    )


class StressMeasures(ArchiveSection):
    m_def = Section(
        description='Class describing stress properties characterized for materials',
        a_eln={
            'properties': {
                'order': [
                    'stress_measured',
                ],
            },
        },
    )

    # recipe_name = Quantity(
    #     type=str,
    #     description='Recipe used to measure etching rate in the process',
    #     a_eln={
    #         'component': 'StringEditQuantity',
    #     },
    # )

    # link_to_step = Quantity(
    #     type=FabricationProcessStep,
    #     description='Link to reach the step with the parameters used',
    #     a_eln={'component': 'ReferenceEditQuantity'},
    # )

    stress_measured = Quantity(
        type=np.float64,
        description='Value obtained for the etching rate',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'GPa',
        },
        unit='GPa',
    )

    # instrument = SubSection(
    #     section_def=EquipmentReference,
    #     description='Instrument through which the etching trial was performed',
    #     repeats=False,
    # )


class StressProperties(ArchiveSection):
    # instrument = SubSection(
    #     section_def=EquipmentReference,
    #     description='Instrument through which the characterization was performed',
    #     repeats=False,
    # )
    stress_results = SubSection(
        section_def=StressMeasures,
        repeats=True,
    )


# class ElectricProperties(ArchiveSection):
#     instrument = SubSection(
#         section_def=EquipmentReference,
#         description='Instrument through which the characterization was performed',
#         repeats=False,
#     )


class FabricationMaterial(FabricationOutput):
    m_def = Section(
        description='Class containing all information measured for a raw material',
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'ID',
                    'description',
                    'location',
                ]
            }
        },
    )

    name = Quantity(
        type=str,
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    description = Quantity(
        type=str,
        a_eln={
            'component': 'RichTextEditQuantity',
        },
    )

    location = Quantity(
        type=str,
        description='Laboratiory which produced the material',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )

    chemical_components = SubSection(
        section_def=FabricationChemical,
        repeats=True,
    )

    etching_properties = SubSection(
        section_def=EtchingProperties,
        repeats=False,
    )

    stress_properties = SubSection(
        section_def=StressProperties,
        repeats=False,
    )

    # geometric_properties = SubSection(
    #     section_def=ProfileProperties,
    #     repeats=False,
    # )

    # electric_properties = SubSection(
    #     section_def=ElectricProperties,
    #     repeats=False,
    # )


class MaterialProductionProcess(FabricationProcess):
    m_def = Section(
        description="""
        Particular instance of a fabrication process where the output is a raw material
        on a wafer. Upon this raw material are performed various characterization and
        trial of steps, e.g. etching to derive the etching rates, to give a list of
        property for that particular material. At the moment you can describe only
        etching rates porperly.
        """,
    )

    output = SubSection(section_def=FabricationMaterial, repeat=False)
