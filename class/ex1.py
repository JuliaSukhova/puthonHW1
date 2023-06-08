def subtract_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Array sizes don't match")
    
    result = []
    for i in range(len(array1)):
        result.append(array1[i] - array2[i])
    
    return result


def divide_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Array sizes don't match")
    
    result = []
    for i in range(len(array1)):
        if array2[i] == 0:
            raise ZeroDivisionError("Division by zero")
        
        result.append(array1[i] / array2[i])
    
    return result


def sum_2d_array(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            try:
                val = int(arr[i][j])
                sum += val
            except ValueError:
                print(f"Invalid number format at row {i}, column {j}")
            except IndexError:
                print(f"Array index out of bounds at row {i}, column {j}")
    
    return sum