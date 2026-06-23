# Вариант 32.
# Задание 2. "В последовательности на n целых чисел умножить все элементы на первый максимальный элемент."

import tkinter as tk
import random

def solve_task_2():
    try:
        count = int(entry_input.get())
        nums = [random.randint(-10, 10) for _ in range(count)]
        
        m_val = max(nums)
        res = [x * m_val for x in nums]
        
        label_output.config(text=f"Сгенерированные числа: {nums}\nМаксимальное число: {m_val}\nРезультат: {res}")
    except ValueError:
        label_output.config(text="Ошибка ввода. Введите целое число.")

root = tk.Tk()
root.title("Задание 2")
root.geometry("400x200")

tk.Label(root, text="Введите количество цифр:").pack(pady=5)
entry_input = tk.Entry(root, width=40)
entry_input.pack(pady=5)

tk.Button(root, text="Выполнить", command=solve_task_2).pack(pady=5)
label_output = tk.Label(root, text="Результат: ", justify="left")
label_output.pack(pady=10)

root.mainloop()