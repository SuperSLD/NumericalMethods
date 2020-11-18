E = 2.71828182846

def newton(x0, e, f, df):
    last_x = 0
    while True:
        delta = f(x0) / df(x0)
        x0 = x0 - delta
        if abs(last_x - x0) <= e:
            return x0
        last_x = x0

f   = lambda x: E**x - 2*x -2
df  = lambda x: E**x - 2

x0 = 2.4
e = 0.000001

print("решение: " + str(newton(x0, e, f, df)))