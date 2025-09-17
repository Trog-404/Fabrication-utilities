#######################################################################################
#######################################################################################
# In this file will be defined entities which will be used to perform some operations #
# on data. In particular, we will define structures within some inputs are passed and #
# through the normalization method will give as output the properties to evaluate.    #
#######################################################################################
#######################################################################################
from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import ArchiveSection, EntryData
from nomad.metainfo import (
    Datetime,
    Package,
    Quantity,
    Section,
    SubSection,
)
from schema_packages.fabrication_utilities import (
    FabricationProcessStep,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Definitions for usual operation of analysis')


class BaseCalculusSheet(EntryData, ArchiveSection):
    m_def = Section()

    name = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})

    ID = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})

    datetime = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )

    notes = Quantity(type=str, a_eln={'component': 'RichTextEditQuantity'})

    location = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})


class EtchingRateOutput(ArchiveSection):
    m_def = Section()

    etching_rate_value = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm/minute'},
        unit='nm/minute',
    )


class EtchingRateInputs(ArchiveSection):
    m_def = Section()

    etching_time = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    etching_time_reference = Quantity(
        type=FabricationProcessStep,
        a_eln={'component': 'ReferenceEditQuantity'},
    )
    depth = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    depth_reference = Quantity(
        type=FabricationProcessStep,
        a_eln={'component': 'ReferenceEditQuantity'},
    )


class EtchingRate(BaseCalculusSheet):
    m_def = Section()

    inputs = SubSection(section_def=EtchingRateInputs, repeats=False)

    output = SubSection(section_def=EtchingRateOutput, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        if self.inputs is not None:
            if self.inputs.depth and self.inputs.etching_time != 0:
                self.output = EtchingRateOutput()
                self.output.etching_rate_value = (
                    self.inputs.depth / self.inputs.etching_time
                )


class DepositionRateOutput(ArchiveSection):
    m_def = Section()

    deposition_rate_value = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm/minute'},
        unit='nm/minute',
    )


class DepositionRateInputs(ArchiveSection):
    m_def = Section()

    deposition_time = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    deposition_time_reference = Quantity(
        type=FabricationProcessStep,
        a_eln={'component': 'ReferenceEditQuantity'},
    )
    thickness = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )
    thickness_reference = Quantity(
        type=FabricationProcessStep,
        a_eln={'component': 'ReferenceEditQuantity'},
    )


class DepositionRate(BaseCalculusSheet):
    m_def = Section()

    inputs = SubSection(section_def=DepositionRateInputs, repeats=False)

    output = SubSection(section_def=DepositionRateOutput, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        if self.inputs is not None:
            if self.inputs.thickness and self.inputs.deposition_time != 0:
                self.output = DepositionRateOutput()
                self.output.deposition_rate_value = (
                    self.inputs.thickness / self.inputs.deposition_time
                )


class StressPropertiesOutput(ArchiveSection):
    m_def = Section()

    stress_value = Quantity(
        type=np.float64,
        unit='GPa',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'GPa'},
    )


class StressPropertiesInputs(ArchiveSection):
    m_def = Section()

    substrate_thickness = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )

    substrate_thickness_reference = Quantity(
        type=FabricationProcessStep, a_eln={'component': 'ReferenceEditQuantity'}
    )

    layer_thickness = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )

    layer_thickness_reference = Quantity(
        type=FabricationProcessStep, a_eln={'component': 'ReferenceEditQuantity'}
    )

    curvature_radius = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nm'},
        unit='nm',
    )

    curvature_radius_reference = Quantity(
        type=FabricationProcessStep, a_eln={'component': 'ReferenceEditQuantity'}
    )


class StressParametersAdopted(ArchiveSection):
    m_def = Section()

    assumed_Young_module_of_the_substrate = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'GPa'},
        unit='GPa',
    )

    assumed_Poisson_coefficient = Quantity(
        type=np.float64, a_eln={'component': 'NumberEditQuantity'}
    )


class StressProperties(BaseCalculusSheet):
    m_def = Section(
        description="""
        Calculus sheet to evaluate some stress properties thanks to the Stoney formula
        """
    )

    inputs = SubSection(section_def=StressPropertiesInputs, repeats=False)

    parameters = SubSection(section_def=StressParametersAdopted, repeats=False)

    output = SubSection(section_def=StressPropertiesOutput, repeats=False)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        if self.parameters.assumed_Poisson_coefficient is not None:
            pois = self.parameters.assumed_Poisson_coefficient
        if self.parameters.assumed_Young_module_of_the_substrate is not None:
            young = self.parameters.assumed_Young_module_of_the_substrate
        if self.inputs is not None and pois and young:
            if self.inputs.curvature_radius and self.inputs.layer_thickness:
                R = self.inputs.curvature_radius
                t = self.inputs.layer_thickness
                if self.inputs.substrate_thickness is not None and R != 0 and t != 0:
                    D = self.inputs.substrate_thickness
                    self.output = StressPropertiesOutput()
                    self.output.stress_value = young * D * D / (6 * (1 - pois) * R * t)
