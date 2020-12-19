def dihotomia(function, e, lim):
    print("интервал: " + str(lim))
    if abs(lim[1] - lim[0]) <= e:
        return (lim[0] + lim[1])/2
    x = (lim[0] + lim[1])/2
    print("текущий X: " + str(x))
    f0 = function(lim[0])
    fx = function(x)
    if f0*fx < 0:
        return dihotomia(function, e, [lim[0], x])
    else:
        return dihotomia(function, e, [x, lim[1]])
    return

f = lambda x: 40*(x**5)+34*(x**4)-101*(x**3)-71*(x**2)-35*x+28
lim = [0,1]
e = 0.00001

print("корень -> " + str(dihotomia(f, e, lim)))