#Phase Diagrams for Magrathea v2: A planetary interior modeling platform in C++ submitted to JOSS

Planets on each plot are 1 Earth-mass with 100% of the mass in the layer of the diagram (hydrosphere, mantle, mantle (with carbon phase diagram)).

Example for mode0 below. For first panel: mass_of_hydro=1.0. For second panel: mass_of_mantle=1.0, mass_of_hydro=1.0. For third panel: mass_of_mantle=1.0, mass_of_hydro=1.0, mantle_phasedgm="C_simple".

Example mode0.cfg
#Input Mode 0 inputs
input_mode=0
mass_of_core=0.0	# Earth Masses in core
mass_of_mantle=0.0	# Earth Masses in mantle
mass_of_hydro=1.0	# Earth Masses in hydrosphere
mass_of_atm=0.0		# Earth Masses in atmosphere
surface_temp=300	# Kelvin, top of planet where enclosed mass equals total mass
# Below: Temperature of the outer boundary of the inner layer minus the inner boundary of the outer layer. A positive number indicates temperature increases inward. 0 indicates the temperature is continuous at the boundary of layers.
temp_jump_1=0		# Atmosphere to Hydrosphere discontinuity in K
temp_jump_2=0		# Hydrosphere to Mantle discontinuity in K
temp_jump_3=0		# Mantle to Core discontinuity in K
output_file="./result/Structure.txt"	# Output file name & location
#-------------------------------------------------------------------------------------------------------------------------------------
#Global Run Options
verbose=false				# Whether to print warnings
P_surface=1E5				# The pressure level that the broad band optical transit radius probes (in microbar)
core_phasedgm="Fe_default" 		# Phase Diagram for the core
mantle_phasedgm="Si_default"		# Phase Diagram for the mantle
hydro_phasedgm="water_default"	# Phase Diagram for the hydropshere
atm_phasedgm="gas_default"		# Phase Diagram for the atmopshere
ave_rho_core=15		# Initial guess: density of the core is 15, mantle is 5, hydrosphere is 2, and gas is 1E-3 g/cm^3
ave_rho_mantle=5
ave_rho_hydro=2
ave_rho_atm=1E-3
