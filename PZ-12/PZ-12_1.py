# Вариант 32.
# 1. Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.

import random

rows, cols = random.randint(3, 10), random.randint(3, 10)
matrix = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(row)
    
has_positive = any(item > 0 for row in matrix for item in row)
print(f"\nНаличие положительных элементов: {has_positive}")