import numpy as np
import visual as vs
import time as ti
from visual.graph import *

scene = vs.display()

seed = 24

path = "NonResTides"

data = open("../{1}/PosFiles/pos_seed{0}_both.txt".format(seed, path), "r")

time, s, p1, p2, p3, p4, p5, m1, m2, m3, m4, m5 = [], [], [], [], [], [], [], [], [], [], [], []
t = [] 
reset = False
ctr = 0
for line in data:
    parsed = line.split()
    if float(parsed[0]) not in time:
        time.append(float(parsed[0]))
    if parsed[1] == "9":
        s.append((float(parsed[2]), float(parsed[3]), float(parsed[4])))
    elif parsed[1] == "1":
        p1.append((float(parsed[2]), float(parsed[3]), float(parsed[4])))
        m1.append(float(parsed[-1]))
    elif parsed[1] == "2":
        p2.append((float(parsed[2]), float(parsed[3]), float(parsed[4])))
        m2.append(float(parsed[-1]))
    elif parsed[1] == "3":
        p3.append((float(parsed[2]), float(parsed[3]), float(parsed[4])))
        m3.append(float(parsed[-1]))
    elif parsed[1] == "4":
        p4.append((float(parsed[2]), float(parsed[3]), float(parsed[4])))
        m4.append(float(parsed[-1]))
    elif parsed[1] == "5":
        p5.append((float(parsed[2]), float(parsed[3]), float(parsed[4])))
        m5.append(float(parsed[-1]))

time = time

data = open("../{1}/DataFiles/data_seed{0}_both.txt".format(seed, path), "r")
time2, a1, a2, a3, a4, a5 = [], [], [], [], [], []
e1, e2, e3, e4, e5 = [], [], [], [], []
t = []
ctr = 0
for line in data:
    parsed = line.split()
    if parsed[-1] == "1":
        a1.append(float(parsed[1]))
        e1.append(float(parsed[2]))
    elif parsed[-1] == "2":
        a2.append(float(parsed[1]))
        e2.append(float(parsed[2]))
    elif parsed[-1] == "3":
        a3.append(float(parsed[1]))
        e3.append(float(parsed[2]))
    elif parsed[-1] == "4":
        a4.append(float(parsed[1]))
        e4.append(float(parsed[2]))
    elif parsed[-1] == "5":
        a5.append(float(parsed[1]))
        e5.append(float(parsed[2]))

time2 = time

points = 200#max(len(p1), len(p2), len(p3), len(p4), len(p5))

if len(p5) > 0:
    colors = [vs.color.red, vs.color.orange, vs.color.yellow, vs.color.green, vs.color.blue]
else:
    colors = [vs.color.red, vs.color.orange, vs.color.yellow, vs.color.blue]

star = vs.sphere(pos = (s[0][0], s[0][1], s[0][2]), radius = 5, color = vs.color.white)

try:
    planet1 = vs.sphere(pos = (p1[0][0], p1[0][1], p1[0][2]), radius = 2, color = colors[0], make_trail = True, trail_type = "points", retain = points)
except:
    pass
try:
    planet2 = vs.sphere(pos = (p2[0][0], p2[0][1], p2[0][2]), radius = 2, color = colors[1], make_trail = True, trail_type = "points", retain = points)
except:
    pass
try:
    planet3 = vs.sphere(pos = (p3[0][0], p3[0][1], p3[0][2]), radius = 2, color = colors[2], make_trail = True, trail_type = "points", retain = points)
except:
    pass
try:
    planet4 = vs.sphere(pos = (p4[0][0], p4[0][1], p4[0][2]), radius = 2, color = colors[3], make_trail = True, trail_type = "points", retain = points)
except:
    pass
if len(p5) > 0:
    try:
        planet5 = vs.sphere(pos = (p5[0][0], p5[0][1], p5[0][2]), radius = 2, color = colors[4], make_trail = True, trail_type = "points", retain = points)
        label5 = vs.label(pos = planet5.pos, text = "P5", xoffset = 12, yoffset = 12, height = 10, border = 1, color = colors[4])
        labela5 = vs.label(pos = planet5.pos, text = "{0:.2f}".format(a5[0]), xoffset = -12, yoffset = -12, height = 10, border = 1, color = colors[4])
        planet5.trail_object.size = 3
    except:
        pass

try:
    planet1.trail_object.size = 3
    label1 = vs.label(pos = planet1.pos, text = "P1", xoffset = 12, yoffset = 12, height = 10, border = 1, color = colors[0])
    labela1 = vs.label(pos = planet1.pos, text = "{0:.2f}".format(a1[0]), xoffset = -12, yoffset = -12, height = 10, border = 1, color = colors[0])
except:
    pass

try:
    planet2.trail_object.size = 3
    label2 = vs.label(pos = planet2.pos, text = "P2", xoffset = 12, yoffset = 12, height = 10, border = 1, color = colors[1])
    labela2 = vs.label(pos = planet2.pos, text = "{0:.2f}".format(a2[0]), xoffset = -12, yoffset = -12, height = 10, border = 1, color = colors[1])
except:
    pass

try:
    planet3.trail_object.size = 3
    label3 = vs.label(pos = planet3.pos, text = "P3", xoffset = 12, yoffset = 12, height = 10, border = 1, color = colors[2])
    labela3 = vs.label(pos = planet3.pos, text = "{0:.2f}".format(a3[0]), xoffset = -12, yoffset = -12, height = 10, border = 1, color = colors[2])
except:
    pass

try:
    planet4.trail_object.size = 3
    label4 = vs.label(pos = planet4.pos, text = "P4", xoffset = 12, yoffset = 12, height = 10, border = 1, color = colors[3])
    labela4 = vs.label(pos = planet4.pos, text = "{0:.2f}".format(a4[0]), xoffset = -12, yoffset = -12, height = 10, border = 1, color = colors[3])
except:
    pass

timelabel = vs.label(pos = (0, -150, 0), text = "t = 0.0")
count = 0

plotsa = vs.display()
plotsa.select()

gd = gdisplay(x=0, y=0, width=700, height=300,
      title='Semi-Major Axis vs. t', xtitle='t', ytitle='a',
      foreground=color.white, background=color.black,
      logx = True)

fa1 = gcurve(color=colors[0])
fa2 = gcurve(color=colors[1])
fa3 = gcurve(color=colors[2])
fa4 = gcurve(color=colors[3])
if len(p5)>0:
    fa5 = gcurve(color=colors[4])

plotse = vs.display()
plotse.select()

gd = gdisplay(x=0, y=0, width=700, height=300,
      title='Eccentricity vs. t', xtitle='t', ytitle='e',
      foreground=color.white, background=color.black,
      logx = True)

fe1 = gcurve(color=colors[0])
fe2 = gcurve(color=colors[1])
fe3 = gcurve(color=colors[2])
fe4 = gcurve(color=colors[3])
if len(p5)>0:
    fe5 = gcurve(color=colors[4])

for i in range(len(time)):
    timelabel.text = "t = {0}".format(time[i])
    timelabel.pos = (scene.x, scene.y - 120, 0)
    star.pos = (s[i][0], s[i][1], s[i][2])
    try:
        planet1.pos = (p1[i][0], p1[i][1], p1[i][2])
        planet1.radius = planet1.radius
        label1.pos = planet1.pos
        labela1.pos = planet1.pos
        labela1.text = "{0:.2f}".format(a1[i])
        fa1.plot(pos = (time[i], a1[i]))
        fe1.plot(pos = (time[i], e1[i]))
    except:
        planet1.color = vs.color.white
        label1.color = vs.color.white
        labela1.color = vs.color.white
    try:
        planet2.pos = (p2[i][0], p2[i][1], p2[i][2])
        planet2.radius = planet2.radius
        label2.pos = planet2.pos
        labela2.pos = planet2.pos
        labela2.text = "{0:.2f}".format(a2[i])
        fa2.plot(pos = (time[i], a2[i]))
        fe2.plot(pos = (time[i], e2[i]))
    except:
        planet2.color = vs.color.white
        label2.color = vs.color.white
        labela2.color = vs.color.white
    try:
        planet3.pos = (p3[i][0], p3[i][1], p3[i][2])
        planet3.radius = planet3.radius
        label3.pos = planet3.pos
        labela3.pos = planet3.pos
        labela3.text = "{0:.2f}".format(a3[i])
        fa3.plot(pos = (time[i], a3[i]))
        fe3.plot(pos = (time[i], e3[i]))
    except:
        pass
        planet3.color = vs.color.white
        label3.color = vs.color.white
        labela3.color = vs.color.white
    try:
        planet4.pos = (p4[i][0], p4[i][1], p4[i][2])
        planet4.radius = planet4.radius
        label4.pos = planet4.pos
        labela4.pos = planet4.pos
        labela4.text = "{0:.2f}".format(a4[i])
        fa4.plot(pos = (time[i], a4[i]))
        fe4.plot(pos = (time[i], e4[i]))
    except:
        pass
        planet4.color = vs.color.white
        label4.color = vs.color.white
        labela4.color = vs.color.white
    if len(p5) > 0:
        try:
            planet5.pos = (p5[i][0], p5[i][1], p5[i][2])
            planet5.radius = planet5.radius
            label5.pos = planet5.pos
            labela5.pos = planet5.pos
            labela5.text = "{0:.2f}".format(a5[i])
            fa5.plot(pos = (time[i], a5[i]))
            fe5.plot(pos = (time[i], e5[i]))
        except:
            pass
            planet5.color = vs.color.white
            label5.color = vs.color.white
            labela5.color = vs.color.white
    if time[i] > 3.588e8:
        ti.sleep(0.001)
    else:
        ti.sleep(0.001)
