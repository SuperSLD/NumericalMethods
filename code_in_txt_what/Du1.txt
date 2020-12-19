from math import *
import numpy as np

def eiler_method(f, lim, h, start):
    current_x = lim[0]
    current_y = start[0]
    f_x_y = f([current_x, current_y])
    result = np.array([])
    while (current_x <= lim[1] + h):
        result = np.append(result ,current_y)
        current_y = f_x_y * h + current_y
        current_x += h
        f_x_y = f([current_x, current_y])
    return result

f = lambda args: (args[0]**2*exp(args[0] - 1/args[0]) + args[1])/(args[0]**2)
lim = np.array([1, 9])
h = 0.4
start = np.array([1.367879])

print(eiler_method(f, lim, h, start))