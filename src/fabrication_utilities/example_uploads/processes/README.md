# Introduction

The goal of this example is to show how, through the *Fabrication-utilities* plugin, it is possible to describe either a simple or complex fabrication process, making many (potentially all) of the useful metadata searchable for both replicability and process understanding.

## Explanation

To represent fabrication processes, two fundamental entities have been defined in the process workflow.  
The first is the `FabricationProcess` class, which allows you to report all parameters useful for the findability of the process, as it was globally carried out in a laboratory, clean-room, etc.  
The second key building block is the `FabricationProcessStep` class, which serves as a base class and is then specialized for each possible type of step. This element is the repeatable unit of the process and describes any kind of procedure aimed at modifying the chemical-physical or geometric properties of a material.  

Individual step instances are generated from a taxonomy defined and described here (insert link).  
Briefly, the concept of *technique* (e.g., *chemical vapor deposition (CVD)*, *doping*, just to name a few) is fundamental. Each specific instance distinguishes the corresponding class built from `FabricationProcessStep`.  

Each step is collected into a taxonomy that distinguishes them based on a `GeneralCategory` (add, remove, transform, characterize), which determines what kind of effect will be produced on the sample (for example, "add" contains all techniques aimed at adding materials, such as deposition).  
These are further refined into more specific categories called `MainCategory`, used to better describe what each step does (for example, the CVD steps mentioned earlier belong to the "synthesis" class, since their purpose is to synthesize materials from precursors).  
Finally, the specific techniques (such as CVD) are `SubCategories` of the `MainCategory` and describe the techniques, although they can then be specialized into specific instances (e.g., CVD may be LPCVD or PECVD). For more details, see (insert link).  

Another important concept is the definition of an *item*. Currently, processes and steps are linked to the item on which they are performed. By *item* we mean, in general, the uniquely identifiable component that undergoes a certain process of modification or inspection of its properties.  
In this sense, an item differs from what is typically called a *sample* in characterization processes, or rather it generalizes it since in fabrication processes a sample is simply an item specifically prepared for a given characterization step.

## Files view

The example upload can be browsed in the `FILES` section to check its contents.  
All the files are of type `.archive.json` because fabrication processes are typically made up of instructions that the user must execute manually, or more frequently by setting up machine parameters or recipes. For this reason, representing them as electronic lab notebooks within `NOMAD` seemed the best solution, and we have expanded only that option.  

Therefore, each schema can also be filled in within `NOMAD` by selecting `CREATE FROM SCHEMA` among the built-in schemas, and choosing the desired section (e.g., `FabricationProcess`, `WetCleaning`, `RIE`, `LPCVD`, etc.).  

Regarding the content, the file contains only dummy upload tests, intended solely to demonstrate the methodology:

- `Process_prova.archive.json`: Contains references to the various steps, listed in the data section of the archive  
- `Prova_cleaning.archive.json`  
- `Prova_drying.archive.json`  
- `Prova_spin_develop.archive.json`  
- `Prova_soft_bake.archive.json`  
- `Prova_ebl.archive.json`  
- `Prova_PEB.archive.json`  
- `Prova_spin_develop.archive.json`  
- `Prova_stripping.archive.json`

The result of the processing could be also searched thanks to the research apps defined in `EXPLORE` under the category `Fabrication utilities`

## Remaining features and issues

The process described in this example could also support characterization steps if built on the `FabricationProcessStep` class.  
Therefore, the best way to describe and integrate them is through the *Characterization-utilities* package, which also provides built-in methods to generate FAIR-compliant files recognized by the community directly from raw experimental data, where supported (the package is continuously expanding and you may be integrated into its structure).  

For any issues with the code or features request, please do not hesitate to contact the system maintainers (insert emails).  
