## Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
## Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
## В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
## *Пример:*
## 5
##  1 2 3 4 5
## 6
##  -> 5

import random 
#n= int(input('Введите длину массива: '))
#list = [randint(1, 10) for _ in range(n)]
#print(*list)
#x = int(input('Введите число: '))
#y =  0
#for i in range(len(list)):
    #if (x - list[i]) < x -y and x- list[i]>0:
     #   y = list[i]  
#print(f'Самое близкое число к заданному: {y}')

list = [random.randint(0, 40) for _ in range(10)]
print(*list)
x = int(input('Введите число: '))
nearest_num = list[0]
dist = abs(x -nearest_num)

for num in list:
    if abs(num - x) < dist:
        dist = abs(num - x)
        nearest_num = num

if list.count(x):
    print(f'Заданное число встречается {list.count(x)} раз')
else:
    print(f'Самое близкое число к заданному {x} является {nearest_num}')

 


