import copy

def simple_iteration(A, e):
    last_x = [0 for _ in range(len(A))]
    x = [1 for _ in range(len(A))]
    while True:
        for i in range(len(A)):
            x[i] = A[i][len(A[i]) - 1] / A[i][i]
            for j in range(len(A[i]) - 1):
                if i != j:
                    x[i] += -last_x[j]*A[i][j]/A[i][i]
                    
        print("last_x: " + str(last_x))
        if abs(x[0] - last_x[0]) <= e:
            return last_x
        last_x = copy.copy(x)
        x = [0 for _ in range(len(A))]

A = [
    [22,  5, 10, -6,  45],
    [ 5, 15,  2, -7, -18],
    [10, -6, 20,  3, -71],
    [ 6, -3, -7, 17, -38]
]

e = 0.000001

print("решение: " + str(simple_iteration(A, e)))