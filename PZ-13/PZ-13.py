# Вариант 32.
# 32. Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать количество полученных элементов.

import re

with open('experience.txt', 'r', encoding='utf-8') as file:
    content = file.read()

pattern = r'\d+\s+(?:лет|года|год)(?:\s+\d+\s+(?:месяцев|месяца|месяц))?'

experience_list = re.findall(pattern, content)

print("Список стажа работы:")
for item in experience_list:
    print(item)

count = len(experience_list)
print(f"\nКоличество полученных элементов: {count}")