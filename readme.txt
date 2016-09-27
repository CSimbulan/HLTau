The "Main" folder contains the python scripts used to run the simulations.

	- hltau.py is the main script. To run it in a command line, type "python hltau" and additional arguments: seed nummber (integer), # of planets ("4p" or "5p")
	  and resonant or not ("res" or nothing"). For example: "python hltau.py 1 5p res" or "python hltau.py 2 4p"

	- res_setup.py is the script to move the outer planets into resonance. Running it is similar to above but do not include resonant argument.

	- hltau_tides.py is the script to run for loading checkpoints with planets reaching within 0.2 AU of the star and includes tidal precession and general relativity.
	  Running is the same as hltau.py.

	- cleaner.py clears all the folders containing data from the simulations. Add an additional argument (anything) to regenerate empty folders.

	- four main folders are "DataFiles", "LogFiles", "PosFiles", and "SaveStates"

	- DataFiles folder contains txt files with data in the following order (columns): time, semimajor axis, eccentricity, inclination, Omega, omega,
	  angle along orbit, energy error, planet ID, and pericenter (only in simulations from hltau_tides.py)

	- LogFiles contains txt files containing a log of what happens in the simulations, starting with the initial conditions, then anytime
	  the simulation reloads from a checkpoint, any collisions/ejects as well as the time it occurs.

	- PosFiles contains txt files with data in the following order (columns): time, planet ID, x position, y position, z position, x velocity,
	  y velocity, z velocity, mass, and in simulations from hltau_tides.py two additional columns: minimum distance reached from the star and inclination
	  at that distance.

	- SaveStates contains binary files that are checkpoints for the simulations. Each simulations will produce: a binary at the start of the simulation,
	  a binary at the last output step, and a binary for each time a planet collides with the star (0.2 AU for hltau.py)

	- CloseParticleStates contains txt files of the positions and velocities of the planets in simulations that had a planet reach 0.2 AU from the star.
	  These were taken by loading the binaries mentioned above, and saving the t,x,y,z,vx,vy,vz,m into a textfile. This was necessary as everytime rebound
	  updates, the format of the binary file would change.  

	- StartFiles4 and StartFiles5 contains the initial x,y,z,vx,vy,vz of planets after res_setup.py

The "Analysis" folder contains python scripts to mine the data and generate plots used in the paper. All paths in the script files will need to be changed.

	- data_extractor.py is used to read all the files from "DataFiles" folder, and make a single text file of all the final eccentricities as well
	  as the average eccentricity of the last billion years, and the eccentricities sampled at 100 even points across the final billion years.
	  The text files will save into the "Text Files" folder.

	- data_reader_avse.py is used to generate the scatter plot of semimajor axis vs eccentricity.
	
	- log_reader.py is used to read all the log files, check for number of collisions and ejections as well as the distribution of times at which they occur.

	- data_reader_0.2.py reads the text files generated from data_extractor.py and creates the cumulative distribution of eccentricities.

	- data_reader_4p.py and data_reader_5p.py do the same but look at each case in more detail (not used in paper)

	- element_plot.py is used to generate time evolution plots for a, e, and inc from a single simulation (not used in paper)

	- element_plot_close_all.py is used to generate time evolution of eccentriciy for all simulations.

	- tide_search.py is used to make the cumulative distribution of the minimum distance reached from the star.

	- visual_test.py shows an animation of the simulation using the positions from PosFiles. Trails seem to only show in Windows.

