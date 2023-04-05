## Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
## num = int(input('Введите число: '))

n = int(input('Введите число ограничение: '))
match = 1
while match < n:    
        if  match * 2 > n:
            break
        else:
            match = match * 2
            print(match, end= ' ')

n = int (input())
i = 0
while 2 ** i<= n:
     print(2 ** i)
     i +=1