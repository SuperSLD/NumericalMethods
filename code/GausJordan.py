import copy
from fractions import Fraction

def gaus(matrix, p=[[i, i] for i in range(100)]):
        """
        Метод Гауса-Жордана.
        :param matrix: исходная матрица.
        :param p: координаты каждого разрешающего элемента.
        :return: список строк для вывода подробной информации.
        """
        n = len(matrix)
        for k in range(n):
            if not one_replace(matrix, p[k][0], p[k][1]):
                return False
            #matrix_print(matrix)
        return True

def one_replace(matrix, x, y):
    """
    Итерация однократного замещения
    :param matrix: исходная матрица.
    :param x: строка
    :param y: столбец
    """
    key = copy.copy(matrix[y])
    n = len(matrix)
    if key[x] == 0: return False
    for j in range(n):
        key2 = matrix[j][x]
        for i in range(len(matrix[j])):
            matrix[j][i] = matrix[j][i] / key[x] if y == j else matrix[j][i] - key2 * key[i] / key[x]
    return True

def matrix_print(matrix):
        """
        Вывод информации о матрице.
        :param matrix: матрица
        :param h: список для записи информации.
        """
        SYMBOL_SIZE = 10
        if len(matrix) != 0:
            lenght = None
            for i in range(len(matrix)):
                string = "".join(["|" + " "*(SYMBOL_SIZE-len(str(f))) + str(f) for f in matrix[i]]) + "|"
                print(string)
                lenght = len(string)
            print("-" * (lenght))
        else:
            print("Решений нет")
        return

A = [
    ["2", "-5", "-4", "3", "1", "-26", "1", "0", "0", "0", "0"],
    ["4", "3", "1", "-5", "2", "16", "0", "1", "0", "0", "0"],
    ["-2", "3", "4", "2", "-5", "23", "0", "0", "1", "0", "0"],
    ["2", "0", "-4", "1", "3", "-13", "0", "0", "0", "1", "0"],
    ["1", "3", "-5", "-7", "-2", "11", "0", "0", "0", "0", "1"]
]

for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = Fraction(A[i][j])

print("Исходная матрица системы:")
matrix_print(A)
gaus(A)
print("Решение полученное методом\nГауса-Жордана:")
matrix_print(A)