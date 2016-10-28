"""
To get the text files for this script, run data_extractor.py
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
        self.pa1, self.pe1 = [], []
        self.pa2, self.pe2 = [], []
        self.pa3, self.pe3 = [], []
        self.pa4, self.pe4 = [], []
        self.pa5, self.pe5 = [], []

    def getdata(self):

        self.a, self.e, self.inc, self.ids = np.loadtxt("Text Files/{0}_orbital_elements_10002.txt".format(self.name), unpack = True)
#        self.e_avg  = np.loadtxt("Text Files/{0}_eccentricity_avg_1000.txt".format(self.name), unpack = True)
#        self.e_samp = np.loadtxt("Text Files/{0}_eccentricity_extrasamples_1000.txt".format(self.name), unpack = True)

        
#        self.e02 = np.array([x for x in self.e_samp if x >= 0.2])
        self.e03 = np.array([x for x in self.e if x >= 0.2])

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

res4 = stats("5MassVary")
nonres4 = stats("5MassVary2")
res5 = stats("5MassVary3")
nonres5 = stats("5NonRes")

res4.getdata()
nonres4.getdata()
res5.getdata()
nonres5.getdata()

eo = np.loadtxt("Text Files/rv_ecc", skiprows = 2)
exoa = np.loadtxt("Text Files/exoplanets_a", skiprows = 2)
exoe = np.loadtxt("Text Files/exoplanets_e", skiprows = 2)

fig2 = p.figure()
#fig2.suptitle("Cumulative Eccentricity Distributions for e $\geq$ 0.2")

e02 = np.array([x for x in eo if x >= 0.2])
e03 = np.array([x for x in eo if x >= 0.2])

ax4 = fig2.add_subplot(1,1,1)
countso, binso, patcheso = ax4.hist(e03, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
countsa, binsa, patchesa = ax4.hist(res4.e03, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
ax4.plot(binsa[:-1], countsa, 'b', label = "Alternating")
countsa, binsa, patchesa = ax4.hist(nonres4.e03, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
ax4.plot(binsa[:-1], countsa, 'r', label = "$U[0.3M_J$, $2.3M_J]$")
countsa5, binsa5, patchesa5 = ax4.hist(res5.e03, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
ax4.plot(binsa5[:-1], countsa5, 'g', label = "$U[0.3M_J$, $3.2M_J]$")
countsna5, binsna5, patchesna5 = ax4.hist(nonres5.e03, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
ax4.plot(binsna5[:-1], countsna5, color = '#ff9900', label = "5P Non-Resonant $1M_J$")
ax4.plot(binso[:-1], countso, 'k--', label = "Observed")
ax4.set_xlim(0,1)
ax4.grid()
ax4.set_ylim(0,1)
ax4.set_xlim(0.2,1)
ax4.tick_params(axis ="both", labelsize = "large")
ax4.xaxis.set_major_formatter(tk.OldScalarFormatter())
ax4.xaxis.major.formatter._useMathText = True
ax4.yaxis.set_major_formatter(tk.OldScalarFormatter())
ax4.set_xlabel("e", fontsize = "x-large")
ax4.set_ylabel("n(<e)", fontsize = "x-large")
ax4.legend(loc = "lower right", fontsize = "x-large")

#fig3 = p.figure()
#fig3.suptitle("Cumulative Eccentricity Distributions")

#ax5 = fig3.add_subplot(1,1,1)
#countso, binso, patcheso = ax5.hist(eo, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
#countsa, binsa, patchesa = ax5.hist(res4.e_samp, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
#ax5.plot(binsa[:-1], countsa, 'b', label = "Alternating")
#countsa, binsa, patchesa = ax5.hist(nonres4.e_samp, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
#ax5.plot(binsa[:-1], countsa, 'r', label = "$U[0.3M_J$, $2.3M_J]$")
#countsa5, binsa5, patchesa5 = ax5.hist(res5.e_samp, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
#ax5.plot(binsa5[:-1], countsa5, 'g', label = "$U[0.3M_J$, $3.2M_J]$")
#ax5.plot(binso[:-1], countso, 'k--', label = "Observed")
#ax5.set_xlim(0,1)
#ax5.grid()
#ax5.set_ylim(0,1)
#ax5.set_xlim(0,1)
#ax5.tick_params(axis ="both")
#ax5.xaxis.set_major_formatter(tk.OldScalarFormatter())
#ax5.xaxis.major.formatter._useMathText = True
#ax5.yaxis.set_major_formatter(tk.OldScalarFormatter())
#ax5.set_xlabel("e")
#ax5.set_ylabel("n(<e)")
#ax5.legend(loc = "lower right")

p.show()

d1, p1 = st.ks_2samp(res5.e03, nonres5.e03)
print ("ks test for 5MassVary3 vs 5nonres ", p1)
d2, p2 = st.ks_2samp(res5.e03, res4.e03)
print ("ks test for 5MassVary3 vs 5MassVary ", p2)
d3, p3 = st.ks_2samp(res5.e03, nonres4.e03)
print ("ks test for 5MassVary3 vs 5MassVary2 ", p3)
d4, p4 = st.ks_2samp(nonres5.e03, res4.e03)
print ("ks test for 5NonRes vs 5MassVary ", p4)
d5, p5 = st.ks_2samp(nonres5.e03, nonres4.e03)
print ("ks test for 5NonRes vs 5MassVary2 ", p5)
d6, p6 = st.ks_2samp(res4.e03, nonres4.e03)
print ("ks test for 5MassVary vs 5MassVary2 ", p6)


dd1, pp1 = st.ks_2samp(res5.e03, e03)
print ("ks test for 5MassVary3 vs obs ", pp1)
dd1, pp2 = st.ks_2samp(nonres5.e03, e03)
print ("ks test for 5NonRes vs obs ", pp2)
dd1, pp3 = st.ks_2samp(res4.e03, e03)
print ("ks test for 5MassVary vs obs ", pp3)
dd1, pp4 = st.ks_2samp(nonres4.e03, e03)
print ("ks test for 5MassVary2 vs obs ", pp4)
