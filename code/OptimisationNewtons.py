import numpy as np
import copy
import matplotlib.pyplot as plt

def optimisation_newton(f, lim, h, e):
    next_x = lim[0]
    while True:
        x = next_x
        fx = f(x)
        x_min_h = x - h
        f_x_min_h = f(x_min_h)
        x_add_h = x + h
        f_x_add_h = f(x_add_h)
        print("x> "+str(x)+" f> "+str(fx)+" x-h> "+str(x_min_h)+" x+h> "+str(x_add_h)+" next_x>"+str(next_x))
        next_x = x - h/2*(f_x_add_h - f_x_min_h)/(f_x_add_h - 2*fx + f_x_min_h)
        if abs(x - next_x) < e: return next_x
    
    return

f = lambda x: (2*(x**2)*np.cos(x/2)+(x**2)*np.sin(x/4)+3*(x+1))/(x+4)**2
lim1 = [2, 4]
lim2 = [5, 7]
h = 0.15
e = 0.00001

print("точка максимума: " + str(optimisation_newton(f, lim1, h, e)))
