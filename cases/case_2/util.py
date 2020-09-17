# %%
import numpy as np
import math
# %% Subfunction
# This function is used for modify the gas emission at certain row
def modify_gas_emit_func(flist_row, coefficient):
    flist_split_list = flist_row.split()
    flist_split_np=np.array(flist_split_list[1:],dtype=np.float64)
    #print(flist_split_np)
    
    # multiply by coefficient
    flist_split_np=np.array(flist_split_np * coefficient,dtype=np.str)
    #print(flist_split_np)
    
    # convert back to list
    flist_split_new_list_np = list(flist_split_np)
    flist_split_new_list = [str.upper("{:.4}".format(float(x))) for x in flist_split_new_list_np]

    # add the "\n" and the begining element of the original list (e.g., rate)
    flist_split_new_list.append("\n")
    flist_split_new_list.insert(0,flist_split_list[0])
    
    # join back the list
    flist_row_new = ' '.join(flist_split_new_list)
    return flist_row_new 

# This function is used for modify the temperature at a constant profile
def modify_temp_func(flist_row, coefficient):
    flist_split_list = flist_row.split()
    flist_split_np=np.array(flist_split_list[1:],dtype=np.float64)
    #print(flist_split_np)
    
    # multiply by coefficient
    flist_split_np=np.array(np.repeat(coefficient,len(flist_split_np)),dtype=np.str)
    #print(flist_split_np)
    
    # convert back to list
    flist_split_new_list = list(flist_split_np)

    # add the "\n" and the begining element of the original list (e.g., rate)
    flist_split_new_list.append("\n")
    flist_split_new_list.insert(0,flist_split_list[0])
    
    # join back the list
    flist_row_new = ' '.join(flist_split_new_list)
    return flist_row_new

# %% function aero_emit
def modify_aero_emit_comp_carbo(directory, matrix):
    f=open(directory+"/aero_emit_comp_carbo.dat", "r+")
    flist=f.readlines()
    # modify the matrix here
    flist[1] = "BC              " + "{:.4}".format(matrix[24]) + "\n"
    flist[2] = "OC              " + "{:.4}".format(1-matrix[24]) + "\n"    
    f=open(directory+"/aero_emit_comp_carbo.dat", "w+")
    f.writelines(flist)
    f.close()
    
def modify_aero_emit_comp_ss1(directory, matrix):
    f=open(directory+"/aero_emit_comp_ss1.dat", "r+")
    flist=f.readlines()
    # modify the matrix here
    flist[1] = "OC              " + "{:.4}".format(matrix[28]) + "\n"
    flist[2] = "Na              " + "{:.4}".format((1-matrix[28])*0.3856) + "\n"
    flist[3] = "Cl              " + "{:.4}".format((1-matrix[28])*0.5389) + "\n"
    flist[3] = "SO4             " + "{:.4}".format((1-matrix[28])*0.0755) + "\n"
    f=open(directory+"/aero_emit_comp_ss1.dat", "w+")
    f.writelines(flist)
    f.close()

def modify_aero_emit_comp_ss2(directory, matrix):
    # modify the filename here
    f=open(directory+"/aero_emit_comp_ss2.dat", "r+")
    flist=f.readlines()
    # modify the matrix here
    flist[1] = "OC              " + "{:.4}".format(matrix[32]) + "\n"
    flist[2] = "Na              " + "{:.4}".format((1-matrix[32])*0.3856) + "\n"
    flist[3] = "Cl              " + "{:.4}".format((1-matrix[32])*0.5389) + "\n"
    flist[3] = "SO4             " + "{:.4}".format((1-matrix[32])*0.0755) + "\n"
    f=open(directory+"/aero_emit_comp_ss2.dat", "w+")
    f.writelines(flist)
    f.close()


def modify_aero_emit_dist(directory, matrix, ss_option, dust_option):
    f=open(directory+"/aero_emit_dist.dat", "r+")
    flist=f.readlines()
    
    # carbo
    flist[4] = "num_conc " + "{:.4}".format(matrix[23]) + "                     # particle number density (#/m^2)\n"
    flist[5] = "geom_mean_diam " + "{:.4}".format(matrix[21]) + "                # geometric mean diameter (m)\n"
    flist[6] = "log10_geom_std_dev " + "{:.4}".format(math.log10(matrix[22])) + "           # log_10 of geometric std dev of diameter\n"
    
    if ss_option != None:
        # ss1
        flist[12] = "num_conc " + "{:.4}".format(matrix[27]) + "                     # particle number density (#/m^2)\n"
        flist[13] = "geom_mean_diam " + "{:.4}".format(matrix[25]) + "                # geometric mean diameter (m)\n"
        flist[14] = "log10_geom_std_dev " + "{:.4}".format(math.log10(matrix[26])) + "           # log_10 of geometric std dev of diameter\n"
        
        # ss2
        flist[20] = "num_conc " + "{:.4}".format(matrix[31]) + "                     # particle number density (#/m^2)\n"
        flist[21] = "geom_mean_diam " + "{:.4}".format(matrix[29]) + "                # geometric mean diameter (m)\n"
        flist[22] = "log10_geom_std_dev " + "{:.4}".format(math.log10(matrix[30])) + "           # log_10 of geometric std dev of diameter\n"
    else:
        for ii in range(8, 24):
            flist[ii] = ""
    
    if dust_option != None:
        # dust1
        flist[28] = "num_conc " + "{:.4}".format(matrix[35]) + "                     # particle number density (#/m^2)\n"
        flist[29] = "geom_mean_diam " + "{:.4}".format(matrix[33]) + "                # geometric mean diameter (m)\n"
        flist[30] = "log10_geom_std_dev " + "{:.4}".format(math.log10(matrix[34])) + "           # log_10 of geometric std dev of diameter\n"
        
        # dust2
        flist[36] = "num_conc " + "{:.4}".format(matrix[38]) + "                     # particle number density (#/m^2)\n"
        flist[37] = "geom_mean_diam " + "{:.4}".format(matrix[36]) + "                # geometric mean diameter (m)\n"
        flist[38] = "log10_geom_std_dev " + "{:.4}".format(math.log10(matrix[37])) + "           # log_10 of geometric std dev of diameter\n"
    else:
        for ii in range(24,40):
            flist[ii] = ""

    f=open(directory+"/aero_emit_dist.dat", "w+")
    f.writelines(flist)
    f.close()

# %% function gas
def modify_gas_emit(directory, matrix, DMS_option):
    f=open(directory+"/gas_emit.dat", "r+")
    flist=f.readlines()
    for i in range(7,24):
        flist[i]=modify_gas_emit_func(flist[i], matrix[i-3])
    if DMS_option != None:
        flist[24]=modify_gas_emit_func(flist[24], matrix[40])
    else:
        flist[24]=""
    f=open(directory+"/gas_emit.dat", "w+")
    f.writelines(flist)
    f.close()

# %% function environment
def modify_temp(directory, matrix):
    f=open(directory+"/temp.dat", "r+")
    flist=f.readlines()
    flist[3]=modify_temp_func(flist[3],"{:.6}".format(matrix[3]))
    f=open(directory+"/temp.dat", "w+")
    f.writelines(flist)
    f.close()

# %% Make spec file
def make_spec(directory, scenario_num, matrix):
    f=open(directory+"/urban_plume_init.spec", "r+")
    flist=f.readlines()   
   
    # modify the matrix here
    # flist[1] = "output_prefix out/urban_plume_" + str(scenario_num).zfill(4) + "   # prefix of output files \n"
    
    flist[27] = "rel_humidity " + "{:.4}".format(matrix[0]) + "               # initial relative humidity (1) \n"
    print("Relative Humidity", "{:.4}".format(matrix[0]))
   
    flist[28] = "latitude  " + "{:.4}".format(matrix[1]) + "                      # latitude (degrees, -90 to 90) \n"
    print("latitude  " + "{:.4}".format(matrix[1]))
    #flist[29] = "longitude " + "{:.4}".format(matrix[0]) + "                     # longitude (degrees, -180 to 180) \n"   
   
    flist[32] = "start_day " + str(int(matrix[2])) + "                   # start day of year (UTC) \n"
    print("start_day " + str(int(matrix[2])))
    
    f=open(directory+"/urban_plume_init.spec", "w+")
    f.writelines(flist)
    f.close()

# %% Make spec file
def make_spec_restart(directory, scenario_num, matrix):
    f=open(directory+"/urban_plume_restart.spec", "r+")
    flist=f.readlines()   
   
    # modify the matrix here
    # flist[1] = "output_prefix out/urban_plume_" + str(scenario_num).zfill(4) + "   # prefix of output files \n"
    restart_time_stamp = "%08i" % int(matrix[39])
    
    flist[5] = "restart_file out_init/urban_plume_0001_" + restart_time_stamp + ".nc \n"
    print("restart_file out_init/urban_plume_0001_" + restart_time_stamp + ".nc \n")
   
    flist[21] = "rel_humidity " + "{:.4}".format(matrix[0]) + "               # initial relative humidity (1) \n"
    print("Relative Humidity", "{:.4}".format(matrix[0]))
   
    flist[22] = "latitude  " + "{:.4}".format(matrix[1]) + "                      # latitude (degrees, -90 to 90) \n"
    print("latitude  " + "{:.4}".format(matrix[1]))
    #flist[29] = "longitude " + "{:.4}".format(matrix[0]) + "                     # longitude (degrees, -180 to 180) \n"   
   
    flist[26] = "start_day " + str(int(matrix[2])) + "                   # start day of year (UTC) \n"
    print("start_day " + str(int(matrix[2])))    


    f=open(directory+"/urban_plume_restart.spec", "w+")
    f.writelines(flist)
    f.close()

