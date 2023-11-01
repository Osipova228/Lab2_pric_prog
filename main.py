# Задание #19
# Напишите программу, которая строит на экране столбчатую гистограмму
# успеваемости студентов в группе.
import tkinter as tk


def gistogram():
    data = entry_data.get()
    data = list(map(int, data.split()))

    graph_window = tk.Toplevel(root)
    graph_window.title("Гистограмма успеваемости")

    canvas = tk.Canvas(graph_window, width=400, height=300)
    canvas.pack()

    bar_width = 30
    x = 20
    y_max = max(data)
    for i, value in enumerate(data):
        height = (value / y_max) * 250
        canvas.create_rectangle(x, 250 - height, x + bar_width, 250, fill="blue")
        canvas.create_text(x + bar_width / 2, 260, text=str(value))
        canvas.create_text(x + bar_width / 2, 270, text=f"Студент {i + 1}")
        x += 50


root = tk.Tk()
root.title("Успеваемость студентов")

label_data = tk.Label(root, text="Введите оценки студентов через пробел:")
label_data.pack()
entry_data = tk.Entry(root)
entry_data.pack()

plot_button = tk.Button(root, text="Построить гистограмму", command=gistogram)
plot_button.pack()

root.mainloop()
