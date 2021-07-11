from functools import reduce  # Функция для свёрки последовательности
from operator import mul  # Функция, перемножающая 2 числа


def fact(arg):
    i = 1
    for i in range(1, arg + 1):
        yield reduce(mul, range(1, i + 1))


n = int(input('факториал какого числа нужно вычислить? '))
for el in fact(n):
    print(el)



