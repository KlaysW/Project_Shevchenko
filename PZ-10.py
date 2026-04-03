# Вариант 32.
# 1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной последовательности из целых положительных и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов:
# Элементы последней трети:
# Индекс максимального элемента последней трети:

import random

with open('file1.txt', 'w') as f1:
    f1.write(' '.join(map(str, [random.randint(-10, 10) for _ in range(6)])))

with open('file2.txt', 'w') as f2:
    f2.write(' '.join(map(str, [random.randint(-10, 10) for _ in range(6)])))


with open('file1.txt', 'r') as f1:
    list1 = list(map(int, f1.read().split()))

with open('file2.txt', 'r') as f2:
    list2 = list(map(int, f2.read().split()))

combined = list1 + list2
count = len(combined)
last_third = combined[2 * count // 3:]
max_val = max(last_third)
max_index = last_third.index(max_val)


with open('result1.txt', 'w', encoding='utf-8') as res:
    res.write(f"Элементы первого и второго файлов: {combined}\n")
    res.write(f"Количество элементов первого и второго файлов: {count}\n")
    res.write(f"Элементы последней трети: {last_third}\n")
    res.write(f"Индекс максимального элемента последней трети: {max_index}\n")

# 2. Из предложенного текстового файла (text18-32.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно вставив после каждой строки строку из символов «*».

import string


with open('text18-32.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
print("Содержимое файла:")
for line in lines:
    print(line.strip())

punc_count = 0
for line in lines[:4]:
    for char in line:
        if char in string.punctuation or char in '—«»':
            punc_count += 1
print(f"\nКоличество знаков пунктуации в первых 4 строках: {punc_count}")

with open('poem_stars.txt', 'w', encoding='utf-8') as f_out:
    for line in lines:
        f_out.write(line)
        if line.strip():
            f_out.write("*" * 10 + "\n")