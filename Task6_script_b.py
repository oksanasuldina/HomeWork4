from itertools import cycle

my_list = [100, 200, 300]
с = 1
for el in cycle(my_list):
    if с > 9:
        break
    print(el)
    с += 1