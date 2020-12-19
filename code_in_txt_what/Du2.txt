from math import *
import numpy as np

def eiler_method(z_, y_, lim, h, start):
    current_x = lim[0]
    current_y = start[0]
    current_z = start[1]
    y = y_([current_x, current_y, current_z])
    z = z_([current_x, current_y, current_z])
    result = np.array([])
    while (current_x <= lim[1] + h):
        print(current_z, current_y)
        result = np.append(result ,current_y)
        current_z = z * h + current_z
        current_y = y * h + current_y
        y = y_([current_x, current_y, current_z])
        z = z_([current_x, current_y, current_z])
        current_x += h
    return result

# По условию три переменных X Y Z
z_ = lambda args: -args[2]/args[0]
y_ = lambda args: args[2]
lim = np.array([1, 5])
h = 0.25
start = np.array([1, 1])

print(eiler_method(z_, y_, lim, h, start))