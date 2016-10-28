"""
Creates plot of cumulative distribution of min distance from star
Get data from 
"""

import glob as gb
import numpy as np
import pylab as p
import matplotlib.ticker as tk
import matplotlib as mlab
import matplotlib.lines as mlines
import scipy.stats as st

n_p = 5

mind = np.loadtxt("Text Files/min_distances_Tides.txt", unpack = True)
mindnr = np.loadtxt("Text Files/min_distances_4ResTides.txt", unpack = True)

eo = np.loadtxt("Text Files/rv_ecc", skiprows = 2)
exoa = np.loadtxt("Text Files/exoplanets_a", skiprows = 2)
exoe = np.loadtxt("Text Files/exoplanets_e", skiprows = 2)

print min(mind)
print max(mind)


fig2 = p.figure()
#fig2.suptitle("Cumulative Distribution for 5 Planet Systems")
xx = [x for x in mind if x <= 0.2]
xxnr = [x for x in mindnr if x <=0.2]


ax4 = fig2.add_subplot(1,1,1)
#ax4.set_title("Mininum = Distance from Host Star")
c, b, pa = ax4.hist(xx + xxnr, bins = 10000, cumulative= True, normed = 1, histtype = "step", visible = False)
##c2, b2, pa2 = ax4.hist(xx, bins = 10000, cumulative= True, normed = 1, histtype = "step", visible = False)
ax4.plot(b[:-1], c, "b")
##ax4.plot(b2[:-1], c2, "r")
ax4.grid()
ax4.set_xlim(b[0], 0.2)
##ax4.set_xscale("log")
ax4.tick_params(axis ="both", labelsize = "large")
ax4.xaxis.set_major_formatter(tk.OldScalarFormatter())
ax4.xaxis.major.formatter._useMathText = True
ax4.yaxis.set_major_formatter(tk.OldScalarFormatter())
ax4.set_xlabel("$r_{min}$", fontsize = "x-large")
ax4.set_ylabel("n$(<r_{min})$", fontsize = "x-large")
#ax4.legend(loc = "lower right")

p.show()
