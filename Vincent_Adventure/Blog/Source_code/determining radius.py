import pandas as pd
import numpy as np

# Wheel Torque
tw = 0

# total tractive effort
tte = 14.823316

# radius of wheel/tire
rw = 0.0

# resistence factor
rf = 1.15

# calulator
def twCal(rw):
    tw = tte * rw * rf
    return tw
# Setup

row = [0]
column = [0]
# loop
for rw in range(1,31):
    rw = rw/10
    twResult = twCal(rw)
    roundTwResult = (round(twResult*10000))/10000
    column.append(roundTwResult)
    row.append(rw)

s = pd.Series(column[:],
              index = row[:])

s.to_csv('radius.csv')

# debugg
print("Proceed")
