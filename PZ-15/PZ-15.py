# Вариант 2
# Приложение АБИТУРИЕНТ для автоматизации работы приемной комиссии, которая обеспечивает обработку анкетных данных абитуриентов.
# Таблица Анкета содержит следующие данные об абитуриентах: Регистрационный номер, Фамилия, Имя, Отчество, Дата Рождения,
# Награды (наличие кр. Диплома или медали (да/нет)), Адрес, выбранная Специальность.

from db import init_db

conn = init_db()
cursor = conn.cursor()

cursor.execute("select * from Anketa where specialty = 'Информационные системы'")
print("Поиск (Информационные системы):")
for row in cursor.fetchall():
    print(row)
cursor.execute("select * from Anketa where awards = 'да'")
print("\nПоиск (с наградами):")
for row in cursor.fetchall():
    print(row)
cursor.execute("select * from Anketa where reg_num = 105")
print("\nПоиск (номер 105):")
for row in cursor.fetchall():
    print(row)

cursor.execute("update Anketa set address = 'г. Ростов, ул. Садовая 10' where reg_num = 102")
cursor.execute("update Anketa set specialty = 'Программирование' where last_name = 'Новиков'")
cursor.execute("update Anketa set awards = 'да' where reg_num = 104")
conn.commit()
cursor.execute("select * from Anketa")
print("\nИтоговая база данных после обновления:")
for row in cursor.fetchall():
    print(row)

cursor.execute("delete from Anketa where reg_num = 109")
cursor.execute("delete from Anketa where awards = 'нет' and specialty = 'Сетевое администрирование'")
cursor.execute("delete from Anketa where last_name = 'Васильев'")
conn.commit()
cursor.execute("select * from Anketa")
print("\nИтоговая база данных после удаления:")
for row in cursor.fetchall():
    print(row)

conn.close()