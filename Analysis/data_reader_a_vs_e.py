""""
Generates a vs e and a vs inc plots for 4Nonres, 4res, 5nonres, and 5res cases
"""

import glob as gb
import numpy as np
import pylab as p
import matplotlib.ticker as tk
import matplotlib as mlab
import matplotlib.lines as mlines
import scipy.stats as st

n_p = 5

class stats:

    def __init__(self, name):

        self.name = name
        self.pa1, self.pe1, self.pi1 = [], [], []
        self.pa2, self.pe2, self.pi2 = [], [], []
        self.pa3, self.pe3, self.pi3 = [], [], []
        self.pa4, self.pe4, self.pi4 = [], [], []
        self.pa5, self.pe5, self.pi5 = [], [], []

    def getdata(self):

        self.a, self.e, self.inc, self.ids = np.loadtxt("Text Files/{0}_orbital_elements_1000.txt".format(self.name), unpack = True)

    def sort(self):

        for i in range(len(self.ids)):
            if int(self.ids[i]) == 1:
                self.pa1.append(self.a[i])
                self.pe1.append(self.e[i])
            elif int(self.ids[i]) == 2:
                self.pa2.append(self.a[i])
                self.pe2.append(self.e[i])
            elif int(self.ids[i]) == 3:
                self.pa3.append(self.a[i])
                self.pe3.append(self.e[i])
            elif int(self.ids[i]) == 4:
                self.pa4.append(self.a[i])
                self.pe4.append(self.e[i])
            elif int(self.ids[i]) == 5:
                self.pa5.append(self.a[i])
                self.pe5.append(self.e[i])
            else:
                pass

def extract(stats):
    
    seeds = np.arange(1,101,1)

    if stats.name[0] == "4":
        n_p = 4
    else:
        n_p = 5
    for seed in seeds:
        log = open("../{0}/LogFiles/log_seed{1}.txt".format(stats.name, seed), "r")
        col_count = 0
        ej_count = 0
        mp_count = 0
        for line in log:
            parsed = line.split()
            if "collided" in parsed and "Star" not in parsed:
                col_count += 1
            elif "ejected" in parsed:
                ej_count += 1
            elif "Star" in parsed and "collided" in parsed:
                mp_count += 1
        Npl = (n_p - col_count - ej_count - mp_count)

        log.close()

        datafile = open("../{0}/DataFiles/data_seed{1}.txt".format(stats.name, seed), "r")
        data = datafile.readlines()

        
        for line in data[-Npl:]:
            parsed = line.split()
            if Npl == 1:
                stats.pa1.append(float(parsed[1]))
                stats.pe1.append(float(parsed[2]))
                stats.pi1.append(float(parsed[3]))
            elif Npl == 2:
                stats.pa2.append(float(parsed[1]))
                stats.pe2.append(float(parsed[2]))
                stats.pi2.append(float(parsed[3]))
            elif Npl == 3:
                stats.pa3.append(float(parsed[1]))
                stats.pe3.append(float(parsed[2]))
                stats.pi3.append(float(parsed[3]))
            elif Npl == 4:
                stats.pa4.append(float(parsed[1]))
                stats.pe4.append(float(parsed[2]))
                stats.pi4.append(float(parsed[3]))
            elif Npl == 5:
                stats.pa5.append(float(parsed[1]))
                stats.pe5.append(float(parsed[2]))
                stats.pi5.append(float(parsed[3]))
        datafile.close()

res4 = stats("4Res")
nonres4 = stats("4NonRes")
res5 = stats("5Res")
nonres5 = stats("5NonRes")

extract(res4)
extract(nonres4)
extract(res5)
extract(nonres5)

eo = np.loadtxt("Text Files/rv_ecc", skiprows = 2)
exoa = np.loadtxt("Text Files/exoplanets_a", skiprows = 2)
exoe = np.loadtxt("Text Files/exoplanets_e", skiprows = 2)

if n_p == 4:
    colors = ["r", "#ff9933", "#d2d22d", "b", "w"]
elif n_p == 5:
    colors = ["r", "#ff9933", "#d2d22d", "g", "#33ccff", "b", "#9933ff", "#ff00ff"]

fig4 = p.figure()
p.title("Semi-major Axis vs. Eccentricity (4 Planet Systems)")
p.plot(res4.pa1, res4.pe1, markeredgecolor = colors[0], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "1P")
p.plot(res4.pa2, res4.pe2, markeredgecolor = colors[2], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "2P")
p.plot(res4.pa3, res4.pe3, markeredgecolor = colors[3], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "3P")
p.plot(res4.pa4, res4.pe4, markeredgecolor = colors[5], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "4P")
p.plot(nonres4.pa1, nonres4.pe1, markeredgecolor = colors[0], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None")
p.plot(nonres4.pa2, nonres4.pe2, markeredgecolor = colors[2], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None")
p.plot(nonres4.pa3, nonres4.pe3, markeredgecolor = colors[3], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None")
p.plot(nonres4.pa4, nonres4.pe4, markeredgecolor = colors[5], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None")
##p.plot(exoa, exoe, markeredgecolor = "k", marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "Observed")
p.xscale("log")
p.xlabel("a (AU)")
p.ylabel("e")
p.grid()
p.legend(fontsize = "small")

fig5 = p.figure()
p.title("Semi-major Axis vs. Inclination (4 Planet Systems)")
p.plot(res4.pa1, res4.pi1, markeredgecolor = colors[0], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "1P Res")
p.plot(res4.pa2, res4.pi2, markeredgecolor = colors[2], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "2P Res")
p.plot(res4.pa3, res4.pi3, markeredgecolor = colors[3], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "3P Res")
p.plot(res4.pa4, res4.pi4, markeredgecolor = colors[5], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "4P Res")
p.plot(nonres4.pa1, np.array(nonres4.pi1) * 180 / np.pi, markeredgecolor = colors[0], marker = "*", markersize = 15, markerfacecolor = "None", linestyle = "None", label = "1P Non-Res")
p.plot(nonres4.pa2, np.array(nonres4.pi2) * 180 / np.pi, markeredgecolor = colors[2], marker = "*", markersize = 15, markerfacecolor = "None", linestyle = "None", label = "2P Non-Res")
p.plot(nonres4.pa3, np.array(nonres4.pi3) * 180 / np.pi, markeredgecolor = colors[3], marker = "*", markersize = 15, markerfacecolor = "None", linestyle = "None", label = "3P Non-Res")
p.plot(nonres4.pa4, np.array(nonres4.pi4) * 180 / np.pi, markeredgecolor = colors[5], marker = "*", markersize = 15, markerfacecolor = "None", linestyle = "None", label = "4P Non-Res")
p.xscale("log")
p.xlabel("a (AU)")
p.ylabel("inc (deg)")
p.grid()
p.legend(fontsize = "small")

fig7 = p.figure()
p.title("Semi-major Axis vs. Eccentricity (5 Planet Systems)")
p.plot(res5.pa1, res5.pe1, markeredgecolor = colors[0], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "1P")
p.plot(res5.pa2, res5.pe2, markeredgecolor = colors[2], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "2P")
p.plot(res5.pa3, res5.pe3, markeredgecolor = colors[3], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "3P")
p.plot(res5.pa4, res5.pe4, markeredgecolor = colors[5], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "4P")
p.plot(nonres5.pa1, nonres5.pe1, markeredgecolor = colors[0], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None")
p.plot(nonres5.pa2, nonres5.pe2, markeredgecolor = colors[2], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None")
p.plot(nonres5.pa3, nonres5.pe3, markeredgecolor = colors[3], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None")
p.plot(nonres5.pa4, nonres5.pe4, markeredgecolor = colors[5], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None")
##p.plot(exoa, exoe, markeredgecolor = "k", marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "Observed")
p.xscale("log")
p.xlabel("a (AU)")
p.ylabel("e")
p.grid()
p.legend(fontsize = "small")

fig8 = p.figure()
p.title("Semi-major Axis vs. Inclination (5 Planet Systems)")
p.plot(res5.pa1, np.array(res5.pi1) * 180 / np.pi, markeredgecolor = colors[0], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "1P")
p.plot(res5.pa2, np.array(res5.pi2) * 180 / np.pi, markeredgecolor = colors[2], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "2P")
p.plot(res5.pa3, np.array(res5.pi3) * 180 / np.pi, markeredgecolor = colors[3], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "3P")
p.plot(res5.pa4, np.array(res5.pi4) * 180 / np.pi, markeredgecolor = colors[5], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None", label = "4P")
p.plot(nonres5.pa1, np.array(nonres5.pi1) * 180 / np.pi, markeredgecolor = colors[0], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None")
p.plot(nonres5.pa2, np.array(nonres5.pi2) * 180 / np.pi, markeredgecolor = colors[2], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None")
p.plot(nonres5.pa3, np.array(nonres5.pi3) * 180 / np.pi, markeredgecolor = colors[3], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None")
p.plot(nonres5.pa4, np.array(nonres5.pi4) * 180 / np.pi, markeredgecolor = colors[5], marker = "o", markersize = 10, markerfacecolor = "None", linestyle = "None")
p.xscale("log")
p.xlabel("a (AU)")
p.ylabel("inc (deg)")
p.grid()
p.legend(fontsize = "small")

p.show()


