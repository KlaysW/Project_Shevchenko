# Вариант 32
# 1. Дан список размера N. Поменять местами его минимальный и максимальный элементы.

N = int(input("N: "))
A = [float(input(f"A[{i}]: ")) for i in range(N)]

if N > 0:
    min_idx = A.index(min(A))
    max_idx = A.index(max(A))
    A[min_idx], A[max_idx] = A[max_idx], A[min_idx]
    print(f"Результат: {A}")

# 2. Дан список А размера N. Сформировать новый список В того же размера по следующему правилу:
# элемент Вк равен сумме элементов списка А с номерами от К до N.

N = int(input("N: "))
A = [float(input(f"A[{i}]: ")) for i in range(N)]

B = [0] * N
current_sum = 0

for i in range(N-1, -1, -1):
    current_sum += A[i]
    B[i] = current_sum

print(f"Список B: {B}")

# 3. Дан список размера N. Осуществить циклический сдвиг элементов списка вправо на одну позицию
# (при этом A1 перейдет в А2, A2 - в Аз,…, An - в A1).

N = int(input("N: "))
A = [float(input(f"A[{i}]: ")) for i in range(N)]

if N > 0:
    A = [A[-1]] + A[:-1]
    print(f"После сдвига: {A}")