#Задача 26

A = int(input())
B = int(input())

def expanent(A,B):
    if B == 0:
        return 1
    else:
        return A * expanent(A, B - 1)

print(expanent(A,B))

