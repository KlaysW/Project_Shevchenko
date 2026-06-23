# Вариант 2
# Приложение АБИТУРИЕНТ для автоматизации работы приемной комиссии, которая обеспечивает обработку анкетных данных абитуриентов.
# Таблица Анкета содержит следующие данные об абитуриентах: Регистрационный номер, Фамилия, Имя, Отчество, Дата Рождения,
# Награды (наличие кр. Диплома или медали (да/нет)), Адрес, выбранная Специальность.

from db import init_db

conn = init_db()
cursor = conn.cursor()

cursor.execute("SELECT * FROM Anketa WHERE specialty = 'Информационные системы'")
print("Поиск (Информационные системы):")
for row in cursor.fetchall():
    print(row)
cursor.execute("SELECT * FROM Anketa WHERE awards = 'да'")
print("\nПоиск (с наградами):")
for row in cursor.fetchall():
    print(row)
cursor.execute("SELECT * FROM Anketa WHERE reg_num = 105")
print("\nПоиск (номер 105):")
for row in cursor.fetchall():
    print(row)

cursor.execute("UPDATE Anketa SET address = 'г. Ростов, ул. Садовая 10' WHERE reg_num = 102")
cursor.execute("UPDATE Anketa SET specialty = 'Программирование' WHERE last_name = 'Новиков'")
cursor.execute("UPDATE Anketa SET awards = 'да' WHERE reg_num = 104")
conn.commit()
cursor.execute("SELECT * FROM Anketa")
print("\nИтоговая база данных после обновления:")
for row in cursor.fetchall():
    print(row)

cursor.execute("DELETE FROM Anketa WHERE reg_num = 109")
cursor.execute("DELETE FROM Anketa WHERE awards = 'нет' and specialty = 'Сетевое администрирование'")
cursor.execute("DELETE FROM Anketa WHERE last_name = 'Васильев'")
conn.commit()
cursor.execute("SELECT * FROM Anketa")
print("\nИтоговая база данных после удаления:")
for row in cursor.fetchall():
    print(row)

conn.close()