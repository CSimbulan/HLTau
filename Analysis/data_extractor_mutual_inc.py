"""
This generates text files for the mutual inclination used for data_reader_incs.py
(figure with histograms of mutual and absolute inclinations)
"""

import numpy as np
import itertools

def n(p):
    return p.y*p.vz - p.z*p.vy, p.z*p.vx-p.x*p.vz, p.x*p.vy - p.y*p.vx

def mutualinc(p1, p2):
    nx1, ny1, nz1 = n(p1)
    nx2, ny2, nz2 = n(p2)
    dot = nx1*nx2 + ny1*ny2 + nz1*nz2
    n1 = np.sqrt(nx1**2 + ny1**2 + nz1**2)
    n2 = np.sqrt(nx2**2 + ny2**2 + nz2**2)
    return np.arccos(dot/n1/n2)

class Planet:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        
paths = ["4Res", "4NonRes", "5Res", "5NonRes"]
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

for path in paths:
    
    m_inc = []
    for seed in range(1, 101):

        if (path, seed) not in exclude:
        
            posfile = open("../{0}/PosFiles/pos_seed{1}.txt".format(path, seed), "r")
            lines = posfile.readlines()
            ctr = 0
            current_t = 1.0        
            
            planarplanet = Planet(1.,0.,0.,0.,1.,0.)
            for i in range(len(lines)):
                
                parsed = lines[i].split()
                t = float(parsed[0])
                
                if t >= 4.0e9:
                
                    if t != current_t:
                        current_t = t
                        ctr += 1
                        if ctr == 100:
                            planets = []
                            ninclined=0
##                            print float(parsed[0]), t, current_t,i,path,seed
                            star = Planet(float(parsed[2]),float(parsed[3]),float(parsed[4]),
                                          float(parsed[5]),float(parsed[6]),float(parsed[7]))
                            try:              
                                parsed1 = lines[i+1].split()
                                if float(parsed1[0]) == current_t:
                                    planets.append(Planet(float(parsed1[2])-star.x,float(parsed1[3])-star.y,float(parsed1[4])-star.z,
                                                          float(parsed1[5])-star.vx,float(parsed1[6])-star.vy,float(parsed1[7])-star.vz))
                                    inc = mutualinc(planarplanet, planets[-1])
                                    if inc > 50.:
                                            ninclined += 1
                            except:
                                pass
                            try:
                                parsed2 = lines[i+2].split()
                                if float(parsed2[0]) == current_t:
                                    planets.append(Planet(float(parsed2[2])-star.x,float(parsed2[3])-star.y,float(parsed2[4])-star.z,
                                                      float(parsed2[5])-star.vx,float(parsed2[6])-star.vy,float(parsed2[7])-star.vz))
                                    inc = mutualinc(planarplanet, planets[-1])
                                    if inc > 50.:
                                            ninclined += 1
                            except:
                                pass
                            try:
                                parsed3 = lines[i+3].split()
                                if float(parsed3[0]) == current_t:
                                    planets.append(Planet(float(parsed3[2])-star.x,float(parsed3[3])-star.y,float(parsed3[4])-star.z,
                                                      float(parsed3[5])-star.vx,float(parsed3[6])-star.vy,float(parsed3[7])-star.vz))
                                    inc = mutualinc(planarplanet, planets[-1])
                                    if inc > 50.:
                                            ninclined += 1
                            except:
                                pass
                            try:
                                parsed4 = lines[i+4].split()
                                if float(parsed4[0]) == current_t:
                                    planets.append(Planet(float(parsed4[2])-star.x,float(parsed4[3])-star.y,float(parsed4[4])-star.z,
                                                      float(parsed4[5])-star.vx,float(parsed4[6])-star.vy,float(parsed4[7])-star.vz))
                                    inc = mutualinc(planarplanet, planets[-1])
                                    if inc > 50.:
                                            ninclined += 1
                            except:
                                pass
                            try:
                                parsed5 = lines[i+5].split()
                                if float(parsed5[0]) == current_t:
                                    planets.append(Planet(float(parsed5[2])-star.x,float(parsed5[3])-star.y,float(parsed5[4])-star.z,
                                                      float(parsed5[5])-star.vx,float(parsed5[6])-star.vy,float(parsed5[7])-star.vz))
                                    inc = mutualinc(planarplanet, planets[-1])
                                    if inc > 50.:
                                            ninclined += 1
                            except:
                                pass
                            N = len(planets)+1
                            for k,j in itertools.combinations(range(N-1), r=2):
                                m_inc.append(mutualinc(planets[k], planets[j])*180./np.pi)
                                if ninclined >1:
                                    print(m_inc[-1])
                            ctr = 0
        else:
            print "Skipping ({0}, {1})".format(path, seed)
        posfile.close()
    m_inc = np.array(m_inc)
    d = np.transpose(m_inc)
    np.savetxt("Text Files/mutual_incs_{0}.txt".format(path), d)
            
