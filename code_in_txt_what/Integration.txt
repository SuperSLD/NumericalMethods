import numpy as np
import copy
import matplotlib.pyplot as plt

def function_array(f, lim, count):
    x = []
    y = []
    dx = abs(lim[1] - lim[0])/count
    for i in range(count):
        local_x = i*dx + lim[0]
        x.append(local_x)
        y.append(f(local_x))
    return [x, y]

def integration_simpson(fx, a, b):
    h = (b - a)/len(fx)
    start_value = fx[0]
    end_value = fx[-1]
    line_mid_1 = []
    line_mid_2 = []
    i = 1
    while(i <= len(fx)-1):
        line_mid_1.append(fx[i])
        i+=2
    i = 2
    while(i <= len(fx)-1):
        line_mid_2.append(fx[i])
        i+=2
    return (start_value+end_value+4*sum(line_mid_1)+2*sum(line_mid_2))*h/3

# Исходная функция и пределы интегрирования
f = lambda x:(x*np.cos(x) + np.sin(x))/(x+1)**2
lim = [0, 2]
COUNT = 1000

line = function_array(f, lim, COUNT)
print("Значение подученное методом Симпсона -> " + str(integration_simpson(line[1], line[0][0], line[0][-1])))

plt.grid(linestyle="--")
plt.plot(line[0], line[1])
plt.show()