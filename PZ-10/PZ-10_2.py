# 
# 2. Из предложенного текстового файла (text18-32.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно вставив после каждой строки строку из символов «*».

import string


with open('PZ-10/text18-32.txt', 'r', encoding='utf-8') as f:
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

with open('PZ-10/poem_stars.txt', 'w', encoding='utf-8') as f_out:
    for line in lines:
        f_out.write(line)
        if line.strip():
            f_out.write("*" * 10 + "\n")