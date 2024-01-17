import tkinter as tk
from datetime import datetime
from tkcalendar import DateEntry

def determine_season():
    try:
        date_object = entry.get_date()
        month = date_object.month

        if 3 <= month <= 5:
            result_label.config(text="Весна")
        elif 6 <= month <= 8:
            result_label.config(text="Лето")
        elif 9 <= month <= 11:
            result_label.config(text="Осень")
        else:
            result_label.config(text="Зима")
    except ValueError:
        result_label.config(text="Ошибка в формате даты")

# Создаем графический интерфейс
app = tk.Tk()
app.title("Определение времени года")

# Создаем элементы интерфейса с использованием DateEntry
label = tk.Label(app, text="Выберите дату:")
label.pack(pady=10)

entry = DateEntry(app, date_pattern="dd-mm-yyyy")
entry.pack(pady=10)

button = tk.Button(app, text="Определить время года", command=determine_season)
button.pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

# Запускаем главный цикл приложения
app.mainloop()