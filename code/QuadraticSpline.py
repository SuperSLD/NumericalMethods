import numpy as np
from numpy import linalg as LA
import copy

def create_spline(X, Y):
    abc1 = []
    if len(X) != len(Y): return None
    dx = X[1] - X[0]
    df = Y[1] - Y[0]
    a = Y[0]
    b = (-3*Y[0] + 4*Y[1] - Y[2])/(2*dx)
    c = df/(dx**2)-b/dx
    abc1.append([a, b, c])
    print("на интервале [0,1] -> " + str(abc1))
    for i in range(2, len(X)):
        dx = X[1] - X[0]
        df = Y[1] - Y[0]
        a = Y[i - 1]
        b = abc1[len(abc1) - 1][1] + 2*abc1[len(abc1) - 1][2]*dx
        c = df/(dx**2) - b/dx
        abc1.append([a, b, c])
        print("на интервале ["+str(i-1)+","+str(i)+"] -> " + str([a, b, c]))
    return abc1

x = [-1.23, 0, 1.23, 2.46, 3.69, 4.92, 6.15, 7.38 ,8.61, 9.84, 11.07]
y = [
    -0.6935, -1.2745, -1.6279, -1.7581, -0.2693, 3.1725,
    4.7245, 4.8517, 3.9438, 2.8712, 0.9652
    ]

create_spline(x, y)