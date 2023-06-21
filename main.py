#Бабкин Даниил Группа 44-22-114 Вариант 2 Задание 3
import tkinter as tk
import math

def calculate_value(x):
    if x > 1:
        return 1 / (x - 1)
    else:
        return 2 * math.sin(3.14 + x) ** 3

def calculate_button_click():
    try:
        x = float(entry.get())
        result = calculate_value(x)
        result_label.config(text="Результат: " + str(result))
    except ValueError:
        result_label.config(text="Ошибка ввода числа")
    except ZeroDivisionError:
        result_label.config(text="Ошибка: Деление на ноль")
    except Exception as e:
        result_label.config(text="Ошибка: " + str(e))

window = tk.Tk()
window.title("Вычисление значения")
window.geometry("300x150")

label = tk.Label(window, text="Введите значение x:")
label.pack()

entry = tk.Entry(window)
entry.pack()

calculate_button = tk.Button(window, text="Вычислить", command=calculate_button_click)
calculate_button.pack()

result_label = tk.Label(window, text="Результат:")
result_label.pack()

window.mainloop()