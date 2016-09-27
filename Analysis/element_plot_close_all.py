import numpy as np
import pylab as p

n_p = 5

seeds, planets = np.loadtxt("5Res_seeds.txt", unpack = True)
seeds2, planets2 = np.loadtxt("5NonRes_seeds.txt", unpack = True)

fig = p.figure()
fig.suptitle("Eccentriciy Time Evolution")
p.subplots_adjust(hspace = 0.75)

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

if n_p == 4:
    colors = ["r", "#ff9933", "#d2d22d", "b", "w"]
elif n_p == 5:
    colors = ["r", "#ff9933", "#d2d22d", "b", "b"]

for i in range(1,101):
    path = "../5Res/DataFiles/data_seed{0}.txt".format(i)

    datafile = open(path, "r")
    data = datafile.readlines()

    time = []
    t1, t2, t3, t4, t5 = [], [], [], [], []
    a1, a2, a3, a4, a5 = [], [], [], [], []
    e1, e2, e3, e4, e5 = [], [], [], [], []
    i1, i2, i3, i4, i5 = [], [], [], [], []

    for line in data:
        parsed = line.split()
        if parsed[-1] == "1":
            t1.append(float(parsed[0]))
            a1.append(float(parsed[1]))
            e1.append(float(parsed[2]))
            i1.append(float(parsed[3]))
        elif parsed[-1] == "2":
            t2.append(float(parsed[0]))
            a2.append(float(parsed[1]))
            e2.append(float(parsed[2]))
            i2.append(float(parsed[3]))
        elif parsed[-1] == "3":
            t3.append(float(parsed[0]))
            a3.append(float(parsed[1]))
            e3.append(float(parsed[2]))
            i3.append(float(parsed[3]))
        elif parsed[-1] == "4":
            t4.append(float(parsed[0]))
            a4.append(float(parsed[1]))
            e4.append(float(parsed[2]))
            i4.append(float(parsed[3]))
        elif parsed[-1] == "5":
            t5.append(float(parsed[0]))
            a5.append(float(parsed[1]))
            e5.append(float(parsed[2]))
            i5.append(float(parsed[3]))

    ax1.plot(t1, e1, color = colors[4], alpha = 0.3, marker = ",")
    ax1.plot(t2, e2, color = colors[4], alpha = 0.3, marker = ",")
    ax1.plot(t3, e3, color = colors[4], alpha = 0.3, marker = ",")
    ax1.plot(t4, e4, color = colors[4], alpha = 0.3, marker = ",")
    if n_p == 5:
        ax1.plot(t5, e5, color = colors[4], alpha = 0.3, marker = ",")

####    ax3.plot(t1, i1, color = colors[0], alpha = 0.3, marker = ",")
####    ax3.plot(t2, i2, color = colors[1], alpha = 0.3, marker = ",")
##    ax3.plot(t3, np.array(a3)*(1-np.array(e3)), color = colors[3], alpha = 0.6, marker = ",")
##    ax3.plot(t4, np.array(a4)*(1-np.array(e4)), color = colors[3], alpha = 0.3, marker = ",")
##    if n_p == 5:
##        ax3.plot(t5, np.array(a5)*(1-np.array(e5)), color = colors[3], alpha = 0.3, marker = ",")

for i in range(1,101):

    path = "../5NonRes/DataFiles/data_seed{0}.txt".format(i)

    datafile = open(path, "r")
    data = datafile.readlines()

    time = []
    t1, t2, t3, t4, t5 = [], [], [], [], []
    a1, a2, a3, a4, a5 = [], [], [], [], []
    e1, e2, e3, e4, e5 = [], [], [], [], []
    i1, i2, i3, i4, i5 = [], [], [], [], []

    for line in data:
        parsed = line.split()
        if parsed[-1] == "1":
            t1.append(float(parsed[0]))
            a1.append(float(parsed[1]))
            e1.append(float(parsed[2]))
            i1.append(float(parsed[3]))
        elif parsed[-1] == "2":
            t2.append(float(parsed[0]))
            a2.append(float(parsed[1]))
            e2.append(float(parsed[2]))
            i2.append(float(parsed[3]))
        elif parsed[-1] == "3":
            t3.append(float(parsed[0]))
            a3.append(float(parsed[1]))
            e3.append(float(parsed[2]))
            i3.append(float(parsed[3]))
        elif parsed[-1] == "4":
            t4.append(float(parsed[0]))
            a4.append(float(parsed[1]))
            e4.append(float(parsed[2]))
            i4.append(float(parsed[3]))
        elif parsed[-1] == "5":
            t5.append(float(parsed[0]))
            a5.append(float(parsed[1]))
            e5.append(float(parsed[2]))
            i5.append(float(parsed[3]))

    ax2.plot(t1, e1, color = colors[0], alpha = 0.3, marker = ",")
    ax2.plot(t2, e2, color = colors[0], alpha = 0.3, marker = ",")
    ax2.plot(t3, e3, color = colors[0], alpha = 0.6, marker = ",")
    ax2.plot(t4, e4, color = colors[0], alpha = 0.3, marker = ",")
    if n_p == 5:
        ax2.plot(t5, e5, color = colors[0], alpha = 0.3, marker = ",")

    

##ax1.plot([], color = colors[0], label = "NonRes")
##ax1.plot([], color = colors[3], label = "Res")
##
##ax2.plot([], color = colors[0], label = "NonRes")
##ax2.plot([], color = colors[3], label = "Res")

##ax3.plot([], color = colors[0], label = "NonRes")
##ax3.plot([], color = colors[3], label = "Res")

ax1.set_title("Systems With Resonances")
ax1.set_xlabel("Time (yrs)")
ax1.set_ylabel("e")
ax1.set_xscale("log")
ax1.set_xlim(0, 5.0e9)
ax1.set_ylim(0,1)
ax2.set_title("Systems Without Resonances")
ax2.set_xlabel("Time (yrs)")
ax2.set_ylabel("e")
ax2.set_xscale("log")
ax2.set_xlim(0, 5.0e9)
ax2.set_ylim(0,1)
ax1.grid()
##ax1.legend(loc = "upper left")
ax2.grid()
##ax2.legend(loc = "upper left")

p.show()
