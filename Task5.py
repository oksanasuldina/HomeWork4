from functools import reduce  # Функция для свёрки последовательности
from operator import mul  # Функция, перемножающая 2 числа
my_list = [el for el in range(100, 1001) if el % 2 == 0]
# в задаче конкретизировали включить границы,
# поэтому от 100 (включая 100) до 1001 (включая 1000)
print(f"список: {my_list}")
print(f"произведение всех элементов списка: {reduce(mul, my_list)}")
