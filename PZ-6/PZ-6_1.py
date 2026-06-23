# Вариант 32.
# 1. Дан список размера N. Поменять местами его минимальный и максимальный элементы.

N = int(input("N: "))
A = [float(input(f"A[{i}]: ")) for i in range(N)]

if N > 0:
    min_idx = A.index(min(A))
    max_idx = A.index(max(A))
    A[min_idx], A[max_idx] = A[max_idx], A[min_idx]
    print(f"Результат: {A}")