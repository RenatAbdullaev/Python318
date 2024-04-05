def count_negative(arr):
    if len(arr) == 0:
        return 0
    if arr[0] < 0:
        return 1 + count_negative(arr[1:])
    else:
        return count_negative(arr[1:])


arr = [-2, 3, 8, -11, -4, 6]
result = count_negative(arr)
print("Количество отрицательных чисел в массиве:", result)
