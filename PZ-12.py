# Вариант 32.
# 1. Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.

matrix = [
    [-1, -2, 3],
    [4, 5, -6],
    [-7, -8, 9]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

positive = any(item > 0 for row in matrix for item in row)
print(positive)

# 2. В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).

n = int(input("\nВведите номер строки N (начиная с 0): "))

if 0 <= n < len(matrix):
    target_row = matrix[n]
    row_sum = sum(target_row)
    
    row_mult = 1
    for item in target_row:
        row_mult *= item
        
    print(f"Строка {n}: {target_row}")
    print(f"Сумма: {row_sum}")
    print(f"Произведение: {row_mult}")
else:
    print("Строки с таким номером нет в матрице")