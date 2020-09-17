PartMC Scenario Generator
=================
[![DOI](https://zenodo.org/badge/261375515.svg)](https://zenodo.org/badge/latestdoi/261375515)

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Introduction](#introduction)
- [Prerequisite](#prerequisite)
- [Instructions](#instructions)
- [Cases Information](#cases-information)
- [Acknowledgement](#acknowledgement)

<!-- /code_chunk_output -->

## Introduction
This repository is a supplementary to the manuscript **"Estimating Submicron Aerosol Mixing State at the Global Scale with Machine Learning and Earth System Modeling"**.

The purpose of this project is to using **[Latin hypercube sampling (LHS)](https://en.wikipedia.org/wiki/Latin_hypercube_sampling)** to create scenarios for **[Particle-resolved Monte Carlo (PartMC)](http://lagrange.mechse.illinois.edu/partmc/)** version 2.5.0.

## Prerequisite
```bash
# Create your own conda/python environment
pip install pyDOE datetime pandas xarray
```

## Instructions
**Step 1: Define the parameters and create cases**

Within each case (e.g., `case_1`), define the paramaters in the file `1_create_LHS_matrix.py`. Then execute the command:
```python
python 1_create_LHS_matrix.py
```
Here you need to type the total number of scenarios that you want to generate

**Step 2: Apply the parameters to the cases**

Within the same case, execute the command:
```python
python 2_modify_dat_spec.py
```
Again, here you need to confrim the total number of scenarios that you want to deal with.

**Step 3: Run the particle-resolved simulations**

You may follow the [instruction](http://lagrange.mechse.illinois.edu/partmc/partmc-2.5.0/doc/README.html) of PartMC to run the simulation for the scenarios! 

## Cases Information    

***w/o sea salt***    
Action (within the case):<br>
1.modify "1_create_LHS_matrix" (RH_min, RH_max, Latitude_min, Latitude_max, and **ss** relevant copies)<br>
2.modify "gas_back.dat"<br>
3.modify "2_modify_dat_spec.py"  

```python
# assume there are no sea salt and DMS
util.modify_aero_emit_dist(directory, matrix, ss_option=None, dust_option=True)
util.modify_gas_emit(directory, matrix, DMS_option=None))
#util.modify_aero_emit_comp_ss1(directory, matrix)
#util.modify_aero_emit_comp_ss2(directory, matrix)
```

|                                                      | With sea salt     | Without sea salt  |
| ---------------------------------------------------- | ----------------- | ----------------- |
| **Latitude**                                         | [-89.999, 89.999] | [-69.999, 69.999] |
| **Relative humidty**                                 | [0.4, 0.999]      | [0.1, 0.999]      |
| **DMS concentration (ppb)** (gas_back.dat)           | 5.0E-01           | No                |
| **DMS emissions (mol m^{-2} s^{-1})** (gas_emit.dat) | 3.756E-11         | No                |

***w/o dust***     
Action:<br>
1.modify "1_create_LHS_matrix" (RH_min, RH_max, Latitude_min, Latitude_max, and **dust** relevant copies)<br>
2.modify "2_modify_dat_spec.py"  

```python
# assume there are no dust, but sea salt
util.modify_aero_emit_dist(directory, matrix, ss_option=True, dust_option=None)
```

**Cases/Scenarios Distribution**

|                      | 2/3 with sea salt | 1/3 without sea salt |
| -------------------- | ----------------- | -------------------- |
| **2/3 with dust**    | **case_1** (4/9)  | **case_2** (2/9)     |
| **1/3 without dust** | **case_3** (2/9)  | **case_4** (1/9)     |

**case_5** (high latitudes, Northern Hemisphere, lat: 60 - 89.999): include seasalt and carbonaceous aerosol (no dust) emissions (1/9) 

**case_6** (high latitudes, Southern Hemisphere, lat: -89.999 - -60): include seasalt and carbonaceous aerosol (no dust) emissions (1/9) 

## Acknowledgement

This research is part of the Blue Waters sustained-petascale computing project, which is supported by the National Science Foundation (awards OCI-0725070 and ACI-1238993) the State of Illinois, and as of December, 2019, the National Geospatial-Intelligence Agency. Blue Waters is a joint effort of the University of Illinois at Urbana-Champaign and its National Center for Supercomputing Applications.

