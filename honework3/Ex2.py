#Задача18

N = int(input()) 
A = [int(i) for i in input().split()]
X = int(input())  

closest = A[0] 
min_diff = A[0] - X  # Переменная для хранения мин
if min_diff < 0:
    min_diff *= -1

for i in range(1, N):  # Перебираем каждый элемент массива A
    diff = A[i] - X  
    if diff < 0:
        diff *= -1  
    if diff < min_diff: 
        closest = A[i]
        min_diff = diff

print(closest)