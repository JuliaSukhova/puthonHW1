#Задача 16:

N = int(input()) 
A = [int(i) for i in input().split()]  
X = int(input()) 

count = 0 

for num in A:  
    if num == X: 
        count += 1

print(count) 