import matplotlib.pyplot as plt

def create_spline(X, Y):
    abc1 = []
    if len(X) != len(Y): return None
    dx = X[1] - X[0]
    lastDX = dx
    df = Y[1] - Y[0]
    a = Y[0]
    b = (-3*Y[0] + 4*Y[1] - Y[2])/(2*dx)
    c = df/(dx**2)-b/dx
    abc1.append([a, b, c])
    print("на интервале [0,1] -> " + str([a, b, c]))
    for i in range(2, len(X)):
        dx = X[i] - X[i - 1]
        df = Y[i] - Y[i - 1]
        a = Y[i - 1]
        b = abc1[-1][1] + 2*abc1[-1][2]*lastDX
        c = df/(dx*dx) - b/dx
        abc1.append([a, b, c])
        lastDX = dx
        print("на интервале ["+str(i-1)+","+str(i)+"] -> " + str([a, b, c]))
    return abc1

# Точки, данные в варианте
x = [-1.23, 0, 1.23, 2.46, 3.69, 4.92, 6.15, 7.38 ,8.61, 9.84, 11.07, 12, 13]
y = [
    -0.6935, -1.2745, -1.6279, -1.7581, -0.2693, 3.1725,
    4.7245, 4.8517, 3.9438, 2.8712, 0.9652, 3, 2
    ]

# Получение коэфициэнтов сплайна для каждого интервала.
abc1 = create_spline(x, y)
x_spline = []
y_spline = []
COUNT = 100

# Построение сплайна
for i in range(1, len(x)):
    dx = (x[i] - x[i - 1])/COUNT
    for j in range(COUNT):
        local_x = x[i-1] + dx*j
        x_spline.append(local_x)
        local_y = abc1[i - 1][0] + abc1[i - 1][1]*(local_x - x[i - 1]) + abc1[i - 1][2]*(local_x - x[i - 1])*(local_x - x[i - 1])
        y_spline.append(local_y)

def to_normal_color(R,G,B):
    c = 1/256
    return (c*R, c*G, c*B)

# Вывод на экран
plt.plot(x, y, color=to_normal_color(144, 0, 255))
plt.plot(x_spline, y_spline, color=to_normal_color(255, 102, 232))
plt.show()