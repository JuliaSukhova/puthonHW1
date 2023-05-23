#Задача 12

S = int(input("Введите сумму (S): "))
P = int(input("Введите произведение (P): "))

for X in range(1, 1001):
    for Y in range(1, 1001):
        if X + Y == S and X * Y == P:

            print(X,Y)