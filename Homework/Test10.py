## На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
## Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
## вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
from random import randint
coin = int(input("Введите количество монеток: "))
eagle = 0 
tails = 0
for i in range(coin):
    coin_1 = randint(0, 1)
    print(coin_1, end =' ')
    if coin_1 == 0:
        eagle += 1
    else:
        tails += 1    
print()
print(f'Всего монет орлом вверх - {eagle}, решкой вверх {tails}')
if eagle < tails:
    print(f'Меньше монет орлом вверх {eagle}')
elif eagle == tails:
    print("Монет одинаковое количество")
else:
    print(f'Меньше монет решкой вверх {tails}')