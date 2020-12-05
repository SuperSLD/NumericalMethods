import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

def function_data(f, x_lim, y_lim, h):
    matrix = []
    x_array = [x_lim[0]+h*i for i in range(int((x_lim[1] - x_lim[0])/h))]
    y_array = [y_lim[0]+h*i for i in range(int((y_lim[1] - y_lim[0])/h))]
    for i in range(int((y_lim[1] - y_lim[0])/h)):
        line = []
        for j in range(int((x_lim[1] - x_lim[0])/h)):
            line.append(f([y_lim[0] + h*j, y_lim[0] + h*i]))
        matrix.append(line)
    return x_array, y_array, matrix

def grad_abs(grad, position):
    return np.sqrt(grad[0](position)**2 + grad[1](position)**2)

def optimal_lambda(f, grad, position, h):
    l = 0
    min_val = 299792458
    current_l = 0
    while current_l < 1:
        fl = f([position[0] - current_l*grad[0](position), position[1] - current_l*grad[1](position)])
        if min_val > fl:
            min_val = fl
            l = current_l
        current_l += h
    return l

def gradient_max_speed_optimisation(f, grad, position, e, h):
    x_array = []
    y_array = []
    while grad_abs(grad, position) > e:
        l = optimal_lambda(f, grad, position, h)
        next_x = position[0] - l*grad[0](position)
        next_y = position[1] - l*grad[1](position)
        x_array.append(position[0])
        y_array.append(position[1])
        position = [next_x, next_y]
    return [f(position), [x_array, y_array]]

def gradient_optimisation(f, grad, position, e, h):
    x_array = []
    y_array = []
    while grad_abs(grad, position) > e:
        l = 0.1
        next_x = position[0] - l*grad[0](position)
        next_y = position[1] - l*grad[1](position)
        x_array.append(position[0])
        y_array.append(position[1])
        position = [next_x, next_y]
    return [f(position), [x_array, y_array]]

f = lambda args: (2*args[0]**2)*(args[1] + 2) - args[0]**4 + (args[1] - 1)**2*np.cos(2*args[0] + 1) - (args[1] - 2*args[0] + 2)*np.sin(2*args[1] - 1)
dFx = lambda args: -4*args[0]**3 + 2*np.sin(2*args[1] - 1) - 2*(args[1] - 1)**2*np.sin(2*args[0] + 1) + 4*args[0]*(args[1] + 2)
dFy = lambda args: -np.sin(2*args[1] - 1) + 2*args[0]**2 + (-2 + 2*args[1])*np.cos(2*args[0] + 1) + 2*(-2 - args[1] + 2*args[0])*np.cos(2*args[1] - 1)

x_start = -1        # Начальный X
y_start = 0         # Начальный Y
e = 0.000001        # Точность
h = 0.001           # Шаг перебора лямбды

resultMaxSpeed = gradient_max_speed_optimisation(f, [dFx, dFy], [x_start, y_start], e, h)
print("min f >>>>>> " + str(resultMaxSpeed[0]))
resultMinSpeed = gradient_optimisation(f, [dFx, dFy], [x_start, y_start], e, h)
print("min f >>>>>> " + str(resultMinSpeed[0]))


X, Y, Z = function_data(f, [-1, 1], [-1, 3], 0.01)

def to_normal_color(R,G,B):
    c = 1/256
    return (c*R, c*G, c*B)

plt.grid(linestyle="--")
plt.plot(resultMinSpeed[1][0], resultMinSpeed[1][1], color=to_normal_color(255,0,0))
plt.plot(resultMaxSpeed[1][0], resultMaxSpeed[1][1], color=to_normal_color(255,190,107))

#matshow contourf
cf = plt.contourf(X, Y, Z) 
plt.colorbar(cf)
plt.show()