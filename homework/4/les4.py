#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).


n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
k = int(input("Введите число k: "))

if k >= n * m:
    print("no")
else:
    if k % n == 0 or k % m == 0:
        print("yes")
    else:
        print("no")