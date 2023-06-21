#Бабкин Даниил Группа 44-22-114 Вариант 2 Задание 1
import math
def calculate_value(x):
    if x > 1:
        return 1 / (x - 1)
    else:
        return 2 * math.sin(3.14 + x) ** 3

try:
    x = float(input("Введите значение x: "))
    result = calculate_value(x)
    print("Результат:", result)
except ValueError:
    print("Ошибка ввода числа")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль")
except Exception as e:
    print("Ошибка:", e)