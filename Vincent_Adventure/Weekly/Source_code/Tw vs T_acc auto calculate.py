import pandas as pd
import numpy as np
import math

# Variables

# rolling resistence
rr = 0
# weight (kg)
w = 23
#surface coefficent (-)
c = 0.015
#grade resistance (kg)
gr = 0
# maximum angle incline 
delta = 0.0
#ratio of incline
ratio = 1/2
#acceleration force (kg)
fa = 0
# max speed(m/s)
vmax = 1.788161
#acceleration ( m^2/s)
a = 0
# time taken to reach max speed
t = 0
#total tractive effort (kg)
tte = 0
# Wheel motor torque
tw = 0
# radius of wheel (m)
rw = 0.11176
#resistance of factor
rf = 1.15
#gravity(m^2/s)
g = 9.81
#Calculation
rr = w * c
delta = math.atan(ratio)
gr = w * math.sin(delta)

# array setup
column = ["time to reach max speed"]
row = ["Wheel motor torque"]
# loop
for t in range (1,301):
    t = t/100
    column.append(t)
    fa = w*vmax/(g*t)
    tte = rr + gr + fa
    tw = tte * rw
    roundTw = (round(tw*10000))/10000
    row.append(roundTw)

s = pd.Series(row[:],
              index = column[:])
s.to_csv('TwVsT_accGraph1.csv')



