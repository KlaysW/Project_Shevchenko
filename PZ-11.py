# Вариант 32.
# 1.В последовательности на n целых чисел умножить все элементы на первый максимальный элемент.

n = int(input("Введите количество элементов n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Введите {i+1}-е число: ")))

if nums:
    max_val = max(nums)
    # Умножаем каждый элемент на первый найденный максимальный
    for i in range(len(nums)):
        nums[i] *= max_val

print("Результат умножения:", nums)

# 2.Из заданной строки отобразить только символы пунктуации. Использовать библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

import string

text = '--msg-template="$FileDir$\\{path}:{line}:{column}:{C}:({symbol}){msg}"'
result_punctuation = ""

for char in text:
    if char in string.punctuation:
        result_punctuation += char

print("\nСимволы пунктуации в строке:", result_punctuation)