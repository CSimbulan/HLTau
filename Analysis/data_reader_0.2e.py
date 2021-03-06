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

        self.a, self.e, self.inc, self.ids = np.loadtxt("Text Files/{0}_orbital_elements_1000.txt".format(self.name), unpack = True)
#        self.e_samp = np.loadtxt("Text Files/sampled_eccentricities_{0}.txt".format(self.name), unpack = True)

        
#        self.e02 = np.array([x for x in self.e_samp if x >= 0.2])
        self.e03 = np.array([x for x in self.e if x >= 0.2])


res4 = stats("4Res")
nonres4 = stats("4NonRes")
res5 = stats("5Res")
nonres5 = stats("5NonRes")
##tenjm = stats("4TenMj")

res4.getdata()
nonres4.getdata()
res5.getdata()
nonres5.getdata()
##tenjm.getdata()

eo = np.loadtxt("Text Files/rv_ecc", skiprows = 2)
exoa = np.loadtxt("Text Files/exoplanets_a", skiprows = 2)
exoe = np.loadtxt("Text Files/exoplanets_e", skiprows = 2)

#fig2 = p.figure()
#fig2.suptitle("Cumulative Eccentricity Distributions for e $\geq$ 0.2")

e02 = np.array([x for x in eo if x >= 0.2])
e03 = np.array([x for x in eo if x >= 0.2])

#ax4 = fig2.add_subplot(1,1,1)
#countso, binso, patcheso = ax4.hist(e02, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
#countsr4, binsr4, patchesr4 = ax4.hist(res4.e02, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
#ax4.plot(binsr4[:-1], countsr4, 'b', label = "4P Resonant $5M_J$")
#countsnr4, binsnr4, patchesnr4 = ax4.hist(nonres4.e02, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
#ax4.plot(binsnr4[:-1], countsnr4, 'b--', label = "4P Non-Resonant $5M_J$")
#ax4.plot(binso[:-1], countso, 'k--', label = "Observed")
#countsr5, binsr5, patchesr5 = ax4.hist(res5.e02, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
#ax4.plot(binsr5[:-1], countsr5, 'r', label = "5P Resonant $1M_J$")
#countsnr5, binsnr5, patchesnr5 = ax4.hist(nonres5.e02, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
#ax4.plot(binsnr5[:-1], countsnr5, 'r--', label = "5P Non-Resonant $1M_J$")
#ax4.set_xlim(0,1)
#ax4.grid()
#ax4.set_ylim(0,1)
#ax4.set_xlim(0.2,1)
#ax4.set_xlabel("e")
#ax4.set_ylabel("n(<e)")
#ax4.legend(loc = "lower right")

##fig3 = p.figure()
##fig3.suptitle("Cumulative Eccentricity Distributions")
##ax5 = fig3.add_subplot(1,1,1)
##countso, binso, patcheso = ax5.hist(eo, bins = 1000, histtype = "step", normed = 1, cumulative = True, visible = False)
##countsa, binsa, patchesa = ax5.hist(res4.e_samp, bins = 1000, histtype = "step", normed = 1, cumulative = True, visible = False)
##ax5.plot(binsa[:-1], countsa, 'b', label = "4P Resonant $5M_J$")
##countsa, binsa, patchesa = ax5.hist(nonres4.e_samp, bins = 1000, histtype = "step", normed = 1, cumulative = True, visible = False)
##countsa2, binsa2, patchesa2 = ax5.hist(tenjm.e_samp, bins = 1000, histtype = "step", normed = 1, cumulative = True, visible = False)
##ax5.plot(binsa[:-1], countsa, 'b--', label = "4P Non-Resonant $5M_J$")
##ax5.plot(binsa2[:-1], countsa2, 'g', label = "4P Resonant $10M_J$")
##ax5.plot(binso[:-1], countso, 'k--', label = "Observed")
##countsa5, binsa5, patchesa5 = ax5.hist(res5.e_samp, bins = 1000, histtype = "step", normed = 1, cumulative = True, visible = False)
##ax5.plot(binsa5[:-1], countsa5, 'r', label = "5P Resonant $1M_J$")
##countsna5, binsna5, patchesna5 = ax5.hist(nonres5.e_samp, bins = 1000, histtype = "step", normed = 1, cumulative = True, visible = False)
##ax5.plot(binsna5[:-1], countsna5, 'r--', label = "5P Non-Resonant $1M_J$")
##ax5.set_xlim(0,1)
##ax5.grid()
##ax5.set_ylim(0,1)
##ax5.tick_params(axis ="both")
##ax5.xaxis.set_major_formatter(tk.OldScalarFormatter())
##ax5.xaxis.major.formatter._useMathText = True
##ax5.yaxis.set_major_formatter(tk.OldScalarFormatter())
##ax5.set_xlabel("e")
##ax5.set_ylabel("n(<e)")
##ax5.legend(loc = "lower right")

d1, p1 = st.ks_2samp(res5.e03, nonres5.e03)
print ("ks test for 5res vs 5nonres ", p1)
d2, p2 = st.ks_2samp(res5.e03, res4.e03)
print ("ks test for 5res vs 4res ", p2)
d3, p3 = st.ks_2samp(res5.e03, nonres4.e03)
print ("ks test for 5res vs 4nonres ", p3)
d4, p4 = st.ks_2samp(nonres5.e03, res4.e03)
print ("ks test for 5nonres vs 4res ", p4)
d5, p5 = st.ks_2samp(nonres5.e03, nonres4.e03)
print ("ks test for 5rnones vs 4nonres ", p5)
d6, p6 = st.ks_2samp(res4.e03, nonres4.e03)
print ("ks test for 4res vs 4nonres ", p6)


dd1, pp1 = st.ks_2samp(res5.e03, e03)
print ("ks test for 5res vs obs ", pp1)
dd1, pp2 = st.ks_2samp(nonres5.e03, e03)
print ("ks test for 5nonres vs obs ", pp2)
dd1, pp3 = st.ks_2samp(res4.e03, e03)
print ("ks test for 4res vs obs ", pp3)
dd1, pp4 = st.ks_2samp(nonres4.e03, e03)
print ("ks test for 4nonres vs obs ", pp4)

fig3 = p.figure()
ax6 = fig3.add_subplot(1,1,1)
countso, binso, patcheso = ax6.hist(e03, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
countsr4, binsr4, patchesr4 = ax6.hist(res4.e03, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
ax6.plot(binsr4[:-1], countsr4, 'b', label = "4P Resonant $5M_J$")
countsnr4, binsnr4, patchesnr4 = ax6.hist(nonres4.e03, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
ax6.plot(binsnr4[:-1], countsnr4, 'b--', label = "4P Non-Resonant $5M_J$")
ax6.plot(binso[:-1], countso, 'k--', label = "Observed")
countsr5, binsr5, patchesr5 = ax6.hist(res5.e03, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
ax6.plot(binsr5[:-1], countsr5, 'r', label = "5P Resonant $1M_J$")
countsnr5, binsnr5, patchesnr5 = ax6.hist(nonres5.e03, bins = 100, histtype = "step", normed = 1, cumulative = True, visible = False)
ax6.plot(binsnr5[:-1], countsnr5, 'r--', label = "5P Non-Resonant $1M_J$")
ax6.set_xlim(0,1)
ax6.grid()
ax6.set_ylim(0,1)
ax6.set_xlim(0.2,1)
ax6.tick_params(labelsize = "large")
ax6.set_xlabel("e", fontsize = "x-large")
ax6.set_ylabel("n(<e)", fontsize = "x-large")
ax6.legend(loc = "lower right", fontsize = "x-large")


p.show()

