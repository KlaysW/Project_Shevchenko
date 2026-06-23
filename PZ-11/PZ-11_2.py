# Вариант 32.
# 2.Из заданной строки отобразить только символы пунктуации. Использовать библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

import string

def gp(text):
    return "".join(filter(lambda char: char in string.punctuation, text))

line = '--msg-template="$FileDir$\\{path}:{line}:{column}:{C}:({symbol}){msg}"'
print("\nСимволы пунктуации в строке:", gp(line))