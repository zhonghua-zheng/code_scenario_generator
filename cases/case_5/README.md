# Information for this case

sea salt and carbonaceous aerosol (no dust) emissions: Northern Hemisphere

- Add an additional mode with the following parameters:
  - Dpg ranges between 0.015 - 0.053 micrometer
  - sigma_g = 1.6 (constant)
  - Emission flux between 0 and 2*10^8 1/(m^2 * s)
  - composition is 100% SO4

- Add another additional mode with the same ranges/parameters
  - but composition is 100% sea salt
- More detail: we want the sea salt and the sulfate externally mixed. In MAM4 they are internally mixed, but that’s not what they should be. 

--------

What has been changed:

- copy from case_1
- modify "1_create_LHS_matix.py"
  - **latitude: [60, 89.999]**
  - gas emission factor: 0-1
  - Dg_seasalt\_\*, sigmag_seasalt\_\*, Ea_seasalt_*
  - Dg_sulfate\_\*, sigmag_sulfate\_\*, Ea_sulfate_*
  - Copy the new files ("aero_emit_comp_Aitken_seasalt", "aero_emit_comp_Aitken_sulfate")
- modify "2_create_modify_dat_spec.py" to be in line with function in "util.py" (see below)
- modify "aero_emit_dist.dat"
  - mode_name, mass_frac
- create "aero_emit_comp_Aitken_seasalt.dat"
  - Na: 0.393
  - Cl: 0.607
- create "aero_emit_comp_Aitken_sulfate.dat"
  - SO4: 1
- modify "util.py"
  - Change the function of "modify_aero_emit_dist", removed the "ss_option" and "dust_option"
- modify "1_run.sh"
  - Change the function name