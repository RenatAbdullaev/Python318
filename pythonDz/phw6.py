import random

w, h = 3, 4
matrix = [[random.randint(-20, 10) for x in range(w)] for d in range(h)]
for row in matrix:
    for x in row:
        print(x, end="\t\t")
    print()
count = 0
for d in range(h):
    for x in range(w):
        if matrix[d][x] < 0:
            count += 1
print("\nКоличество отрицательных элементов: ", count)