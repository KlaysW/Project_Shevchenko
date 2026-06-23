# Вариант 32.
# 2. Создайте базовый класс "Человек" со свойствами "имя", "возраст" и "пол".
# От этого класса унаследуйте классы "Мужчина" и "Женщина" и добавьте в них свойства,
# связанные с социальным положением (например, "семейное положение", "количество детей" и т.д.).

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")

class Man(Person):
    def __init__(self, name, age, marital_status, military_service):
        super().__init__(name, age, "Мужской")
        self.marital_status = marital_status
        self.military_service = military_service

    def display_info(self):
        super().display_info()
        print(f"Семейное положение: {self.marital_status}, Военная служба: {self.military_service}")
        
class Woman(Person):
    def __init__(self, name, age, marital_status, children_count):
        super().__init__(name, age, "Женский")
        self.marital_status = marital_status
        self.children_count = children_count

    def display_info(self):
        super().display_info()
        print(f"Семейное положение: {self.marital_status}, Количество детей: {self.children_count}")

man = Man("Алексей", 28, "Женат", "Военнообязанный")
woman = Woman("Елена", 25, "Замужем", 2)

print("\nИнформация о мужчине:")
man.display_info()

print("\nИнформация о женщине:")
woman.display_info()