# Information for this case

sea salt and carbonaceous aerosol (no dust) emissions: Southern Hemisphere

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

- copy from case_5
- modify "1_create_LHS_matix.py"
  - **latitude: [-89.999, -60]**
  - gas emission factor: 0-1