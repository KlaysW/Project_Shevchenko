# Вариант 32
# Задание 1. В соответствии с номером варианта перейти по ссылке на прототип. Реализовать его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально приближенный к оригиналу.

import tkinter as tk
from tkinter import ttk

def submit_form():
    print("Форма отправлена")

root = tk.Tk()
root.title("ALL FIELDS FORM")
root.geometry("620x860")
root.resizable(False, False)
root.configure(bg="#f8f9fa")

container = tk.Frame(root, bg="#f8f9fa")
container.pack(fill="both", expand=True, padx=10, pady=10)

canvas = tk.Canvas(container, bg="#f8f9fa", highlightthickness=0)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#f8f9fa", padx=0, pady=0)

window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def resize_window(event):
    canvas.itemconfig(window_id, width=event.width)

scrollable_frame.bind("<Configure>", update_scrollregion)
canvas.bind("<Configure>", resize_window)
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

card_frame = tk.Frame(scrollable_frame, bg="white", bd=1, relief="solid", padx=30, pady=30)
card_frame.pack(fill="x", expand=False, padx=10, pady=20)

tk.Label(card_frame, text="ALL FIELDS FORM", font=("TimesNewRoman", 18, "bold"), bg="white", fg="#4a7ebB").grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 20))

form_frame = tk.Frame(card_frame, bg="white")
form_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
form_frame.columnconfigure(1, weight=0)

label_opts = {"font": ("TimesNewRoman", 10), "bg": "white", "anchor": "w"}
entry_opts = {"bd": 1, "relief": "solid", "bg": "white"}

row = 0

tk.Label(form_frame, text="Textfield", **label_opts).grid(row=row, column=0, sticky="w", pady=10, padx=(0, 20))
tk.Entry(form_frame, width=38, **entry_opts).grid(row=row, column=1, sticky="w", pady=10, ipady=5)
row += 1

tk.Label(form_frame, text="Textarea", **label_opts).grid(row=row, column=0, sticky="nw", pady=10, padx=(0, 20))
textarea = tk.Text(form_frame, width=38, height=8, bd=1, relief="solid", bg="white")
textarea.grid(row=row, column=1, sticky="w", pady=10)
row += 1

tk.Label(form_frame, text="Email Address", **label_opts).grid(row=row, column=0, sticky="w", pady=10, padx=(0, 20))
tk.Entry(form_frame, width=38, **entry_opts).grid(row=row, column=1, sticky="w", pady=10, ipady=5)
row += 1

tk.Label(form_frame, text="Dropdown", **label_opts).grid(row=row, column=0, sticky="w", pady=10, padx=(0, 20))
combo = ttk.Combobox(form_frame, values=["Option 1", "Option 2", "Option 3"], state="readonly", width=30)
combo.current(0)
combo.grid(row=row, column=1, sticky="w", pady=10)
row += 1

radio_var = tk.IntVar(value=1)
tk.Label(form_frame, text="Radio Button", **label_opts).grid(row=row, column=0, sticky="nw", pady=10, padx=(0, 20))
radio_frame = tk.Frame(form_frame, bg="white")
radio_frame.grid(row=row, column=1, sticky="w", pady=10)
tk.Radiobutton(radio_frame, text="Option 1", variable=radio_var, value=1, bg="white").pack(anchor="w", pady=2)
tk.Radiobutton(radio_frame, text="Option 2", variable=radio_var, value=2, bg="white").pack(anchor="w", pady=2)
row += 1

label_checkbox = tk.Label(form_frame, text="Checkbox", **label_opts)
label_checkbox.grid(row=row, column=0, sticky="nw", pady=10, padx=(0, 20))
checkbox_frame = tk.Frame(form_frame, bg="white")
checkbox_frame.grid(row=row, column=1, sticky="w", pady=10)
tk.Checkbutton(checkbox_frame, text="Option 1", bg="white").pack(anchor="w", pady=2)
tk.Checkbutton(checkbox_frame, text="Option 2", bg="white").pack(anchor="w", pady=2)
tk.Checkbutton(checkbox_frame, text="Option 3", bg="white").pack(anchor="w", pady=2)
row += 1

tk.Label(form_frame, text="Password", **label_opts).grid(row=row, column=0, sticky="w", pady=10, padx=(0, 20))
tk.Entry(form_frame, width=38, bd=1, relief="solid", show="*", bg="#ffffd8").grid(row=row, column=1, sticky="w", pady=10, ipady=5)
row += 1

tk.Label(form_frame, text="Number Field", **label_opts).grid(row=row, column=0, sticky="w", pady=10, padx=(0, 20))
tk.Entry(form_frame, width=26, **entry_opts).grid(row=row, column=1, sticky="w", pady=10, ipady=5)
row += 1

math_label = tk.Label(form_frame, text="Mathematical Captcha", **label_opts)
math_label.grid(row=row, column=0, sticky="w", pady=10, padx=(0, 20))
math_frame = tk.Frame(form_frame, bg="white")
math_frame.grid(row=row, column=1, sticky="w", pady=10)
tk.Label(math_frame, text="6 + 8 =", bg="white", font=("TimesNewRoman", 10)).pack(side="left")
tk.Entry(math_frame, width=18, bd=1, relief="solid").pack(side="left", padx=(10, 0), ipady=4)
row += 1

captcha_box = tk.Frame(form_frame, bd=1, relief="solid", bg="#f7f9fb", padx=10, pady=10)
captcha_box.grid(row=row, column=0, columnspan=2, sticky="w", pady=(15, 20))
tk.Checkbutton(captcha_box, text="I'm not a robot", bg="#f7f9fb").pack(side="left")
row += 1

submit_button = tk.Button(form_frame, text="Submit", bg="#5dade2", fg="white", font=("TimesNewRoman", 10, "bold"), bd=0, padx=24, pady=10, command=submit_form)
submit_button.grid(row=row, column=0, columnspan=2, sticky="w")

# Задание 2. "В последовательности на n целых чисел умножить все элементы на первый максимальный элемент."
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

task2_win = tk.Toplevel(root)
task2_win.title("Задание 2")
task2_win.geometry("400x200")

tk.Label(task2_win, text="Введите количество цифр:").pack(pady=5)
entry_input = tk.Entry(task2_win, width=40)
entry_input.pack(pady=5)

tk.Button(task2_win, text="Выполнить", command=solve_task_2).pack(pady=5)
label_output = tk.Label(task2_win, text="Результат: ", justify="left")
label_output.pack(pady=10)

root.mainloop()