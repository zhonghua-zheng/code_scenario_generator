#!/bin/sh

# exit on error
set -e
# turn on command echoing
set -v

# create output folder for initial run
mkdir -p out_init
# start the initial run
../../build/partmc urban_plume_init.spec &> run_init.log

# create output folder for restart run
mkdir -p out
# start the restart run
../../build/partmc urban_plume_restart.spec &> run_restart.log

# run the postprocessing 
../../build/get_var &> get_var.log
../../build/get_chi &> get_chi.log

