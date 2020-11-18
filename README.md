# NumericalMethods
![](https://img.shields.io/github/stars/SuperSLD/NumericalMethods) ![](https://img.shields.io/github/forks/SuperSLD/NumericalMethods)

Программы по курсу "численные методы" написанные на Python
## GausJordan.py Решение СЛАУ занятие 1. 

Входные данные:
```python
A = [
    ["2", "-5", "-4", "3", "1", "-26", "1", "0", "0", "0", "0"],
    ["4", "3", "1", "-5", "2", "16", "0", "1", "0", "0", "0"],
    ["-2", "3", "4", "2", "-5", "23", "0", "0", "1", "0", "0"],
    ["2", "0", "-4", "1", "3", "-13", "0", "0", "0", "1", "0"],
    ["1", "3", "-5", "-7", "-2", "11", "0", "0", "0", "0", "1"]
]
```
Вывод программы:
```python
Исходная матрица системы:
|         2|        -5|        -4|         3|         1|       -26|         1|         0|         0|         0|         0|
|         4|         3|         1|        -5|         2|        16|         0|         1|         0|         0|         0|
|        -2|         3|         4|         2|        -5|        23|         0|         0|         1|         0|         0|
|         2|         0|        -4|         1|         3|       -13|         0|         0|         0|         1|         0|
|         1|         3|        -5|        -7|        -2|        11|         0|         0|         0|         0|         1|
--------------------------------------------------------------------------------------------------------------------------
Решение полученное методом
Гауса-Жордана:
|         1|         0|         0|         0|         0|         1|  330/1601|  345/1601|  712/4803|   34/1601|  -97/4803|
|         0|         1|         0|         0|         0|         3| -205/1601|    4/1601|  176/1601|  367/1601|   12/1601|
|         0|         0|         1|         0|         0|         2|  -12/1601|  133/1601|  -55/4803| -205/1601| -404/4803|
|         0|         0|         0|         1|         0|        -1|   39/1601|  -32/1601|  193/1601|  266/1601|  -96/1601|
|         0|         0|         0|         0|         1|        -2| -249/1601|  -42/1601| -247/1601|  149/1601| -126/1601|
--------------------------------------------------------------------------------------------------------------------------
```
## SimpleIteration.py Решение СЛАУ занятие 2.
Входные данные:
```python
A = [
    [22,  5, 10, -6,  45],
    [ 5, 15,  2, -7, -18],
    [10, -6, 20,  3, -71],
    [ 6, -3, -7, 17, -38]
]

e = 0.000001
```
Вывод программы:
```python
last_x: [0, 0, 0, 0]
last_x: [2.0454545454545454, -1.2, -3.55, -2.235294117647059]
last_x: [3.322192513368984, -2.4516221033868093, -4.597433155080214, -4.630748663101604]
last_x: [3.4294522767784805, -3.855422459893048, -5.251970588235294, -5.73353255740799]
last_x: [3.745255583516829, -4.318536540618517, -5.561322992745956, -6.288633832823359]
last_x: [3.8397322560732725, -4.641604584123716, -5.774893679020465, -6.609200239539895]
last_x: [3.9228071942538123, -4.7942183732736465, -5.870967467342767, -6.787497825997296]
last_x: [3.9525354356278237, -4.89230572123764, -5.931544435209405, -6.883310032749598]
last_x: [3.9762323982629395, -4.938850569131167, -5.961462929272764, -6.936055342585041]
last_x: [3.986025003766965, -4.967374902057631, -5.979363068483063, -6.964952153051793]
last_x: [3.992763285309456, -4.981737596882084, -5.988482149543003, -6.980812718126831]
last_x: [3.995846962321794, -4.99016941028994, -5.993781014000328, -6.989480444076707]
last_x: [3.9978079330451237, -4.994535726143017, -5.996552237636372, -6.994238653106051]
last_x: [3.9987622312928415, -4.997040384113015, -5.998128886399559, -6.996842378832612]
last_x: [3.9993380232529545, -4.998363335699558, -5.998966874055434, -6.998270396758413]
last_x: [3.9996301381137105, -4.999109943030852, -5.999437452822583, -6.999052133235555]
last_x: [3.999800520180308, -4.999509381171484, -5.999690231980778, -6.999480754560759]
last_x: [3.999889304468211, -4.9997324945910195, -5.9998309612574845, -6.999715464027162]
last_x: [3.999939968243954, -4.999852856534414, -5.999907081007336, -6.999844119963806]
last_x: [3.9999668351346633, -4.9999196345967825, -5.99994922308773, -6.999914585065784]
last_x: [3.999981949703023, -4.999955854997223, -5.999972120186499, -6.999953204483084]
last_x: [3.999990056816028, -4.999975862634914, -5.999984750678215, -6.999974359089134]
last_x: [3.9999945757009963, -4.999986753089843, -5.999991633335117, -6.999985951973436]
last_x: [3.999997017589081, -4.99999275170992, -5.999995420981436, -6.999992302754196]
last_x: [3.999998370538126, -4.999996024350794, -5.999997488894387, -6.999995782796136]
решение: [3.999998370538126, -4.999996024350794, -5.999997488894387, -6.999995782796136]
```
## Dihotomia.py Ренение НУ занятие 3.
Входные данные:
```python
f = lambda x: 40*(x**5)+34*(x**4)-101*(x**3)-71*(x**2)-35*x+28
lim = [0,1]
e = 0.00001
```
Вывод программы:
```python
интервал: [0, 1]
текущий X: 0.5
интервал: [0, 0.5]
текущий X: 0.25
интервал: [0.25, 0.5]
текущий X: 0.375
интервал: [0.375, 0.5]
текущий X: 0.4375
интервал: [0.375, 0.4375]
текущий X: 0.40625
интервал: [0.375, 0.40625]
текущий X: 0.390625
интервал: [0.375, 0.390625]
текущий X: 0.3828125
интервал: [0.375, 0.3828125]
текущий X: 0.37890625
интервал: [0.37890625, 0.3828125]
текущий X: 0.380859375
интервал: [0.37890625, 0.380859375]
текущий X: 0.3798828125
интервал: [0.37890625, 0.3798828125]
текущий X: 0.37939453125
интервал: [0.37939453125, 0.3798828125]
текущий X: 0.379638671875
интервал: [0.37939453125, 0.379638671875]
текущий X: 0.3795166015625
интервал: [0.37939453125, 0.3795166015625]
текущий X: 0.37945556640625
интервал: [0.37939453125, 0.37945556640625]
текущий X: 0.379425048828125
интервал: [0.379425048828125, 0.37945556640625]
текущий X: 0.3794403076171875
интервал: [0.379425048828125, 0.3794403076171875]
текущий X: 0.37943267822265625
интервал: [0.37943267822265625, 0.3794403076171875]
корень -> 0.3794364929199219
```
## NewtonsMethod.py Решение НУ занятие 4.
Входные данные:
```python
f   = lambda x: E**x - 2*x -2
df  = lambda x: E**x - 2

x0 = 2.4
e = 0.000001
```
Вывод программы:
```python
решение: 1.67834699001572
```
## SnuNewtonsMethod.py СНУ Метод Ньютона занятие 5.
Входные данные:
```python
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
```
Вывод программы:
```python
Решение при X = [3, 1] --> [3.1067148534615936, 1.4457731437829973]
```
