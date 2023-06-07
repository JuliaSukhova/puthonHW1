#Задача32

def find_indexes(lst, minimum, maximum):
    indexes = []
    for i, value in enumerate(lst):
        if minimum <= value <= maximum:
            indexes.append(i)
    return indexes

my_list = [1, 5, 3, 7, 10, 2, 6, 8]
min_value = 3
max_value = 7

result = find_indexes(my_list, min_value, max_value)
print("Индексы элементов, значения которых находятся в диапазоне от", min_value, "до", max_value, ":")
print(result)