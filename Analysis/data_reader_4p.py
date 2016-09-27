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
        self.a1, self.e1, self.inc1, self.ids1 = np.loadtxt("Text Files/{0}_orbital_elements_10.txt".format(self.name), unpack = True)
        self.a2, self.e2, self.inc2, self.ids2 = np.loadtxt("Text Files/{0}_orbital_elements_20.txt".format(self.name), unpack = True)
        self.a5, self.e5, self.inc5, self.ids5 = np.loadtxt("Text Files/{0}_orbital_elements_50.txt".format(self.name), unpack = True)
        self.e_avg  = np.loadtxt("Text Files/{0}_eccentricity_avg_1000.txt".format(self.name), unpack = True)
        self.e_avg1  = np.loadtxt("Text Files/{0}_eccentricity_avg_10.txt".format(self.name), unpack = True)
        self.e_avg2  = np.loadtxt("Text Files/{0}_eccentricity_avg_20.txt".format(self.name), unpack = True)
        self.e_avg5  = np.loadtxt("Text Files/{0}_eccentricity_avg_50.txt".format(self.name), unpack = True)
        self.e_samp = np.loadtxt("Text Files/{0}_eccentricity_extrasamples_1000.txt".format(self.name), unpack = True)
        self.e_samp1 = np.loadtxt("Text Files/{0}_eccentricity_extrasamples_10.txt".format(self.name), unpack = True)
        self.e_samp2 = np.loadtxt("Text Files/{0}_eccentricity_extrasamples_20.txt".format(self.name), unpack = True)
        self.e_samp5 = np.loadtxt("Text Files/{0}_eccentricity_extrasamples_50.txt".format(self.name), unpack = True)

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

def histextra(counts, bins, patches, ax, color, color2, showpercent = True, textloc = -18):
                
    # Label the raw counts and the percentages below the x-axis...
    bin_centers = 0.5 * np.diff(bins) + bins[:-1]
    for count, x in zip(counts, bin_centers):
        # Label the raw counts
        ax.annotate(str(int(count)), xy=(x, 0), xycoords=("data", "axes fraction"),
            xytext=(0, textloc), textcoords="offset points", va="top", ha="center",
                    color = color)

        if showpercent == True:
            # Label the percentages
            percent = '{0}%'.format(int(100 * float(count) / counts.sum()))
            ax.annotate(percent, xy=(x, 0), xycoords=("data", "axes fraction"),
                xytext=(0, textloc - 14), textcoords="offset points", va="top", ha="center",
                        color = color2)
    return ax

res4 = stats("4Res")
nonres4 = stats("4NonRes")
res5 = stats("4Res")
nonres5 = stats("4NonRes")
tenjm = stats("4TenMj")

res4.getdata()
nonres4.getdata()
res5.getdata()
nonres5.getdata()
tenjm.getdata()

eo = np.loadtxt("Text Files/rv_ecc", skiprows = 2)
exoa = np.loadtxt("Text Files/exoplanets_a", skiprows = 2)
exoe = np.loadtxt("Text Files/exoplanets_e", skiprows = 2)

fig1 = p.figure()
fig1.suptitle("Orbital Element Distributions For 4 Planet Systems")
p.subplots_adjust(hspace = 0.35)

ax1 = fig1.add_subplot(1,1,1)
ax1.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax1.set_title("Semi-Major Axis Distribution")
counts, bins, patches = ax1.hist(res4.a, 20, histtype = "step", label = "Resonant")
#ax1 = histextra(counts, bins, patches, ax1, "blue", "black", False, textloc = 10)
counts, bins, patches = ax1.hist(nonres4.a, 20, color = "red", histtype = "step", label = "Non-Resonant")
#ax1 = histextra(counts, bins, patches, ax1, "red", "black", False, textloc = 24)
ax1.grid()
ax1.xaxis.set_major_formatter(tk.OldScalarFormatter())
ax1.xaxis.major.formatter._useMathText = True
ax1.yaxis.set_major_formatter(tk.OldScalarFormatter())
ax1.set_xlabel("a")
ax1.set_ylabel("n(<a)")
ax1.legend()
ax1.set_xlim(bins[0], bins[-1])

##ax2 = fig1.add_subplot(3,1,2)
##ax2.set_title("Eccentricity Distribution")
##counts, bins, patches = ax2.hist(res4.e, 20, histtype = "step", label = "Resonant")
###ax2 = histextra(counts, bins, patches, ax2, "blue", "black", False, textloc = 10)
##counts, bins, patches = ax2.hist(nonres4.e, 20, color = "red", histtype = "step", label = "Non-Resonant")
###ax2 = histextra(counts, bins, patches, ax2, "red", "black", False, textloc = 24)
##ax2.grid()
##ax2.xaxis.set_major_formatter(tk.OldScalarFormatter())
##ax2.xaxis.major.formatter._useMathText = True
##ax2.yaxis.set_major_formatter(tk.OldScalarFormatter())
##ax2.set_xlabel("e")
##ax2.set_ylabel("n(<e)")
##ax2.legend()
##
##ax12 = fig1.add_subplot(3,1,3)
##ax12.set_title("Inclination Distribution")
##counts, bins, patches = ax12.hist(res4.inc, 20, histtype = "step", label = "Resonant")
###ax2 = histextra(counts, bins, patches, ax2, "blue", "black", False, textloc = 10)
##counts, bins, patches = ax12.hist(nonres4.inc, 20, color = "red", histtype = "step", label = "Non-Resonant")
###ax2 = histextra(counts, bins, patches, ax2, "red", "black", False, textloc = 24)
##ax12.grid()
##ax12.xaxis.set_major_formatter(tk.OldScalarFormatter())
##ax12.xaxis.major.formatter._useMathText = True
##ax12.yaxis.set_major_formatter(tk.OldScalarFormatter())
##ax12.set_xlabel("inc (rad)")
##ax12.set_ylabel("n(<inc)")
##ax12.legend()

fig2 = p.figure()
fig2.suptitle("Cumulative Distributions for 4 Planet Systems")
#ax3 = fig2.add_subplot(2,1,1)
#ax3.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
#ax3.set_title("Semi-Major Axis")
#counts, bins, patches = ax3.hist(a, 10000, histtype = "step", normed = 1, cumulative = True, visible = False)
#ax3.plot(bins[:-1], counts, 'b')
#ax3.set_xlim(0, bins[-2])
#ax3.grid(color = "b")
#ax3.tick_params(axis ="both", colors = "b")
#ax3.xaxis.set_major_formatter(tk.OldScalarFormatter())
#ax3.xaxis.major.formatter._useMathText = True
#ax3.yaxis.set_major_formatter(tk.OldScalarFormatter())
#ax3.set_xlabel("a")
#ax3.set_ylabel("n(<a)")

ax4 = fig2.add_subplot(1,1,1)
ax4.set_title("Eccentricity")
#counts, bins, patches = ax4.hist(res4.e_avg, histtype = "step", normed = 1, cumulative = True, visible = False)
countsa, binsa, patchesa = ax4.hist(res4.e_samp, histtype = "step", normed = 1, cumulative = True, visible = False)
countso, binso, patcheso = ax4.hist(eo, histtype = "step", normed = 1, cumulative = True, visible = False)
#ax4.plot(bins[:-1], counts, 'b', label = "Resonant Final")
ax4.plot(binsa[:-1], countsa, 'b', label = "Resonant $5M_J$")
#counts, bins, patches = ax4.hist(nonres4.e_avg, histtype = "step", normed = 1, cumulative = True, visible = False)
countsa, binsa, patchesa = ax4.hist(nonres4.e_samp, histtype = "step", normed = 1, cumulative = True, visible = False)
countsa2, binsa2, patchesa2 = ax4.hist(tenjm.e_samp, histtype = "step", normed = 1, cumulative = True, visible = False)
#ax4.plot(bins[:-1], counts, 'r', label = "Non-Resonant Final")
ax4.plot(binsa[:-1], countsa, 'r', label = "Non-Resonant $5M_J$")
ax4.plot(binsa2[:-1], countsa2, 'g', label = "Resonant $10M_J$")
ax4.plot(binso[:-1], countso, 'k--', label = "Observed")
ax4.set_xlim(0, bins[-2])
ax4.grid()
ax4.set_ylim(0,1)
ax4.set_xlim(0, max(binsa))
ax4.tick_params(axis ="both")
ax4.xaxis.set_major_formatter(tk.OldScalarFormatter())
ax4.xaxis.major.formatter._useMathText = True
ax4.yaxis.set_major_formatter(tk.OldScalarFormatter())
ax4.set_xlabel("e")
ax4.set_ylabel("n(<e)")
ax4.legend(loc = "lower right")

fig3 = p.figure()
p.subplots_adjust(hspace = 0.8)
fig3.suptitle("Eccentricity Distribution Comparison for 4 Planet Systems")

ax5 = fig3.add_subplot(2,2,1)
ax5.set_title("All Simulated Planets")
counts, bins, patches = ax5.hist(res4.e,histtype = "step", normed = 1, cumulative = True, visible = False)
countsa, binsa, patchesa = ax5.hist(res4.e_avg,histtype = "step", normed = 1, cumulative = True, visible = False)
countsn, binsn, patchesn = ax5.hist(nonres4.e, histtype = "step", normed = 1, cumulative = True, visible = False)
countsna, binsna, patchesna = ax5.hist(nonres4.e_avg, histtype = "step", normed = 1, cumulative = True, visible = False)
countso, binso, patcheso = ax5.hist(eo,histtype = "step", normed = 1, cumulative = True, visible = False)
D, Pvalue = st.ks_2samp(res4.e, nonres4.e)
Da, Pvaluea = st.ks_2samp(res4.e_samp, eo)
Dn, Pvaluen = st.ks_2samp(nonres4.e, eo)
Dna, Pvaluena = st.ks_2samp(nonres4.e_samp, eo)
label = "D = 0.1583\nP-value = 1.25e-109"
ax5.plot(bins[:-1], counts, 'b', label = "Simulated")
ax5.plot(binsa[:-1], countsa, 'b--', label = "Simulated")
ax5.plot(binsn[:-1], countsn, 'r', label = "Simulated")
ax5.plot(binsna[:-1], countsna, 'r--', label = "Simulated")
ax5.plot(binso[:-1], countso, 'k', label = "Observed")
ax5.set_xlabel("e")
ax5.set_ylabel("n(<e)")
ax5.grid()
ax5.set_xlim(0, max(binso))

ax6 = fig3.add_subplot(2,2,2)
ax6.set_title("a < 10 AU")
counts1, bins1, patches1 = ax6.hist(res4.e1,histtype = "step", normed = 1, cumulative = True, visible = False)
countsa1, binsa1, patchesa1 = ax6.hist(res4.e_avg1,histtype = "step", normed = 1, cumulative = True, visible = False)
countsn1, binsn1, patchesn1 = ax6.hist(nonres4.e1,histtype = "step", normed = 1, cumulative = True, visible = False)
##countsna1, binsna1, patchesna1 = ax6.hist(nonres4.e_avg1, 100, histtype = "step", normed = 1, cumulative = True, visible = False)
countso1, binso1, patcheso1 = ax6.hist(eo, histtype = "step", normed = 1, cumulative = True, visible = False)
D1, Pvalue1 = st.ks_2samp(counts1, countso1)
Da1, Pvaluea1 = st.ks_2samp(countsa1, countso1)
Dn1, Pvaluen1 = st.ks_2samp(countsn1, countso1)
##Dna1, Pvaluena1 = st.ks_2samp(countsna1, countso1)
label = "D = 0.1583\nP-value = 1.25e-109"
ax6.plot(bins1[:-1], counts1, 'b', label = "Simulated")
ax6.plot(binsa1[:-1], countsa1, 'b--', label = "Simulated")
ax6.plot(binsn1[:-1], countsn1, 'r', label = "Simulated")
##ax6.plot(binsna1[:-1], countsna1, 'r--', label = "Simulated")
ax6.plot(binso1[:-1], countso1, 'k', label = "Observed")
ax6.set_xlabel("e")
ax6.set_ylabel("n(<e)")
ax6.grid()
ax6.set_xlim(0, max(binso1))

ax7 = fig3.add_subplot(2,2,3)
ax7.set_title("a < 20 AU")
counts2, bins2, patches2 = ax7.hist(res4.e2, histtype = "step", normed = 1, cumulative = True, visible = False)
countsa2, binsa2, patchesa2 = ax7.hist(res4.e_avg2, histtype = "step", normed = 1, cumulative = True, visible = False)
countsn2, binsn2, patchesn2 = ax7.hist(nonres4.e2, histtype = "step", normed = 1, cumulative = True, visible = False)
countsna2, binsna2, patchesna2 = ax7.hist(nonres4.e_avg2, histtype = "step", normed = 1, cumulative = True, visible = False)
countso2, binso2, patcheso2 = ax7.hist(eo, 100, histtype = "step", normed = 1, cumulative = True, visible = False)
D2, Pvalue2 = st.ks_2samp(counts2, countso2)
Da2, Pvaluea2 = st.ks_2samp(countsa2, countso2)
Dn2, Pvaluen2 = st.ks_2samp(countsn2, countso2)
Dna2, Pvaluena2 = st.ks_2samp(countsna2, countso2)
label = "D = 0.1583\nP-value = 1.25e-109"
ax7.plot(bins2[:-1], counts2, 'b', label = "Simulated")
ax7.plot(binsa2[:-1], countsa2, 'b--', label = "Simulated")
ax7.plot(binsn2[:-1], countsn2, 'r', label = "Simulated")
ax7.plot(binsna2[:-1], countsna2, 'r--', label = "Simulated")
ax7.plot(binso2[:-1], countso2, 'k', label = "Observed")
ax7.set_xlabel("e")
ax7.set_ylabel("n(<e)")
ax7.grid()
ax7.set_xlim(0, max(binso2))

ax8 = fig3.add_subplot(2,2,4)
ax8.set_title("a < 50 AU")
counts5, bins5, patches5 = ax8.hist(res4.e5, 100, histtype = "step", normed = 1, cumulative = True, visible = False)
countsa5, binsa5, patchesa5 = ax8.hist(res4.e_avg5, 100, histtype = "step", normed = 1, cumulative = True, visible = False)
countsn5, binsn5, patchesn5 = ax8.hist(nonres4.e5, 100, histtype = "step", normed = 1, cumulative = True, visible = False)
countsna5, binsna5, patchesna5 = ax8.hist(nonres4.e_avg5, 100, histtype = "step", normed = 1, cumulative = True, visible = False)
countso5, binso5, patcheso5 = ax8.hist(eo, 100, histtype = "step", normed = 1, cumulative = True, visible = False)
D5, Pvalue5 = st.ks_2samp(counts5, countso5)
Da5, Pvaluea5 = st.ks_2samp(countsa5, countso5)
Dn5, Pvaluen5 = st.ks_2samp(countsn5, countso5)
Dna5, Pvaluena5 = st.ks_2samp(countsna5, countso5)
label = "D = 0.1583\nP-value = 1.25e-109"
ax8.plot(bins5[:-1], counts5, 'b', label = "Simulated")
ax8.plot(binsa5[:-1], countsa5, 'b--', label = "Simulated")
ax8.plot(binsn5[:-1], countsn5, 'r', label = "Simulated")
ax8.plot(binsna5[:-1], countsna5, 'r--', label = "Simulated")
ax8.plot(binso5[:-1], countso5, 'k', label = "Observed")
ax8.set_xlabel("e")
ax8.set_ylabel("n(<e)")
ax8.grid()
ax8.set_xlim(0, max(binso5))

blueline = mlines.Line2D([], [], color='b', linestyle='-')
redline = mlines.Line2D([], [], color='r', linestyle='-')
bluedashline = mlines.Line2D([], [], color='b', linestyle='--')
reddashline = mlines.Line2D([], [], color='r', linestyle='--')
blackline = mlines.Line2D([], [], color='k', linestyle='-')

p.figlegend((blueline, bluedashline, redline, reddashline, blackline),
            ("Resonant Final", "Resonant Averaged", "Non-Resonant Final", "None-Resonant Average", "Observed"),
            loc = "center", ncol=3, fontsize = "small")

pvrf = "%.3f" % (Pvalue*100)
pvrf1 = "%.3f" % (Pvalue1*100)
pvrf2 = "%.3f" % (Pvalue2*100)
pvrf5 = "%.3f" % (Pvalue5*100)
pvra = "%.3f" % (Pvaluea*100)
pvra1 = "%.3f" % (Pvaluea1*100)
pvra2 = "%.3f" % (Pvaluea2*100)
pvra5 = "%.3f" % (Pvaluea5*100)

pvnf = "%.3f" % (Pvaluen*100)
pvnf1 = "%.3f" % (Pvaluen1*100)
pvnf2 = "%.3f" % (Pvaluen2*100)
pvnf5 = "%.3f" % (Pvaluen5*100)
pvna = "%.3f" % (Pvaluena*100)
pvna1 = 0.000#"%.3f" % (Pvaluena1*100)
pvna2 = "%.3f" % (Pvaluena2*100)
pvna5 = "%.3f" % (Pvaluena5*100)

print "KS Test Resuls:"
print "Case\t\t\t| All \t\t| a < 10 \t| a < 20 \t| a < 50"
print "--------"*11
print "4P Resonant Final \t| {0}% \t| {1}% \t| {2}% \t| {3}%".format(pvrf, pvrf1, pvrf2, pvrf5)
print "4P Resonant Averaged \t| {0}% \t| {1}% \t| {2}% \t| {3}%".format(pvra, pvra1, pvra2, pvra5)
print "4P Non-Resonant Final \t| {0}% \t| {1}% \t| {2}% \t| {3}%".format(pvnf, pvnf1, pvnf2, pvnf5)
print "4P Non-Resonant Averaged| {0}% \t| {1}% \t| {2}% \t| {3}%".format(pvna, pvna1, pvna2, pvna5)

res4.sort()
nonres4.sort()
res5.sort()
nonres5.sort()

if n_p == 4:
    colors = ["r", "#ff9933", "#d2d22d", "b", "w"]
elif n_p == 5:
    colors = ["r", "#ff9933", "#d2d22d", "g", "b"]

fig4 = p.figure()
p.title("Semi-major Axis vs. Eccentricity (5 Planet Systems)")
p.plot(res4.pa1, res4.pe1, color = colors[0], marker = "o", linestyle = "None", label = "Resonant Planet 1 Results")
p.plot(res4.pa2, res4.pe2, color = colors[1], marker = "o", linestyle = "None", label = "Resonant Planet 2 Results")
p.plot(res4.pa3, res4.pe3, color = colors[2], marker = "o", linestyle = "None", label = "Resonant Planet 3 Results")
p.plot(res4.pa4, res4.pe4, color = colors[3], marker = "o", linestyle = "None",  label = "Resonant Planet 4 Results")
p.plot(nonres4.pa1, nonres4.pe1, color = colors[0], marker = "*", linestyle = "None", markersize = 10, label = "Non-Resonant Planet 1 Results")
p.plot(nonres4.pa2, nonres4.pe2, color = colors[1], marker = "*", linestyle = "None", markersize = 10, label = "Non-Resonant Planet 2 Results")
p.plot(nonres4.pa3, nonres4.pe3, color = colors[2], marker = "*", linestyle = "None", markersize = 10, label = "Non-Resonant Planet 3 Results")
p.plot(nonres4.pa4, nonres4.pe4, color = colors[3], marker = "*", linestyle = "None", markersize = 10, label = "Non-Resonant Planet 4 Results")
p.plot(exoa, exoe, 'ko', label = "Observed Exoplanet Sample")
p.xscale("log")
p.xlabel("a (AU)")
p.ylabel("e")
p.grid()
p.legend(fontsize = "small")

fig5 = p.figure()
p.title("Cummulative Eccentriciy Distribution By Planet (4 Planet Systems)")
ax9 = fig5.add_subplot(1,1,1)
ax9.set_xlabel("e")
ax9.set_ylabel("n(<e)")
counts1, bins1, patches1 = ax9.hist(res4.pe1, 100, histtype = "step", normed = 1, cumulative = True, visible = False)
counts2, bins2, patches2 = ax9.hist(res4.pe2, 100, histtype = "step", normed = 1, cumulative = True, visible = False)
counts3, bins3, patches3 = ax9.hist(res4.pe3, 100, histtype = "step", normed = 1, cumulative = True, visible = False)
counts4, bins4, patches4 = ax9.hist(res4.pe4, 100, histtype = "step", normed = 1, cumulative = True, visible = False)
countsn1, binsn1, patchesn1 = ax9.hist(nonres4.pe1, 100, histtype = "step", normed = 1, cumulative = True, visible = False)
countsn2, binsn2, patchesn2 = ax9.hist(nonres4.pe2, 100, histtype = "step", normed = 1, cumulative = True, visible = False)
countsn3, binsn3, patchesn3 = ax9.hist(nonres4.pe3, 100, histtype = "step", normed = 1, cumulative = True, visible = False)
countsn4, binsn4, patchesn4 = ax9.hist(nonres4.pe4, 100, histtype = "step", normed = 1, cumulative = True, visible = False)
ax9.plot(bins1[:-1], counts1, color = colors[0], label = "Res P1")
ax9.plot(bins2[:-1], counts2, color = colors[1], label = "Res P2")
ax9.plot(bins3[:-1], counts3, color = colors[2], label = "Res P3")
ax9.plot(bins4[:-1], counts4, color = colors[3], label = "Res P4")
ax9.plot(binsn1[:-1], countsn1, color = colors[0], linestyle = "--", label = "Non-Res P1")
ax9.plot(binsn2[:-1], countsn2, color = colors[1], linestyle = "--", label = "Non-Res P2")
ax9.plot(binsn3[:-1], countsn3, color = colors[2], linestyle = "--", label = "Non-Res P3")
ax9.plot(binsn4[:-1], countsn4, color = colors[3], linestyle = "--", label = "Non-Res P4")
ax9.plot(binso[:-1], countso, 'k', label = "Observed")
ax9.grid()
ax9.set_ylim(0,1)
ax9.set_xlim(0,1)
ax9.legend(loc = "lower right")

D1, P1 = st.ks_2samp(counts1, countso)
D2, P2 = st.ks_2samp(counts2, countso)
D3, P3 = st.ks_2samp(counts3, countso)
D4, P4 = st.ks_2samp(counts4, countso)

pvp1 = "%.3f" % (P1*100)
pvp2 = "%.3f" % (P2*100)
pvp3 = "%.3f" % (P3*100)
pvp4 = "%.3f" % (P4*100)

print "4P Res Planet 1 Final \t| {0}% \t| \t \t| \t \t| \t".format(pvp1)
print "4P Res Planet 2 Final \t| {0}% \t| \t \t| \t \t| \t".format(pvp2)
print "4P Res Planet 3 Final \t| {0}% \t| \t \t| \t \t| \t".format(pvp3)
print "4P Res Planet 4 Final \t| {0}% \t| \t \t| \t \t| \t".format(pvp4)

D1, P1 = st.ks_2samp(countsn1, countso)
D2, P2 = st.ks_2samp(countsn2, countso)
D3, P3 = st.ks_2samp(countsn3, countso)
D4, P4 = st.ks_2samp(countsn4, countso)

pvp1 = "%.3f" % (P1*100)
pvp2 = "%.3f" % (P2*100)
pvp3 = "%.3f" % (P3*100)
pvp4 = "%.3f" % (P4*100)

print "4P NonRes Planet 1 Final| {0}% \t| \t \t| \t \t| \t".format(pvp1)
print "4P NonRes Planet 2 Final| {0}% \t| \t \t| \t \t| \t".format(pvp2)
print "4P NonRes Planet 3 Final| {0}% \t| \t \t| \t \t| \t".format(pvp3)
print "4P NonRes Planet 4 Final| {0}% \t| \t \t| \t \t| \t".format(pvp4)

fig6 = p.figure()
p.subplots_adjust(hspace = 0.25)
fig6.suptitle("Distribution Of Planets Remaining")
ax10 = fig6.add_subplot(2,1,1)
ax10.set_title("Resonant Case")
bars = ax10.bar([0.6, 1.6, 2.6, 3.6], [len(res4.pa1), len(res4.pa2), len(res4.pa3), len(res4.pa4)], edgecolor = "k")
ax10.set_xticks([0, 1, 2, 3, 4])
bars[0].set_color(colors[0])
bars[1].set_color(colors[1])
bars[2].set_color(colors[2])
bars[3].set_color(colors[3])
ax10.set_xlabel("Planet ID")
ax10.set_xlim(0.5, 4.5)
ax10.set_ylim(0, 100)
ax10.grid()

ax11 = fig6.add_subplot(2,1,2)
ax11.set_title("Non-Resonant Case")
bars = ax11.bar([0.6, 1.6, 2.6, 3.6], [len(nonres4.pa1), len(nonres4.pa2), len(nonres4.pa3), len(nonres4.pa4)])
ax11.set_xticks([0, 1, 2, 3, 4])
bars[0].set_color(colors[0])
bars[1].set_color(colors[1])
bars[2].set_color(colors[2])
bars[3].set_color(colors[3])
ax11.set_xlabel("Planet ID")
ax11.set_xlim(0.5, 4.5)
ax11.set_ylim(0, 100)
ax11.grid()

ax10.set_ylabel("# of Simulations")
ax11.set_ylabel("# of Simulations")
p.show()

