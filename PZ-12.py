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

# 2. В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры). reduce

n = int(input("\nВведите номер строки N (начиная с 0): "))

if 0 <= n < len(matrix):
    target_row = matrix[n]
    
    row_sum = sum(item for item in target_row)
    
    def get_prod(lst):
        res = 1
        for x in lst:
            res *= x
        return res
    
    row_mult = get_prod(target_row)
        
    print(f"\nВыбранная строка {n}: {target_row}")
    print(f"Сумма элементов: {row_sum}")
    print(f"Произведение элементов: {row_mult}")
else:
    print("Ошибка: строка отсутствует")