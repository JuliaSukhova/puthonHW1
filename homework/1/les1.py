# Задача 2: Найдите сумму цифр трехзначного числа.

n = int(input("Введите число "))

a = 0

while n > 0:
    a = a+n % 10
    n = n // 10
print(a)