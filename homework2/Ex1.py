#Задача 10

n = int(input("Введите количество монеток: "))

coins = input("Введите расположение монеток что на столе лежат (R - решка вверх, G - герб вверх): ")

counter = 0

if coins:
    for coin in coins:
        if coin != coins[0]:
            counter += 1
print( counter)