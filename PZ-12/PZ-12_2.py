# Вариант 32.
# 2. В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).

import random
from functools import reduce

rows, cols = random.randint(3, 10), random.randint(3, 10)
matrix = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

print("Исходная матрица:")
list(map(print, matrix))

n = int(input("\nВведите номер строки N (начиная с 0): "))

if 0 <= n < len(matrix):
    target_row = list(filter(lambda _, i=n: True, matrix))[n]

    row_sum = reduce(lambda acc, x: acc + x, target_row)
    row_mult = reduce(lambda acc, x: acc * x, target_row)

    print(f"\nВыбранная строка {n}: {target_row}")
    print(f"Сумма элементов: {row_sum}")
    print(f"Произведение элементов: {row_mult}")
else:
    print("Ошибка: строка отсутствует")