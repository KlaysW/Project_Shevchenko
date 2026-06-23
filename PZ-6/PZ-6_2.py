# Вариант 32.
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