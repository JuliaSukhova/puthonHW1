#Задача 26

A = int(input())
B = int(input())

def degree(A,B):
    if B == 0:
        return 1
    else:
        return A * degree(A, B - 1)

print(degree(A,B))

