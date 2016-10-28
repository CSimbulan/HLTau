"""
To get the text files for this script, run inc_reader.py, data_extractor_mutual_inc.py
and data_extractor_sampled_e_and_inc.py
This generates inclination_histogram.png and obliquities plot
"""


import glob as gb
import numpy as np
import pylab as p
import matplotlib.ticker as tk
import matplotlib as mlab
import scipy.stats as st

mini5 = list(np.loadtxt("Text Files/min_inclinations_Tides.txt", unpack = True)*180./np.pi)
mini4 = list(np.loadtxt("Text Files/min_inclinations_Tides.txt", unpack = True)*180./np.pi)

mininr = list(np.loadtxt("Text Files/min_inclinations_5NonResTides.txt", unpack = True)*180./np.pi)
mininr4 = list(np.loadtxt("Text Files/min_inclinations_5NonResTides.txt", unpack = True)*180./np.pi)

sampi = list(np.loadtxt("Text Files/sampled_incs_Tides.txt", unpack = True)*180./np.pi)
sampinr = list(np.loadtxt("Text Files/sampled_incs_5NonResTides.txt", unpack = True)*180./np.pi)
sampi4 = list(np.loadtxt("Text Files/sampled_incs_4ResTides.txt", unpack = True)*180./np.pi)
sampinr4 = list(np.loadtxt("Text Files/sampled_incs_4NonResTides.txt", unpack = True)*180./np.pi)

fig1 = p.figure()
bins  = np.arange(0, 200, 20)

ax1 = fig1.add_subplot(1,1,1)
ax1.set_xlabel("inc (rad)")
ax1.set_ylabel("n")
ax1.hist(sampi + sampi4, bins = bins, histtype = "step", normed = True, label = "Sampled Over All Time")
##counts, bins, patches = ax1.hist(mini, bins = 5, histtype = "step", normed = True, label = "At Time of min_d <= 0.1 AU (survivors)")
ax1.hist(mini4 + mini5, bins = bins, histtype = "step", normed = True, label = "At Time of $d_{min} \leq 0.1$ AU (all)")
ax1.legend(fontsize = "x-large")
ax1.grid()
ax1.tick_params(labelsize = "large")
ax1.set_xlabel("inc (deg)", fontsize="x-large")
ax1.set_ylabel("n (<deg)", fontsize="x-large")
ax1.set_ylim(0, 0.02)

res4inc = np.loadtxt("Text Files/sampled_inclinations_4Res.txt", unpack = True)*180./np.pi
nonres4inc = np.loadtxt("Text Files/sampled_inclinations_4NonRes.txt", unpack = True)*180./np.pi
res5inc = np.loadtxt("Text Files/sampled_inclinations_5Res.txt", unpack = True)*180./np.pi
nonres5inc = np.loadtxt("Text Files/sampled_inclinations_5NonRes.txt", unpack = True)*180./np.pi

res4minc = np.loadtxt("Text Files/mutual_incs_4Res.txt", unpack = True)
nonres4minc = np.loadtxt("Text Files/mutual_incs_4NonRes.txt", unpack = True)
res5minc = np.loadtxt("Text Files/mutual_incs_5Res.txt", unpack = True)
nonres5minc = np.loadtxt("Text Files/mutual_incs_5NonRes.txt", unpack = True)

fig2 = p.figure()
p.subplots_adjust(hspace = 0.5)
ax2 = fig2.add_subplot(1,1,1)

bins = np.arange(0, 100, 5)

#ax1.hist(res4inc, bins = 20, histtype = "step", label = "4P Res")
#ax1.hist(nonres4inc, bins = 20, histtype = "step", label = "4P NonRes")
ax2.hist(list(res4inc) + list(res5inc) + list(nonres4inc) + list(nonres5inc), bins = bins, histtype = "step", label = "Absolute Inclination", normed = True)
ax2.hist(list(res4minc) + list(res5minc) + list(nonres4minc) + list(nonres5minc), bins = bins, histtype = "step", label = "Mutual Inclination", normed = True)

ax2.legend(fontsize = "xx-large")
ax2.grid()
ax2.set_xlabel("inc (deg)", fontsize = "x-large")
ax2.set_ylabel("n (<inc)", fontsize = "x-large")
ax2.tick_params(lablesize="large")



p.show()
