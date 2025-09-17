# Contribute to This Plugin

To contribute to the plugin the ideal workflow should be:

- Fork the repository from [`Fabrication-Utilities`](https://github.com/Trog-404/Fabrication-utilities.git) in your own github repo.

- Performing some modifications in the forked repository. After some testing the working new code can be inserted in a pull request and then sent to the the main repository.

- To ensure minimum conflicts with the main repository where some modification can occur, it is mandatory to mantaine as up-to-date as possible the forked repository to the origin of the project.

Contribution should be linked mainly to

- Schema packages definitions
- Apps to indicize schemas defined
- Example upload

## Schema_packages contribution

In the [schema_package](https://github.com/Trog-404/Fabrication-utilities/tree/main/src/fabrication_utilities/schema_packages) module you will find different files and repo. For a better description of the module it is possible to refer to this [instructions](https://github.com/Trog-404/Fabrication-utilities/blob/main/src/fabrication_utilities/readme.md).

Files at the top level in the schema_packages folder hierarchy should not be modified. They are the core of the plugin and there a lot of base definition used throghout the code are placed.

### Steps definitions

It is possible to define new schemas for steps definitions in the [steps](https://github.com/Trog-404/Fabrication-utilities/tree/main/src/fabrication_utilities/schema_packages/steps) branch. Here, following the taxonomy described in the [explanation](../explanation/explanation.md) guide. Moreover for a general guide on how to define a new schema you can see [here](https://nomad-lab.eu/prod/v1/docs/howto/plugins/schema_packages.html).

#### Example

If a schema is needed to describe a new kind of CVD not already present in the plugin, that schema should be inserted in the [CVD](../../src/fabrication_utilities/schema_packages/steps/add/synthesis/CVD.py). New fabrication main categories should be added the idea is to define it at the correspinding level of the others following the taxonomy and at that level define the python files containing the schemas. At that point the entry point should be defined in the `__init__.py` of the new module and so called in the `pyproject.toml` file of the entire project. If new sections are needed to define the schemas that subsections type could be defined in the [utils.py](../../src/fabrication_utilities/schema_packages/steps/utils.py) file.

### Equipments definitions

If a new kind of equipment is needed it could be added in the [equipments](../../src/fabrication_utilities/schema_packages/equipments/) module. If the equipment is used to properly perform fabrication steps is should be added in [fabrication-equipments](../../src/fabrication_utilities/schema_packages/equipments/equipments.py) file, while characterization equipments are collected in [characterization-equipments](../../src/fabrication_utilities/schema_packages/equipments/equipments.py). As before new definitions for subsections could be added in the [utils](../../src/fabrication_utilities/schema_packages/equipments/utils.py) file of this directrory.

### Calculus sheet definitions

If new calculation sheets is needed they could be defined in the [calculus](../../src/fabrication_utilities/schema_packages/calculus/calculus.py) module of the plugin.

## Apps contribution

For more detail about the structure of the apps module it is possible to read the following [description](../../src/fabrication_utilities/apps/readme.md). There are present two submodules both very similar. Each modulus has a directories.py file where the path to the schemas to point are report. Than you have different app for steps and equipments. Where new filters to the app should be added.

The organization of the app categories and placement should not be modified.

### App for new step schema

If a new schema was defined by the user, it should be searchable within NOMAD for a better findability of the entry. At this scope the work should be organized as in the following example. To define an app could be used the official NOMAD guide [how to write and app](https://nomad-lab.eu/prod/v1/docs/howto/plugins/apps.html).

#### Example

If a new step synthesis step is defined a new menu should be defined in the [app for add step](../../src/fabrication_utilities/apps/fabrication/addapp.py). The menu should be defined in the menu_steps.py file and the link to the schema defined added to the directories.py file.

## Example upload