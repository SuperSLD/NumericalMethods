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

# Формулы, построенные по двум узлам
def differentiation2(line, h):
    diff_y = []
    diff_x = []
    for i in range(1, len(line[0]) - 1):
        diff_x.append(line[0][i])
        diff_y.append((line[1][i+1]-line[1][i-1])/2*h)
    return [diff_x, diff_y]

# Формулы, построенные по трем узлам
def differentiation3(line, h):
    diff_y = []
    diff_x = []
    for i in range(len(line[0]) - 2):
        diff_x.append(line[0][i])
        diff_y.append((-3*line[1][i]+4*line[1][i+1]-line[1][i+2])/2*h)
    return [diff_x, diff_y]

# Дифференциирование с четырьмя узлами
def differentiation4(line, h):
    diff_y = []
    diff_x = []
    for i in range(1, len(line[0]) - 2):
        diff_x.append(line[0][i])
        diff_y.append(
            (-2*line[1][i-1]-3*line[1][i]+6*line[1][i+1]-line[1][i+2])/6*h
            )
    return [diff_x, diff_y]

f = lambda x: np.sqrt(x**2+3)/(np.sin(x/3)+1) + np.log((x**2 + 1)/(3*x - 1))
lim = [1, 5]
h = 0.2
COUNT = 1000

# Перевод RGB цвета от 255..0 до 1..0
def to_normal_color(R,G,B):
    c = 1/256
    return (c*R, c*G, c*B)

line = function_array(f, lim, COUNT)

line_diff_2 = differentiation2(line, h)
line_diff_3 = differentiation3(line, h)
line_diff_4 = differentiation4(line, h)


# Вывод на экран
plt.grid(linestyle="--")
plt.plot(
    line_diff_2[0], 
    line_diff_2[1])
plt.plot(
    line_diff_3[0], 
    line_diff_3[1])
plt.plot(
    line_diff_4[0], 
    line_diff_4[1])
plt.show()