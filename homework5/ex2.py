#Задача28

def decimal_to_binary(n):
    if n > 0:
        return decimal_to_binary(n // 2) + str(n % 2)
    else:
        return ""

decimal_number = int(input("Введите число: "))
binary_number = decimal_to_binary(decimal_number)
print(binary_number)