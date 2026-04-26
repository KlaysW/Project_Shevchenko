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

# 2.Из заданной строки отобразить только символы пунктуации. Использовать библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

import string

def gp(text):
    return "".join(filter(lambda char: char in string.punctuation, text))

line = '--msg-template="$FileDir$\\{path}:{line}:{column}:{C}:({symbol}){msg}"'
print("\nСимволы пунктуации в строке:", gp(line))