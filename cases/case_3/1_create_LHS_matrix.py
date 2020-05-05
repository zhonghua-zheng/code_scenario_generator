# %% Load necessary libraries
import numpy as np
import pandas as pd
import pyDOE
import os
import shutil

# https://codeday.me/bug/20170427/11215.html 
def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]



def DOY_lat_temp(DOY, latitude, df): 
    df_DOY = df.loc[df["DOY"]==DOY]
    near_lat = find_nearest(np.asarray(list(set(df_DOY.index))),latitude)
    max_temp = df_DOY.loc[near_lat]["max"]
    min_temp = df_DOY.loc[near_lat]["min"]
    #print("DOY is:", DOY)
    #print("Latitude is:", latitude)
    print("nearest latitude is:",near_lat)
    #print("max temp is:", max_temp)
    #print("min temp is:", min_temp)
    return min_temp, max_temp


"""
def max_min_temp(latitude, doy,df):
    DOY_array = np.array([31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365])
    month = (np.abs(DOY_array-doy)).argmin()+1
    nearest_latitude = find_nearest(df.index, latitude)
    min_temp = df.loc[nearest_latitude][str(month)+"_min"]
    max_temp = df.loc[nearest_latitude][str(month)+"_max"]
    print("The nearest latitude is:", "%.3f" % nearest_latitude)
    print("The nearest month is:", month)
    #print("min_temp:", min_temp)
    #print("max_temp:", max_temp)
    
    return min_temp, max_temp 
"""

df = pd.read_pickle('../../ref/doy_lat_temp/temp_max_min.pkl')

# %% Define the min and max for each variable
# Define the scenarios
scenarios = int(input("How many scenarios?\n"))
#scenarios = 5
print("The number of scenarios is:", scenarios)
## Environmental variable
# 1) RH   
RH_min = 0.4; RH_max = 0.999;  #0
# 2) Latitude
Latitude_min = -89.999; Latitude_max = 89.999; #1
# 3) Day of Year 
DOY_min = 1; DOY_max = 365; #2
# 4) Temp
Temp_min = 0; Temp_max = 1; #3
# 5) Restart time stamp
restart_time_stamp_min = 1; restart_time_stamp_max = 25; #39
# Dilution rate
# To be added
# Mixing height
# To be added

## Emission
# Gas phase emissions
# 1) SO2
SO2_emit_min = 0; SO2_emit_max = 2; #4
# 2) NO2
NO2_emit_min = 0; NO2_emit_max = 2; #5
# 3) NO
NO_emit_min = 0; NO_emit_max = 2; #6
# 4) NH3
NH3_emit_min = 0; NH3_emit_max = 2; #7
# 5) CO
CO_emit_min = 0; CO_emit_max = 2; #8
# 6) ALD2
ALD2_emit_min = 0; ALD2_emit_max = 2; #9
# 7) HCHO
HCHO_emit_min = 0; HCHO_emit_max = 2; #10
# 8) ETH
ETH_emit_min = 0; ETH_emit_max = 2; #11
# 9) OLEI
OLEI_emit_min = 0; OLEI_emit_max = 2; #12
# 10) OLET
OLET_emit_min = 0; OLET_emit_max = 2; #13
# 11) TOL
TOL_emit_min = 0; TOL_emit_max = 2; #14
# 12) XYL
XYL_emit_min = 0; XYL_emit_max = 2; #15
# 13) AONE
AONE_emit_min = 0; AONE_emit_max = 2; #16
# 14) PAR
PAR_emit_min = 0; PAR_emit_max = 2; #17
# 15) ISOP 
ISOP_emit_min = 0; ISOP_emit_max = 2; #18
# 16) CH3OH
CH3OH_emit_min = 0; CH3OH_emit_max = 2; #19
# 17) ANOL
ANOL_emit_min = 0; ANOL_emit_max = 2; #20
# 18) DMS
DMS_emit_min = 0; DMS_emit_max = 2; #40

# Carbonaceous Aerosol Emissions
# 1) Dg
Dg_cae_min = 2.5e-08; Dg_cae_max = 2.5e-07; #21
# 2) sigmag
sigmag_cae_min = 1.4; sigmag_cae_max = 2.5; #22
# 3) Ea
Ea_cae_min = 0; Ea_cae_max = 1.6e7; #23
# 4) BC percentage
BC_per_min = 0; BC_per_max = 1; #24

# Sea Salt Emissions
# 1) Dg1
Dg1_sse_min = 1.8e-07; Dg1_sse_max = 7.2e-07; #25
# 2) sigmag1
sigmag1_sse_min = 1.4; sigmag1_sse_max = 2.5; #26
# 3) Ea1
Ea1_sse_min = 0; Ea1_sse_max = 1.69e5; #27
# 4) OC_1 fraction
OC_1_fra_min = 0; OC_1_fra_max = 0.2; #28 
# 4) Dg2
Dg2_sse_min = 1.0e-06; Dg2_sse_max = 6.0e-06; #29
# 5) sigmag2
sigmag2_sse_min = 1.4; sigmag2_sse_max = 2.5; #30
# 6) Ea2
Ea2_sse_min = 0; Ea2_sse_max = 2.38e03; #31
# 7) OC_2 fraction
OC_2_fra_min = 0; OC_2_fra_max = 0.2; #32

# Dust Emissions
# 1) Dg1
Dg1_dust_min = 8.0e-8; Dg1_dust_max = 3.2e-07; #33
# 2) sigmag1
sigmag1_dust_min = 1.4; sigmag1_dust_max = 2.5; #34
# 3) Ea1
Ea1_dust_min = 0; Ea1_dust_max = 5.86e05; #35
# 4) Dg2
Dg2_dust_min = 1.0e-6; Dg2_dust_max = 6.0e-6; #36
# 5) sigmag2
sigmag2_dust_min = 1.4; sigmag2_dust_max = 2.5; #37
# 6) Ea2
Ea2_dust_min = 0; Ea2_dust_max = 2.38e03; #38

# Create Latin Hypercube Sampling matrix and save
lhs_min = np.asarray([RH_min, Latitude_min, DOY_min, Temp_min, 
           SO2_emit_min, NO2_emit_min, NO_emit_min, NH3_emit_min, CO_emit_min,
           ALD2_emit_min, HCHO_emit_min, ETH_emit_min, OLEI_emit_min, OLET_emit_min,           
           TOL_emit_min, XYL_emit_min, AONE_emit_min, PAR_emit_min, ISOP_emit_min,
           CH3OH_emit_min, ANOL_emit_min,
           Dg_cae_min, sigmag_cae_min, Ea_cae_min, BC_per_min, 
           Dg1_sse_min, sigmag1_sse_min, Ea1_sse_min, OC_1_fra_min,
           Dg2_sse_min, sigmag2_sse_min, Ea2_sse_min, OC_2_fra_min,
           Dg1_dust_min, sigmag1_dust_min, Ea1_dust_min, Dg2_dust_min, sigmag2_dust_min, Ea2_dust_min, 
           restart_time_stamp_min, DMS_emit_min])
lhs_max = np.asarray([RH_max, Latitude_max, DOY_max, Temp_max, 
           SO2_emit_max, NO2_emit_max, NO_emit_max, NH3_emit_max, CO_emit_max,
           ALD2_emit_max, HCHO_emit_max, ETH_emit_max, OLEI_emit_max, OLET_emit_max,           
           TOL_emit_max, XYL_emit_max, AONE_emit_max, PAR_emit_max, ISOP_emit_max,
           CH3OH_emit_max, ANOL_emit_max,
           Dg_cae_max, sigmag_cae_max, Ea_cae_max, BC_per_max, 
           Dg1_sse_max, sigmag1_sse_max, Ea1_sse_max, OC_1_fra_max,
           Dg2_sse_max, sigmag2_sse_max, Ea2_sse_max, OC_2_fra_max,
           Dg1_dust_max, sigmag1_dust_max, Ea1_dust_max, Dg2_dust_max, sigmag2_dust_max, Ea2_dust_max, 
           restart_time_stamp_max, DMS_emit_max])

lhs_prob = pyDOE.lhs(len(lhs_min), scenarios)
lhs = lhs_min + (lhs_max-lhs_min) * lhs_prob

# Calculate the temperature for each scenario
for i in range(lhs.shape[0]):
    print("********Scenario",str(i).zfill(4),"********")
    lat=(lhs[i,1])
    print("lat:","%.3f" % lat)
    doy=int(lhs[i,2])
    print("doy:",doy)
    
    min_temp, max_temp = DOY_lat_temp(doy, lat, df)
    print("min temperature:", "%.3f" % (min_temp-273.15))
    print("max temperature:", "%.3f" % (max_temp-273.15))
    
    print("Temperature factor", "%.3f" % lhs[i,3])
    lhs[i,3] = min_temp + (max_temp - min_temp) * lhs[i,3] 
    print("final temperature:", "%.3f" % (lhs[i,3]-273.15))
    print("\n")

print("The dimension of the Latin Hypercube Sampling is:",lhs.shape)
print("There are", str(lhs.shape[0]), "scenarios, and", str(lhs.shape[1]), "variables")

# Save the necessary matrix
np.savetxt("./lhs_prob.txt",lhs_prob)
np.savetxt("./lhs_min.txt",lhs_min)
np.savetxt("./lhs_max.txt",lhs_max)
np.savetxt("./lhs.txt",lhs)

# Load the matrix and distribute into different scenarios
lhs = np.loadtxt("./lhs.txt")
for i in range (lhs.shape[0]):
    directory = "./scenarios/scenario_" +  str(i).zfill(4)
    if not os.path.exists(directory):
        os.makedirs(directory)
    np.savetxt(directory+"/matrix_"+str(i).zfill(4)+".txt",lhs[i])
    
    # aero_data and gas_data
    shutil.copy("./dat_files/aero_data.dat",directory+"/aero_data.dat")
    shutil.copy("./dat_files/gas_data.dat",directory+"/gas_data.dat")
    
    # aero_back
    shutil.copy("./dat_files/aero_back_comp.dat",directory+"/aero_back_comp.dat")
    shutil.copy("./dat_files/aero_back_dist.dat",directory+"/aero_back_dist.dat")
    shutil.copy("./dat_files/aero_back.dat",directory+"/aero_back.dat")
    
    # aero_emit
    shutil.copy("./dat_files/aero_emit_comp_carbo.dat",directory+"/aero_emit_comp_carbo.dat")
    shutil.copy("./dat_files/aero_emit_comp_ss1.dat",directory+"/aero_emit_comp_ss1.dat")
    shutil.copy("./dat_files/aero_emit_comp_ss2.dat",directory+"/aero_emit_comp_ss2.dat")
    #shutil.copy("./dat_files/aero_emit_comp_dust1.dat",directory+"/aero_emit_comp_dust1.dat")
    #shutil.copy("./dat_files/aero_emit_comp_dust2.dat",directory+"/aero_emit_comp_dust2.dat")
    
    shutil.copy("./dat_files/aero_emit_dist.dat",directory+"/aero_emit_dist.dat")
    shutil.copy("./dat_files/aero_emit.dat",directory+"/aero_emit.dat")
    
    # aero_init
    shutil.copy("./dat_files/aero_init_comp.dat",directory+"/aero_init_comp.dat")
    shutil.copy("./dat_files/aero_init_dist.dat",directory+"/aero_init_dist.dat")
    
    # gas 
    shutil.copy("./dat_files/gas_back.dat",directory+"/gas_back.dat")
    shutil.copy("./dat_files/gas_emit.dat",directory+"/gas_emit.dat")
    shutil.copy("./dat_files/gas_init.dat",directory+"/gas_init.dat")
    
    # environment
    shutil.copy("./dat_files/temp.dat",directory+"/temp.dat")
    shutil.copy("./dat_files/pres.dat",directory+"/pres.dat")
    shutil.copy("./dat_files/height.dat",directory+"/height.dat")
    
    # .spec file
    shutil.copy("./dat_files/urban_plume_init.spec",directory+"/urban_plume_init.spec")
    shutil.copy("./dat_files/urban_plume_restart.spec",directory+"/urban_plume_restart.spec")
    
    # run.sh
    shutil.copy("./dat_files/1_run.sh",directory+"/1_run.sh")
