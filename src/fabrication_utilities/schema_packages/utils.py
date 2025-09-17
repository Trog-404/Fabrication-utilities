import re
from collections import defaultdict
from typing import (
    TYPE_CHECKING,
)

import numpy as np
import plotly.express as px
from ase.data import atomic_masses as am
from ase.data import atomic_numbers as an
from nomad.datamodel.data import ArchiveSection
from nomad.datamodel.metainfo.basesections import ElementalComposition
from nomad.datamodel.metainfo.eln import Chemical
from nomad.datamodel.metainfo.plot import PlotlyFigure, PlotSection
from nomad.metainfo import Quantity, Section, SubSection

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )


def parse_chemical_formula(formula):
    formula = formula.replace('·', '.')
    if '.' in formula:
        main_part, hydrate_part = formula.split('.')
    else:
        main_part, hydrate_part = formula, None

    def extract_elements(compound):
        # Espressione per trovare elementi chimici seguiti da un numero opzionale
        matches = re.findall(r'([A-Z][a-z]*)(\d*)', compound)
        elements = defaultdict(int)

        for element, count in matches:
            elements[element] += int(count) if count else 1

        return elements

    element_main = defaultdict(int)

    # Espandiamo le parentesi prima di estrarre gli elementi
    while '(' in main_part:
        main_part = re.sub(
            r'\(([^()]*)\)(\d+)', lambda m: m.group(1) * int(m.group(2)), main_part
        )

    # Trova elementi e numeri
    matches = re.findall(r'([A-Z][a-z]*)(\d*)', main_part)

    for element, count in matches:
        element_main[element] += (
            int(count) if count else 1
        )  # Se il numero manca, assume 1

    if hydrate_part:
        hydrate_match = re.match(r'(\d*)H2O', hydrate_part)
        if hydrate_match:
            water_molecules = (
                int(hydrate_match.group(1)) if hydrate_match.group(1) else 1
            )
            elements_hydrate = extract_elements('H2O')

            for element, count in elements_hydrate.items():
                element_main[element] += count * water_molecules

    # Convertiamo il dizionario in due liste ordinate
    elements = list(element_main.keys())
    counts = list(element_main.values())

    return elements, counts


def generate_elementality(formula):
    elements, counts = parse_chemical_formula(formula)
    total = 0
    for token in counts:
        total += int(token)
    mass = sum(am[an[el]] * cou for el, cou in zip(elements, counts))
    if total != 0:
        elemental_fraction = np.array(counts) / total
        elementality = []
        i = 0
        for entry in elements:
            elemental_try = ElementalComposition()
            elemental_try.element = entry
            elemental_try.atomic_fraction = elemental_fraction[i]
            mass_frac = (am[an[entry]] * counts[i]) / mass
            elemental_try.mass_fraction = mass_frac
            i += 1
            elementality.append(elemental_try)
    else:
        print('No elements provided')

    return elementality


class FabricationChemical(Chemical, ArchiveSection):
    m_def = Section(
        definition='Chemicals for fabrication products',
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
        },
    )

    elemental_composition = SubSection(
        section_def=ElementalComposition,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.chemical_formula:
            self.elemental_composition = generate_elementality(self.chemical_formula)


def make_line_express(list1, list2, labelx, labely, finalist, labelfigure):
    figure1 = px.line(
        x=list1,
        y=list2,
        height=400,
        width=800,
        labels={'x': labelx, 'y': labely},
        markers=True,
    )

    finalist.append(
        PlotlyFigure(
            label=labelfigure,
            figure=figure1.to_plotly_json(),
            index=0,
        )
    )


# Capire se se può ingegnerizzare meglio la funzione per ridurre variabili


class TimeRampTemperature(PlotSection):
    m_def = Section()

    name = Quantity(
        type=str,
        description='What temperature are you tracing?',
        a_eln={'component': 'StringEditQuantity'},
    )

    start_value = Quantity(
        type=np.float64,
        description='Value at the beginning of the increment',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    end_value = Quantity(
        type=np.float64,
        description='Value at the end of the increment',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )

    increment_duration = Quantity(
        type=np.float64,
        description='Duration of the increment',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )

    increment_behavior = Quantity(
        type=str,
        description='Is the increment linear(uniform), sigmoidal, etc...?',
        a_eln={'component': 'StringEditQuantity'},
    )

    time = Quantity(
        type=np.float64,
        shape=['*'],
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )

    values = Quantity(
        type=np.float64,
        shape=['*'],
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )

    def normalize(self, archive, logger):
        if self.values is not None and len(self.values) > 0:
            super().normalize(archive, logger)
            if hasattr(self, 'figures') and self.figures:
                self.figures.clear()
            make_line_express(
                self.time,
                self.values,
                'Time (s)',
                'Temperature (°C)',
                self.figures,
                'Ramp of temperature',
            )


class TimeRampPressure(PlotSection):
    m_def = Section()

    name = Quantity(
        type=str,
        description='What pressure are you tracing?',
        a_eln={'component': 'StringEditQuantity'},
    )

    start_value = Quantity(
        type=np.float64,
        description='Value at the beginning of the increment',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    end_value = Quantity(
        type=np.float64,
        description='Value at the end of the increment',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'mbar',
        },
        unit='mbar',
    )

    increment_duration = Quantity(
        type=np.float64,
        description='Duration of the increment',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )

    increment_behavior = Quantity(
        type=str,
        description='Is the increment linear(uniform), sigmoidal, etc...?',
        a_eln={'component': 'StringEditQuantity'},
    )

    time = Quantity(
        type=np.float64,
        shape=['*'],
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )

    values = Quantity(
        type=np.float64,
        shape=['*'],
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )

    def normalize(self, archive, logger):
        if self.values is not None and len(self.values) > 0:
            super().normalize(archive, logger)
            if hasattr(self, 'figures') and self.figures:
                self.figures.clear()
            make_line_express(
                self.time,
                self.values,
                'Time (s)',
                'Pressure (mbar)',
                self.figures,
                'Ramp of pressure',
            )


class TimeRampMassflow(PlotSection):
    m_def = Section()

    name = Quantity(
        type=str,
        description='What massflow are you tracing? (Chemical formulas are accepted)',
        a_eln={'component': 'StringEditQuantity'},
    )

    start_value = Quantity(
        type=np.float64,
        description='Value at the beginning of the increment',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )

    end_value = Quantity(
        type=np.float64,
        description='Value at the end of the increment',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )

    increment_duration = Quantity(
        type=np.float64,
        description='Duration of the increment',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )

    increment_behavior = Quantity(
        type=str,
        description='Is the increment linear(uniform), sigmoidal, etc...?',
        a_eln={'component': 'StringEditQuantity'},
    )

    time = Quantity(
        type=np.float64,
        shape=['*'],
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )

    values = Quantity(
        type=np.float64,
        shape=['*'],
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'centimeter^3/minute',
        },
        unit='centimeter^3/minute',
    )

    def normalize(self, archive, logger):
        if self.values is not None and len(self.values) > 0:
            super().normalize(archive, logger)
            if hasattr(self, 'figures') and self.figures:
                self.figures.clear()
            make_line_express(
                self.time,
                self.values,
                'Time (s)',
                'Massflow (sccm)',
                self.figures,
                'Ramp of massflow',
            )


class TimeRampRotation(PlotSection):
    m_def = Section()

    name = Quantity(
        type=str,
        description='What rotation are you tracing?',
        a_eln={'component': 'StringEditQuantity'},
    )

    start_value = Quantity(
        type=np.float64,
        description='Value at the beginning of the increment',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'rpm'},
        unit='rpm',
    )

    end_value = Quantity(
        type=np.float64,
        description='Value at the end of the increment',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'rpm'},
        unit='rpm',
    )

    increment_duration = Quantity(
        type=np.float64,
        description='Duration of the increment',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'sec'},
        unit='sec',
    )

    increment_behavior = Quantity(
        type=str,
        description='Is the increment linear(uniform), sigmoidal, etc...?',
        a_eln={'component': 'StringEditQuantity'},
    )

    time = Quantity(
        type=np.float64,
        shape=['*'],
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'sec',
        },
        unit='sec',
    )

    values = Quantity(
        type=np.float64,
        shape=['*'],
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'rpm'},
        unit='rpm',
    )

    def normalize(self, archive, logger):
        if self.values is not None and len(self.values) > 0:
            super().normalize(archive, logger)
            if hasattr(self, 'figures') and self.figures:
                self.figures.clear()
            make_line_express(
                self.time,
                self.values,
                'Time (s)',
                'Spin frequency (rpm)',
                self.figures,
                'Ramp of spin frequency',
            )


class BeamSource(ArchiveSection):
    m_def = Section()

    emitter_material = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})

    probe = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})


def double_list_reading(list1, list2, archive, logger):
    if list1 and list2:
        reactives = []
        for v1, v2 in zip(list1, list2):
            chemical = FabricationChemical()
            val1 = v1  # if v1 != '-' else val1=v2
            val2 = v2 if v2 != '-' else None
            chemical.name = val1
            chemical.chemical_formula = val2
            chemical.normalize(archive, logger)
            reactives.append(chemical)
    return reactives
