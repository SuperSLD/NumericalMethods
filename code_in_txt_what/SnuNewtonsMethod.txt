import numpy as np
from numpy import linalg as LA
import copy

def find_solution(X, F, Jf, e):
    lastX = [0, 0]
    while abs(X[0] - lastX[0]) > e and abs(X[1] - lastX[1]) > e:
        J = np.array([
            [Jf[0][0](X[0], X[1]), Jf[0][1](X[0], X[1])], 
            [Jf[1][0](X[0], X[1]), Jf[1][1](X[0], X[1])]
            ])
        Jinv = LA.inv(J)
        dX = np.dot(Jinv, np.array([
            [F[0](X[0], X[1])],
            [F[1](X[0], X[1])]
            ]))
        lastX = copy.copy(X)
        X[0] -= dX[0][0]
        X[1] -= dX[1][0]
    return X

# Функции системы
f1 = lambda x, y: 2*x**2 - 2*x*y - 3*x - 1
f2 = lambda x, y: 2*x + 3*np.log(x+1) - 5*y**2

# Частные производные
df1x = lambda x, y: 4*x - 2*y - 3
df1y = lambda x, y: -2*x
df2x = lambda x, y: 2 + 3/(x + 1)
df2y = lambda x, y: -10*y

X1 = [3, 1]
X2 = [1, -1]
e = 0.00001

print("Решение при X = " + str(X1) + " --> " + str(find_solution(X1, [f1, f2], np.array([[df1x, df1y], [df2x, df2y]]), e)))
print("="*20)
print("Решение при X = " + str(X2) + " --> " + str(find_solution(X1, [f1, f2], np.array([[df1x, df1y], [df2x, df2y]]), e)))