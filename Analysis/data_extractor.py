import glob as gb
import numpy as np
import pylab as p

def extract_reg(max_a, nt):

    ## Change path
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
    print "Finished extracting for {0} set with a < {1}.\n".format(nt, max_a)

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
    np.savetxt("Text Files/{1}_eccentricity_avg_{0}.txt".format(max_a, nt), c)
    np.savetxt("Text Files/{1}_eccentricity_extrasamples_{0}.txt".format(max_a, nt), d)

##extract_reg(1000, "4Res")
##extract_reg(10, "4Res")
##extract_reg(20, "4Res")
##extract_reg(50, "4Res")
##extract_reg(1000, "4NonRes")
##extract_reg(10, "4NonRes")
##extract_reg(20, "4NonRes")
##extract_reg(50, "4NonRes")
##extract_reg(1000, "5Res")
##extract_reg(10, "5Res")
##extract_reg(20, "5Res")
##extract_reg(50, "5Res")
##extract_reg(1000, "5NonRes")
##extract_reg(10, "5NonRes")
##extract_reg(20, "5NonRes")
##extract_reg(50, "5NonRes")
##extract_reg(1000, "5MassVary")
##extract_reg(10, "5MassVary")
##extract_reg(20, "5MassVary")
##extract_reg(50, "5MassVary")
##extract_reg(1000, "5MassVary2")
##extract_reg(10, "5MassVary2")
##extract_reg(20, "5MassVary2")
##extract_reg(50, "5MassVary2")
##extract_reg(1000, "4TenMJ")
##extract_reg(10, "4TenMJ")
##extract_reg(20, "4TenMJ")
##extract_reg(50, "4TenMJ")
##extract_reg(1000, "5MassVary3")
##extract_reg(10, "5MassVary3")
##extract_reg(20, "5MassVary3")
##extract_reg(50, "5MassVary3")
##extract_reg(1000, "Tides")
##extract_reg(10, "Tides")
##extract_reg(20, "Tides")
##extract_reg(50, "Tides")
##extract_reg(1000, "NonResTides")
##extract_reg(10, "NonResTides")
##extract_reg(20, "NonResTides")
##extract_reg(50, "NonResTides")



