## AST425 Rebound Simulation
## Authors: Chris Simbulan, Daniel Tamayo, Hanno Rein

## This file creates new simulations for a given seed range (first argument is start seed,
## second argument is the end seed. 

## IMPORT LIBRARIES ========================================================================================================================

import numpy as np
import rebound as reb
import reboundx as rebx
import copy
from itertools import combinations
import random
import os.path
#import matplotlib.pyplot as plt
import time as ti
import sys
from os import system
from ctypes import byref
from rebound import clibrebound

## Blank array to save to empty text file
emp = np.array([])

## Choose seed
seed = int(sys.argv[1])

## Check for resonance argument
if "res" in sys.argv:
    resonance = True
else:
    resonance = False

## Check for number of planets
if "4p" in sys.argv:
    numplanets = 4
elif "5p" in sys.argv:
    numplanets = 5
else:
    numplanets = 4

## Global min peri counter
minpericount = 1

## Global sim
sim = None
simtime = 0.0

path = "5Res"

## Add heartbeat function
ctr = 0

def heartbeat(reb_sim):
    
    global seed
    sim = reb_sim.contents
    global ctr
    maxtime = 10000
    '''
    if sim.t > 1.0e8:
        if ctr == maxtime:
            posfile = open("PosFiles/pos_seed{0}.txt".format(seed), "a")
            for i in range(len(sim.particles)):
##                posfile.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\n".format(sim.t, sim.particles[i].hash, sim.particles[i].x, sim.particles[i].y, sim.particles[i].z,
##                                                                                     sim.particles[i].vx, sim.particles[i].vy, sim.particles[i].vz, sim.particles[i].m))
                ctr2 = 0
                maxtime = sim.t/100.0
            posfile.close()
        else:
            ctr += 1
            '''

## Create function to setup bodies with initial conditions
def setup(seed, logfile):

    ## Check if system is to be in resonance
    global resonance
    global path
    global simtime

    ## Get number of planets
    global numplanets
    
    sim = reb.Simulation()
    ## Define units, although these are the default
    sim.units = ("AU", "yr", "Msun")
    Mj = 9.542e-4 # Mass of Jupiter
    Mst = 2.856e-4 # Mass of Saturn
    Mnpt = 5.149e-5 # Mass of Neptune
    M10e = 0.00003002513 # Mass of ten Earths

    ## Set distance for collision in AU
    Rj = 0.000477894503
    Rst = 0.00038925688
    Rnp = 0.0001645879
    
    ## Random Seed
    random.seed(seed)

    ## List of particle attributes
    angles = [0]
    masses = [1.0]
    radii = [0.00465047] + [Rj]*5
    incs = [0.0]
    ecc = [0.0]*6
    ids = [9,1,2,3,4,5]

    if numplanets == 5:
        a0 = (0.0, 13.2, 32.3, 64.2, 73.7, 91.0) ## ALMA positions
        #a0 = (0.0, 13.2, 32.3, 67.2, 76.7, 94.0) ## Start further out to get into resonance
    elif numplanets == 4:
        a0 = (0.0, 13.2, 32.3, 69.0, 91.0)

    ## Generate five random starting angles
    for i in range(0,5):
        angles.append(random.random()*2*np.pi)

    for j in range(0,5):
        masses = masses + [M10e]*5
            
    ## Generate random inclination angle between 0 and 1 degree        
    for i in range(0,5):
        incs.append(random.random()*np.pi/180)

    if resonance == True:
        startfile = open("CloseParticleStates/{1}_states_seed{0}.txt".format(seed, path), "r")
        lines = startfile.readlines()
        numplanets = len(lines) - 1
        data = lines[-(numplanets + 1):]
        for i in range(numplanets + 1):
            d = data[i].split()
            sim.t = float(d[0])
            sim.add(m = float(d[8]), r = radii[i], x=float(d[2]), y=float(d[3]), z=float(d[4]), vx=float(d[5]), vy=float(d[6]), vz=float(d[7]), hash=int(d[1]))
            if int(d[1]) == 9:
                logfile.write("Star added at x = {0}, y = {1}, z = {2}, with vx = {3}, vy = {4}, vz = {5}.\n\n".format(float(d[2]), float(d[3]), float(d[4]), float(d[5]), float(d[6]), float(d[7])))
            else:
                o = sim.calculate_orbits(heliocentric = True)[-1]
                logfile.write("Planet {0} added at x = {1}, y = {2}, z = {3}, with vx = {4}, vy = {5}, vz = {6}.\n".format(int(d[1]), float(d[2]), float(d[3]), float(d[4]), float(d[5]), float(d[6]), float(d[7])))    
                logfile.write("mass = {0} solar masses, a = {1} AU, e = {2}, inc = {3} degrees.\n\n".format(float(d[8]), o.a, o.e, o.inc))
        startfile.close()

    else:
        for i in range(numplanets + 1):
            if i == 0:
                sim.add(m = masses[i], r = radii[i], hash = ids[i])
                logfile.write("Star added at x = {0}, y = {1}, z = {2}, with vx = {3}, vy = {4}, vz = {5}.\n\n".format(sim.particles[i].x, sim.particles[i].y, sim.particles[i].z,
                                                                                                                     sim.particles[i].vx, sim.particles[i].vy, sim.particles[i].vz))
            else:
                sim.add(m = masses[i], r = radii[i], a = a0[i], e = ecc[i], inc = incs[i], f = angles[i], hash = ids[i])
                o = sim.calculate_orbits(heliocentric = True)[-1]
                logfile.write("Planet {0} added at x = {1}, y = {2}, z = {3}, with vx = {4}, vy = {5}, vz = {6}.\n".format(sim.particles[i].hash, sim.particles[i].x, sim.particles[i].y, sim.particles[i].z,
                                                                                                                     sim.particles[i].vx, sim.particles[i].vy, sim.particles[i].vz))
                logfile.write("mass = {0} solar masses, a = {1} AU, e = {2}, inc = {3} degrees.\n\n".format(sim.particles[i].m, o.a, o.e, o.inc))
    sim.move_to_com()

    ## Set the min pericenter
    sim.exit_min_peri = 0.2
    
    ## Save checkpoint of starting point
    checkStart = "SaveStates/HL_Tau_Seed_{0}_Start.bin".format(seed)
    sim.save(checkStart)
    
    ## Add heartbeat function
    sim.heartbeat = heartbeat
    
    return sim

## Function to merge particles
def mergeParticles(reb_sim, collision):

    global seed
    global minpericount
    global sim
    
    id1 = sim.particles[collision.p1].hash
    id2 = sim.particles[collision.p2].hash
    mergedid = min(id1, id2)
    if id1 == 9 or id2 == 9:
        if id1 == 9:
            id1 = "Star"
        if id2 == 9:
            id2 = "Star"
        if minpericount < 5:
            posfile = open("PosFiles/pos_seed{0}_both.txt".format(seed), "a")
            posfile.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\n".format(time, sim.particles[0].hash.value, sim.particles[0].x, sim.particles[0].y, sim.particles[0].z,
                                                                                 sim.particles[0].vx, sim.particles[0].vy, sim.particles[0].vz, sim.particles[0].m, 0.0))
            for i in range(len(sim.particles)):
                posfile.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\n".format(time, sim.particles[i+1].hash.value, sim.particles[i+1].x, sim.particles[i+1].y, sim.particles[i+1].z,
                                                                                     sim.particles[i+1].vx, sim.particles[i+1].vy, sim.particles[i+1].vz, sim.particles[i+1].m, sim.particles[i+1].params["min_distance"]))
            sim.save("SaveStates/HL_Tau_Seed_{0}_minperi_{1}.bin".format(seed, minpericount))
            minpericount += 1
    logfile = open("LogFiles/log_seed{0}_both.txt".format(seed), "a")
    
    logfile.write("Planets {0} and {1} have collided and merged at t = {2}.\n".format(str(id1), str(id2), sim.t))
    logfile.close()
    print ("Planets {0} and {1} have collided and merged and became Planet {2} at t = {3}.\n".format(str(id1), str(id2), mergedid, sim.t))
    sim.move_to_com()
    return clibrebound.reb_collision_resolve_merge(reb_sim, collision)
    
## Define function to eject particles
def ejectParticle(sim, time, seed, logfile):    

    max_d2 = 1000.

    for p in sim.particles:
        d2 = p.x*p.x + p.y*p.y + p.z*p.z
        if d2>max_d2:
            max_d2 = d2
            mid = p.hash
    sim.remove(hash=mid)
    sim.move_to_com()
    
    if mid != 9:
        logfile.write("Planet {0} has been ejected at t = {1}.\n".format(str(mid), sim.t))
        print ("Planet {0} has been ejected at t = {1}.\n".format(str(mid), sim.t))
    return None

## MAIN FUNCTION ===========================================================================================================================

def hltau(seed):

    global sim
    global simtime

    ## Constants
    Mearth = 0.000003002513
    Mj = 9.542e-4 # Mass of Jupiter

    ## Cutoff off
    tcutoff = 4.0e7

    ## Switch to stop recording large eccentricities and inclinations
    e_switch = True
    inc_switch = True
    rebx_switch = False

    ## Strings for names of files
    dataName = "DataFiles/data_seed{0}_both.txt".format(seed)
    logName = "LogFiles/log_seed{0}_both.txt".format(seed)
    checkPoint = "SaveStates/HL_Tau_Seed_{0}_both.bin".format(seed)
    checkPrev = "SaveStates/HL_Tau_Seed_{0}_prev_both.bin".format(seed)
    posPath = "PosFiles/pos_seed{0}_both.txt".format(seed)

    print ("Seed {0} Simulation\n\n".format(seed))
    ## Check if log file exists, if not, create a blank text file
    if (os.path.exists(logName) == False):
        np.savetxt(logName, emp)

    ## Check if data file exists, if not, create a blank text file    
    if (os.path.exists(dataName) == False):
        np.savetxt(dataName, emp)

    ## Check if position file exists, if not, create a blank text file    
    if (os.path.exists(posPath) == False):
        np.savetxt(posPath, emp)

    ## Open the log, data and planet files for reading and writing
    logfile = open(logName, "a")
    datafile = open(dataName, "a")

    ## Number of outputs
    Noutputs = 10000
    ## setting this base to this value allows to extent to 5e9
    logtimes = np.logspace(0, 9, Noutputs/2, base = 11.66529039576116580894) # base = 11.958131745004017 for 5 billion
    lintimes = np.linspace(1, 4.0e9, Noutputs/2)
    temp = list(lintimes) + list(logtimes[1:-1])
    temp.sort()
    sectimes = np.linspace(4.0e9, 5.0e9, Noutputs + 1) 
    temp2 = temp + list(sectimes[1:])
    temp2.sort()
    times = np.array(temp2)

    taue0 = [-1.0e6]*5
    if numplanets == 5:
        taum0 = [8.5e5]*5
    elif numplanets == 4:
        taum0 = [6.0e5]*5
    
    ## Create simulation, check if a checkpoint exists, otherwise make a new one
    if (os.path.exists(checkPrev) == True):
        sim = reb.Simulation.from_file(checkPrev)
        sim.N_lookup = 0
        sim.allocatedN_lookup = 0
        sim._particle_lookup_table = None
        sim.heartbeat = heartbeat

        print ("\n\nSimulation for Seed {0} continuing from t = {1}\n\n".format(seed, sim.t))
        logfile.write("Simulation for Seed {0} continuing from t = {1} ==========================================================================================\n\n".format(seed, sim.t))
        ## Find where the simulation time is in the times array
##        times = np.linspace(sim.t, sim.t + 1.0e7, 1000)
        if sim.t == 0:
            tindex = 0
            tindex2 = 0

        tindex = (np.where(times > sim.t)[0][0]) + 1
        tindex2  = tindex - 1
    
        rebxtra = rebx.Extras(sim)
        tides = rebxtra.add("tides_precession")
        gr = rebxtra.add("gr")
        from reboundx import constants
        gr.params["c"] = constants.C
        sim.particles[0].params["gr_source"] = 1
        effect = rebxtra.add("track_min_distance")


        if sim.t < tcutoff:

            mod_eff = rebxtra.add("modify_orbits_forces")
            mass_effect = rebxtra.add("modify_mass")

            for part in sim.particles[1:]:
                print part.hash, part.hash.value
                part.params["tau_a"] = np.inf
                part.params["tau_e"] = taue0[part.hash.value - 1] * np.exp(times[tindex2] / 3.0e6)
                part.params["tau_mass"] = taum0[part.hash.value - 1] * np.exp(times[tindex2] / 3.0e6)

            rebx_switch = True

        for part in sim.particles[1:]:
            part.params["k1"] = 0.15
            part.params["R_tides"] = part.r
            part.params["min_distance"] = 1000.0

        
##        if sim.t < tcutoff:
##            rebxtra = rebx.Extras(sim)
##            params = rebxtra.add_modify_orbits_forces()
##            params2 = rebxtra.add_modify_mass()
##            
##            for part in sim.particles[1:]:
##                try:
##                    part.tau_a = np.inf
##                    part.tau_e = taue0[part.hash - 1] * np.exp(times[tindex2] / 3.0e6)
##                    part.tau_mass = taum0[part.hash - 1] * np.exp(times[tindex2] / 3.0e6) 
##                except:
##                    pass
            
##            rebx_switch = True
            
        ## The final time step might bug and be less than 5e9 but more
        ## than the second final step, so this condition will force it
        ## to end if it reaches there
        if (sim.t > times[-2]) and (sim.t < times[-1]):
            return sim
    else:
        logfile.write("Simulation for Seed {0} ==========================================================================================\n\n".format(seed))
        sim = setup(seed, logfile)

        ## Reboundx extras instance
        #times = np.linspace(sim.t, sim.t + 1.0e7, 1000)
        if sim.t == 0:
            tindex = 0
            tindex2 = 0
            
        tindex = (np.where(times > sim.t)[0][0]) + 1
        tindex2 = tindex - 1

        rebxtra = rebx.Extras(sim)
        tides = rebxtra.add("tides_precession")
        gr = rebxtra.add("gr")
        from reboundx import constants
        gr.params["c"] = constants.C
        sim.particles[0].params["gr_source"] = 1
        effect = rebxtra.add("track_min_distance")


        if sim.t < tcutoff:

            mod_eff = rebxtra.add("modify_orbits_forces")
            mass_effect = rebxtra.add("modify_mass")

            for part in sim.particles[1:]:
                print part.hash, part.hash.value
                part.params["tau_a"] = np.inf
                part.params["tau_e"] = taue0[part.hash.value - 1] * np.exp(times[tindex2] / 3.0e6)
                part.params["tau_mass"] = taum0[part.hash.value - 1] * np.exp(times[tindex2] / 3.0e6)
            
            rebx_switch = True
    
        for part in sim.particles[1:]:
            part.params["k1"] = 0.15
            part.params["R_tides"] = part.r
            part.params["min_distance"] = 1000.0

    rebx_switch = True
    ## Collisions
    sim.collision = "direct"
    sim.collision_resolve = mergeParticles

    ## Set distance for ejection in AU
    sim.exit_max_distance = 1000.0

    ## Calculate initial energy
    E0 = sim.calculate_energy()
    Eold = E0

    ## Close all the files
    logfile.close()
    datafile.close()

    ## Integrate the simulation
    for i,time in enumerate(times[tindex:]):

        ## Open the log, data and planet files for reading and writing
        logfile = open(logName, "a")
        datafile = open(dataName, "a")
        posfile = open(posPath, "a")
        try:
            sim.integrate(time)
        ## If a particle reaches past the max distance, treat is as ejected
        except reb.Escape as error:
            Ei = sim.calculate_energy()
            ejectParticle(sim, time, seed, logfile)
            Ef = sim.calculate_energy()
            dE = Ef - Ei
            E0 += dE

        E = sim.calculate_energy()
        Eerror = abs(E - E0)/abs(Eold)

        posfile.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\n".format(time, sim.particles[0].hash.value, sim.particles[0].x, sim.particles[0].y, sim.particles[0].z,
                                                                        sim.particles[0].vx, sim.particles[0].vy, sim.particles[0].vz, sim.particles[0].m, 0.0))

        o = sim.calculate_orbits(heliocentric = True)
        for i in range(len(o)):           
            ## Write the semi-major axis, eccentricity, and inclination to data file
            datafile.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\n".format(time, o[i].a, o[i].e,
                                                                        o[i].inc, o[i].Omega, o[i].omega, o[i].f,
                                                                             Eerror, sim.particles[i+1].hash.value, o[i].a*(1 - o[i].e)))
            posfile.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\n".format(time, sim.particles[i+1].hash.value, sim.particles[i+1].x, sim.particles[i+1].y, sim.particles[i+1].z,
                                                                       sim.particles[i+1].vx, sim.particles[i+1].vy, sim.particles[i+1].vz, sim.particles[i+1].m, sim.particles[i+1].params["min_distance"]))
            if (o[i].e > 0.999):
                if e_switch == True:
                    logfile.write("S: Seed {0}: Eccentricity over 0.999 detected at t = {1}.\n".format(seed, time))
                    e_switch = False
            if (o[i].inc > 0.7):
                if inc_switch == True:
                    logfile.write("S: Seed {0}: Inclination over 0.7 detected at t = {1}.\n".format(seed, time))
                    inc_switch = False
        
        if time > tcutoff and rebx_switch == True:
            rebxtra.remove_from_simulation(sim)
            rebx_switch  = False
        
        if time < tcutoff and rebx_switch == True:

            for part in sim.particles[1:]:
                try:
                    part.params["tau_a"] = np.inf
                    part.params["tau_e"] = float(taue0[part.hash.value - 1] * np.exp(time / 3.0e6))
                    part.params["tau_mass"] = float(taum0[part.hash.value - 1] * np.exp(time / 3.0e6))
                except:
                    pass
        #try:
        #    print time, sim.particles[-1].m/Mearth, sim.particles[-1].m/Mj
        #except:
        #    pass


        ## Close all the files
        logfile.close()
        datafile.close()
        posfile.close()

        ## Save the simulation
        sim.save(checkPoint)
        system("mv SaveStates/HL_Tau_Seed_{0}_both.bin SaveStates/HL_Tau_Seed_{0}_prev_both.bin".format(seed))
     
    logfile = open(logName, "a")    
    datafile = open(dataName, "a")

    logfile.write("Number of planets at the end of the simulation: {0}\n\n".format(sim.N - 1))
    #print("Number of particles at the end of the simulation: %d."%sim.N)

    if (sim.N - 1 == 5):
        logfile.write("S: Seed {0}: All five planets remained.\n".format(seed))
    if (sim.N - 1 == 1):
        logfile.write("S: Seed {0}: Only one planet remained.\n".format(seed))

    ## Close all the files
    logfile.close()
    datafile.close()
        
    print "Seed {0} Done.\n\n".format(seed)

    return sim

hltau(seed)
