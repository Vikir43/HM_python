# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

my_list = [random.randint(-10, 20) for _ in range(15)]
print(my_list)
min = int(input('Введите минимум: '))
max = int(input('Введите максимум: '))

for i in range(15):
    ind = [i for i, v in enumerate(my_list) if min <= v <= max]
print(f'Список индексов в заданном диапозоне {ind}')