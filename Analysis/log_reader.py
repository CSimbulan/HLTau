import glob as gb
import numpy as np
import pylab as p
import matplotlib.ticker as tk
import re

n_p = 5

class stats:

    def __init__(self, name):

        self.name = name
        self.collisions = []
        self.ejections = []
        self.minperi = []
        self.Ncol = []
        self.Nej = []
        self.Nmp = []
        self.Npl = []
        self.count = 0
        self.hashes = []

    def getbins(self):
        base = 11.958131745004017
        self.colexp = np.log(min(self.collisions)-1)/np.log(base)
        self.ejexp = np.log(min(self.ejections)-1)/np.log(base)
        self.ejbin = np.logspace(self.ejexp, 9, 30, base = base)
        self.colbin = np.logspace(self.colexp, 9, 30, base = base)
        self.mpexp = np.log(min(self.minperi)-1)/np.log(base)
        self.mpbin = np.logspace(self.mpexp, 9, 30, base = base)
        self.mpbin2 = np.logspace(self.mpexp, 9, 60, base = base)

def histextra(counts, bins, patches, ax, color, color2, showpercent = True, 
              textloc = -18):
                
    # Label the raw counts and the percentages below the x-axis...
    bin_centers = 0.5 * np.diff(bins) + bins[:-1]
    for count, x in zip(counts, bin_centers):
        # Label the raw counts
        if count > 0:
            ax.annotate(str(int(count)), xy=(x, 0), xycoords=("data", "axes fraction"),
                xytext=(0, textloc), textcoords="offset points", va="top", ha="center",
                        color = color)
        
#        if showpercent == True:
#            # Label the percentages
#            percent = '{0}%'.format(int(100 * float(count) / counts.sum()))
#            ax.annotate(percent, xy=(x, 0), xycoords=("data", "axes fraction"),
#                xytext=(0, textloc - 14), textcoords="offset points", va="top", ha="center",
#                        color = color2)
    return ax

def percentage(patches, color1, color2, data, ax):
    # Change the colors of bars at the edges...
    twentyfifth, seventyfifth = np.percentile(data, [25, 75])
    for patch, rightside, leftside in zip(patches, bins[1:], bins[:-1]):
        if rightside < twentyfifth:
            patch.set_facecolor(color1)
        elif leftside > seventyfifth:
            patch.set_facecolor(color2)
    return ax

def extract(stats):

    global n_p
    files = gb.glob("../{0}/LogFiles/*.txt".format(stats.name))

    for logfile in files:
        log = open(logfile, "r")
        col_count = 0
        ej_count = 0
        mp_count = 0
        gh = True
        for line in log:
            parsed = line.split()
            if "collided" in parsed and "Star" not in parsed:
                stats.collisions.append(float(parsed[-1][:-1]))
##                if float(parsed[-1][:-1]) > 1e9:
##                    print logfile, "Over 1bil CC"
                print logfile, "CC"
                col_count += 1
            elif "ejected" in parsed:
                stats.ejections.append(float(parsed[-1][:-1]))
##                if float(parsed[-1][:-1]) > 4e9:
##                    print logfile, "Over 1bil EJ"
                ej_count += 1
            elif "Star" in parsed and "collided" in parsed:
                stats.minperi.append(float(parsed[-1][:-1]))
                if gh == True:
                    stats.count += 1
                    gh = False
                mp_count += 1
##                if float(parsed[-1][:-1]) > 1e9:
##                    print logfile, "Over 1bil S"
                psd = re.split("d|/|t", logfile)
##                seedfile = open("{0}_seeds.txt".format(psd[1]), "a")
##                print logfile, "S"
                if parsed[1] in ("1", "2", "3", "4", "5"):
##                    seedfile.write("{0}\t{1}\n".format(int(float(psd[-3])),parsed[1]))
                    stats.hashes.append(int(parsed[1]))
                if parsed[3] in ("1", "2", "3", "4", "5"):
##                    seedfile.write("{0}\t{1}\n".format(int(float(psd[-3])),parsed[3]))
                    stats.hashes.append(int(parsed[3]))
##                seedfile.close()
##        if col_count == 5:
##            print logfile
        stats.Ncol.append(col_count)
        stats.Nej.append(ej_count)
        stats.Nmp.append(mp_count)
        stats.Npl.append(n_p - col_count - ej_count - mp_count)
        #stats.minperi.append(mp_count)
##        if mp_count > 1:    
##            print logfile, "SADSADSA"
        if ej_count > 3:
            print logfile
        if col_count > 2:
            print logfile
    print stats.count
    print sum(stats.Ncol)
    print sum(stats.Nej)
    print sum(stats.Nmp)
    print sum(stats.Npl)

res = stats("{0}Res".format(n_p))
nonres = stats("{0}NonRes".format(n_p))

extract(res)
extract(nonres)
res.getbins()
nonres.getbins()

tpoints = np.logspace(0, 6, 100000)

fig1 = p.figure()
p.subplots_adjust(hspace = 0.55)
#fig1.text(0.5, 0.02, "time (yrs)", ha="center")
fig1.text(0.04, 0.5, "count", va="center", rotation="vertical")
ax1 = fig1.add_subplot(3,1,1)
ax1.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax1.set_title("Planet-Planet Collision Occurences")
ax1.grid()
counts, bins, patches = ax1.hist(res.collisions, res.colbin, log = True, histtype = "step", label = "Resonant")
ax1 = histextra(counts, bins, patches, ax1, "blue", "black", False, textloc = 10)
counts, bins, patches = ax1.hist(nonres.collisions, nonres.colbin, log = True, color = "red", histtype = "step", label = "Non-Resonant")
ax1 = histextra(counts, bins, patches, ax1, "red", "black", False, textloc = 24)
ax1.set_xscale("log")
ax1.set_xlim(0, bins[-1])
ax1.tick_params(axis ="both")
ax1.set_xticks(np.logspace(res.colexp, 9, 10, base = 11.958131745004017))
ax1.set_xticklabels(tpoints, rotation = 45)
ax1.xaxis.set_major_formatter(tk.OldScalarFormatter())
ax1.xaxis.major.formatter._useMathText = True
ax1.yaxis.set_major_formatter(tk.OldScalarFormatter())
ax1.legend()
ax2 = fig1.add_subplot(3,1,2)
ax2.set_title("Ejection Occurences")
ax2.grid()
counts, bins, patches = ax2.hist(res.ejections, res.ejbin, log = True, histtype = "step", label = "Resonant")
ax2 = histextra(counts, bins, patches, ax2, "blue", "black", False, textloc = 10)
counts, bins, patches = ax2.hist(nonres.ejections, nonres.ejbin, log = True, color = "red", histtype = "step", label = "Non-Resonant")
ax2 = histextra(counts, bins, patches, ax2, "red", "black", False, textloc = 24)
ax2.set_xscale("log")
ax2.set_xlim(0, bins[-1])
ax2.tick_params(axis ="both")
ax2.set_xticks(np.logspace(res.ejexp, 9, 10, base = 11.958131745004017))
ax2.set_xticklabels(tpoints, rotation = 45)
ax2.xaxis.set_major_formatter(tk.OldScalarFormatter())
ax2.xaxis.major.formatter._useMathText = True
ax2.yaxis.set_major_formatter(tk.OldScalarFormatter())
ax2.legend()
ax6 = fig1.add_subplot(3,1,3)
ax6.set_title("Star-Planet Collision Occurences")
ax6.grid()
counts, bins, patches = ax6.hist(res.minperi, res.mpbin, log = True, histtype = "step", label = "Resonant")
ax6 = histextra(counts, bins, patches, ax6, "blue", "black", False, textloc = 10)
counts, bins, patches = ax6.hist(nonres.minperi, nonres.mpbin, log = True, color = "red", histtype = "step", label = "Non-Resonant")
ax6 = histextra(counts, bins, patches, ax6, "red", "black", False, textloc = 24)
ax6.set_xscale("log")
ax6.set_xlim(0, bins[-1])
ax6.tick_params(axis ="both")
ax6.set_xticks(np.logspace(res.mpexp, 9, 10, base = 11.958131745004017))
ax6.set_xticklabels(tpoints, rotation = 45)
ax6.xaxis.set_major_formatter(tk.OldScalarFormatter())
ax6.xaxis.major.formatter._useMathText = True
ax6.yaxis.set_major_formatter(tk.OldScalarFormatter())
ax6.set_xlabel("time (yrs)")
ax6.legend()

fig2 = p.figure()
p.subplots_adjust(hspace = 0.5)
binx = np.arange(-0.5, n_p + 1.5, 1.0)
fig2.text(0.04, 0.5, "count", va="center", rotation="vertical")
ax3 = fig2.add_subplot(3, 1, 1)
ax3.set_title("Distribution of Collisions for {0} Planet Systems".format(n_p))
counts, bins, patches = ax3.hist(res.Ncol, bins = binx, histtype = "step", label = "Resonant")
ax3 = histextra(counts, bins, patches, ax3, "blue", "#6666ff", False, textloc = 10)
counts, bins, patches = ax3.hist(nonres.Ncol, bins = binx, histtype = "step", color = "red", label = "Non-Resonant")
ax3 = histextra(counts, bins, patches, ax3, "red", "#6666ff", False, textloc = 24)
ax3.grid()
ax3.set_xlim(-0.5, n_p + 0.5)
ax4 = fig2.add_subplot(3, 1, 2)
ax4.set_title("Distribution of Ejections")
counts, bins, patches = ax4.hist(res.Nej, bins = binx, histtype = "step", label = "Resonant")
ax4 = histextra(counts, bins, patches, ax4, "blue", "#ff8080", False, textloc = 10)
counts, bins, patches = ax4.hist(nonres.Nej, bins = binx, histtype = "step", color = "red", label = "Non-Resonant")
ax4 = histextra(counts, bins, patches, ax4, "red", "#6666ff", False, textloc = 24)
ax4.grid()
ax4.set_xlim(-0.5, n_p + 0.5)
ax5 = fig2.add_subplot(3, 1, 3)
ax5.set_title("Total Planets Remaining After Five Billion Years")
counts, bins, patches = ax5.hist(res.Npl, bins = binx, histtype = "step", label = "Resonant")
ax5 = histextra(counts, bins, patches, ax5, "blue", "#ff9933", False, textloc = 10)
counts, bins, patches = ax5.hist(nonres.Npl, bins = binx, histtype = "step", color = "red", label = "Non-Resonant")
ax5 = histextra(counts, bins, patches, ax5, "red", "#6666ff", False, textloc = 24)
ax5.grid()
ax5.set_xlim(-0.5, n_p + 0.5)
ax3.set_xlabel("# Collisions")
ax4.set_xlabel("# Ejections")
ax5.set_xlabel("# Planets")
ax3.set_ylabel("# Simulations")
ax4.set_ylabel("# Simulations")
ax5.set_ylabel("# Simulations")
ax3.legend()
ax4.legend()
ax5.legend()

fig3 = p.figure()
fig3.suptitle("Distribution of Planets Getting Within 0.2 AU")
ax7 = fig3.add_subplot(1,1,1)
ax7.set_xlabel("Planet ID")
ax7.set_ylabel("# of Instances")
counts, bins, patches = ax7.hist(res.hashes, bins = binx, histtype = "step", label = "Resonant")
ax7 = histextra(counts, bins, patches, ax7, "blue", "#ff9933", False, textloc = 10)
counts, bins, patches = ax7.hist(nonres.hashes, bins = binx, histtype = "step", color = "red", label = "Non-Resonant")
ax7 = histextra(counts, bins, patches, ax7, "red", "#6666ff", False, textloc = 24)
ax7.set_xlim(0.5, n_p + 0.5)
ax7.grid()
ax7.legend()

fig4 = p.figure()
##fig4.suptitle("Planet-Star Collision Occurences")
ax8 = fig4.add_subplot(1,1,1)
ax8.set_title("Star-Planet Collision Occurences - T_stable")
ax8.grid()
counts, bins, patches = ax8.hist(np.array(res.minperi) - 3.5e6, res.mpbin2, log = True, histtype = "step", label = "Resonant")
##ax8 = histextra(counts, bins, patches, ax8, "blue", "black", False, textloc = 10)
counts, bins, patches = ax8.hist(np.array(nonres.minperi) - 1.0e6, nonres.mpbin2, log = True, color = "red", histtype = "step", label = "Non-Resonant")
##ax8 = histextra(counts, bins, patches, ax8, "red", "black", False, textloc = 24)
ax8.set_xscale("log")
ax8.set_yscale("linear")
ax8.set_xlim(0, bins[-1])
##ax8.tick_params(axis ="both")
ax8.set_xticks(np.logspace(res.mpexp, 9, 10, base = 11.958131745004017))
ax8.set_xticklabels(tpoints, rotation = 45)
ax8.xaxis.set_major_formatter(tk.OldScalarFormatter())
ax8.xaxis.major.formatter._useMathText = True
##ax8.yaxis.set_major_formatter(tk.OldScalarFormatter())
ax8.set_xlabel("time (yrs)")
ax8.legend()


p.show()

