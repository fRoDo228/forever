import tkinter as tk

# Создание окна
window = tk.Tk()
window.title("Шахматная доска")

# Размеры клетки на доске
cell_size = 80

# Создание холста
canvas = tk.Canvas(window, width=8 * cell_size, height=8 * cell_size)
canvas.pack()

# Отрисовка шахматной доски
for row in range(8):
    for col in range(8):
        x1 = col * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        if (row + col) % 2 == 0:
            canvas.create_rectangle(x1, y1, x2, y2, fill="white")
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill="gray")

# Запуск главного цикла событий
window.mainloop()
