"""
Creates text files for eccentricity cumulative distribution for data_reader_0.2e
and data_reader_massvary
"""

import glob as gb
import numpy as np
import pylab as p
import re

exclude = [ ("4Res", 21), ("4Res", 24), ("4Res", 28), ("4Res", 33),
            ("4Res", 4), ("4Res", 51), ("4Res", 62), ("4Res", 64),
            ("4Res", 65), ("4Res", 66), ("4Res", 67), ("4Res", 74),
            ("4Res", 85), ("4Res", 86), ("4Res", 92), ("4Res", 95),
            ("4NonRes", 11), ("4NonRes", 17), ("4NonRes", 2), ("4NonRes", 20),
            ("4NonRes", 21), ("4NonRes", 23), ("4NonRes", 24), ("4NonRes", 25),
            ("4NonRes", 30), ("4NonRes", 36), ("4NonRes", 41), ("4NonRes", 43),
            ("4NonRes", 44), ("4NonRes", 45), ("4NonRes", 48), ("4NonRes", 53),
            ("4NonRes", 59), ("4NonRes", 64), ("4NonRes", 65), ("4NonRes", 7),
            ("4NonRes", 70), ("4NonRes", 73), ("4NonRes", 74), ("4NonRes", 80),
            ("4NonRes", 84), ("4NonRes", 85), ("4NonRes", 98) ]

def extract_reg(max_a, nt):
    
    global exclude

    files = gb.glob("../{0}/DataFiles/*.txt".format(nt))

    e = []
    eavg = []
    esamp = []
    a = []
    inc = []
    ids = []
    print "Extracting orbital elements for {0} set with a < {1}...".format(nt, max_a)
    for datafile in files:
        #print datafile
        data = open(datafile, "r")
        dd = re.split("d|_|t", datafile)
        seed = int(float(dd[-3]))
#        print seed
        if (nt, seed) not in exclude:
            data = data.readlines()
            if len(data) > 0:
                cnt = 0
                ecc = [ [], [], [], [], [] ]
                t_final = float(data[-1].split()[0])
                for hash in range(-5, 0, 1):
                    line = data[hash].split()
                    if float(line[0]) == t_final and float(line[1]) < max_a:
                        a.append(float(line[1]))
                        e.append(float(line[2]))
                        esamp.append(float(line[2]))
                        inc.append(float(line[3]))
                        ids.append(float(line[-1]))
                for output in data:
                    line = output.split()
                    if float(line[0]) > 4.0e9 and float(line[1]) < max_a:
                        ecc[int(line[-1]) - 1].append(float(line[2]))
                        if cnt == 100:
                            esamp.append(float(line[2]))
                            cnt = -1
                        cnt += 1
                for ec in ecc:
                    if len(ec) > 0:
                        eavg.append(np.mean(ec))
            
        else:
            print "Skipping", (nt, seed)
    a = np.array(a)
    e = np.array(e)
    eavg = np.array(eavg)
    esamp = np.array(esamp)
    inc = np.array(inc)
    ids = np.array(ids)

    b = np.transpose((a, e, inc, ids))
    c = np.transpose((eavg))
    d = np.transpose((esamp))
    np.savetxt("Text Files/{1}_orbital_elements_{0}.txt".format(max_a, nt), b)
    print "Finished extracting for {0} set with a < {1}.\n".format(nt, max_a)
    #np.savetxt("OtherTextFiles/{1}_eccentricity_avg_{0}.txt".format(max_a, nt), c)
    #np.savetxt("OtherTextFiles/{1}_eccentricity_extrasamples_{0}.txt".format(max_a, nt), d)

extract_reg(1000, "4Res")
extract_reg(1000, "4NonRes")
extract_reg(1000, "5Res")
extract_reg(1000, "5NonRes")
extract_reg(1000, "5MassVary")
extract_reg(1000, "5MassVary2")
extract_reg(1000, "5MassVary3")




