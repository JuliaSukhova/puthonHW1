#Задача 22

n = [int(i) for i in input().split()]
m = [int(k) for k in input().split()]

common = set(n) & set(m)

for num in sorted(common):
    print(num, end=" ")