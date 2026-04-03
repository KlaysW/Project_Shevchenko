# Вариант 32
# 1. Преобразуйте ключи словаря в список d = {'a':1, 'b':2}.

d = {'a': 1, 'b': 2}
keys_list = list(d.keys())
print(keys_list)

# 2. Организовать словарь avto, содержащий 3 ключа (марки авто) и списки из трех моделей в качестве значений.
# Обеспечить отображение вторых моделей по каждому авто, всех моделей словаря.

avto = {
    "Toyota": ["Camry", "Corolla", "Rav4"],
    "BMW": ["M5", "X5", "M3"],
    "Lada": ["Vesta", "Granta", "Niva"]
}

print("\nВторые модели по каждому авто:")
for brand in avto:
    print(brand, ":", avto[brand][1])

print("\nВсе модели из словаря:")
for models in avto.values():
    for model in models:
        print(model)