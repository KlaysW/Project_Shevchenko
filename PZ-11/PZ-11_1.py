# Вариант 32.
# 1.В последовательности на n целых чисел умножить все элементы на первый максимальный элемент.

import random

def mbm(n):
    nums = [random.randint(-10, 10) for i in range(n)]
    print("Исходная последовательность:", nums)
    if not nums:
        return []
    
    first_max = max(nums)
    return list(map(lambda x: x * first_max, nums))

n_val = int(input("Введите количество элементов n: "))
print("Результат:", mbm(n_val))