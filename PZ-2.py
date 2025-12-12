K = int(input("Введите день года (1-365): "))
start_day = 6  # 1 января = суббота (6)

day_of_week = (K + start_day - 2) % 7 + 1

if day_of_week == 1:
    day_of_week = "Понедельник"
elif day_of_week == 2:
    day_of_week = "Вторник"
elif day_of_week == 3:
    day_of_week = "Среда"
elif day_of_week == 4:
    day_of_week = "Четверг"
elif day_of_week == 5:
    day_of_week = "Пятница"
elif day_of_week == 6:
    day_of_week = "Суббота"
elif day_of_week == 7:
    day_of_week = "Воскресенье"

print(day_of_week)