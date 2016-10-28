"""
Creates text files of min distance from star used for data_reader_tides.py
"""

import numpy as np
import glob as gb
import re

#directories = ["4Res", "4NonRes", "5Res", "5NonRes"]
#paths = ["4ResTides", "4NonResTides", "Tides", "5NonResTides"]

directories = ["4Res", "5Res"]
paths = ["4ResTides", "Tides"]

combos = []

for i in range(len(directories)):

    d = directories[i]
    files = gb.glob("../{0}/LogFiles/*.txt".format(d))
    
    for logfile in files:
        fname = re.split("d|t", logfile)
        seed = int(float(fname[-3]))#print logfile
        log = open(logfile, "r")
        for line in log:
            parsed = line.split()
            if "Star" in parsed and "collided" in parsed:
                if parsed[1] != "Star":
                    pl = parsed[1]
                elif parsed[3] != "Star":
                    pl = parsed[3]
                combos.append((paths[i], seed, pl))
                break
aa = []
mind = []

for x in combos:
    if x[0] == "5Res":
        aa.append(x)

for i in range(len(paths)):

    mind = []

    for x in combos:

        if x[0] == paths[i]:

            temp = []
            logfile = ("../{1}/LogFiles/log_seed{0}_both.txt".format(x[1], paths[i]))
            log = open(logfile, "r")
            x1,x2,x3,x4,x5 = True, True, True, True, True
            for line in log:
                parsed = line.split()
                if "c_uint(1L)" in parsed:
                    x1 = False
                if "c_uint(2L)" in parsed:
                    x2 = False
                if "c_uint(3L)" in parsed:
                    x3 = False
                if "c_uint(4L)" in parsed:
                    x4 = False
                if "c_uint(5L)" in parsed:
                    x5 = False
            if x1 == True:
                temp.append(1)
            if x2 == True:
                temp.append(2)
            if x3 == True:
                temp.append(3)
            if x4 == True:
                temp.append(4)
            if x5 == True:
                temp.append(5)

            log.close()
            print x
            print temp

            posfile = ("../{1}/PosFiles/pos_seed{0}_both.txt".format(x[1], paths[i]))
            pos = open(posfile, "r")

            m1,m2,m3,m4,m5 = 1000.0,1000.0,1000.0,1000.0,1000.0
            for line in pos:
                parsed = line.split()
                if int(parsed[1]) in temp:
                    if int(parsed[1]) == 1:
                        if float(parsed[-1]) < m1:
                            m1 = float(parsed[-2])
                    if int(parsed[1]) == 2:
                        if float(parsed[-1]) < m2:
                            m2 = float(parsed[-2])
                    if int(parsed[1]) == 3:
                        if float(parsed[-1]) < m3:
                            m3 = float(parsed[-2])
                    if int(parsed[1]) == 4:
                        if float(parsed[-1]) < m4:
                            m4 = float(parsed[-2])
                    if int(parsed[1]) == 5:
                        if float(parsed[-1]) < m5:
                            m5 = float(parsed[-2])
            if 1 in temp:
                mind.append(m1)
                print 1
            if 2 in temp:
                mind.append(m2)
                print 2
            if 3 in temp:
                mind.append(m3)
                print 3
            if 4 in temp:
                mind.append(m4)
                print 4
            if 5 in temp:
                mind.append(m5)
                print 5

            pos.close()

    mind = np.array(mind)
    d = np.transpose(mind)
    np.savetxt("Text Files/min_distances_{0}.txt".format(paths[i]), d)    
