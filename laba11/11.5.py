import tkinter as tk
import random

root = tk.Tk()
root.title("Секретная кнопка")
root.geometry("400x200")

secret_button = random.randint(1, 4)

def click(button_number):
    if button_number == secret_button:
        result_label.config(text="Поздравляем! Ты нашёл секрет!")
    else:
        result_label.config(text="Попробуй ещё!")

button1 = tk.Button(root, text="Кнопка 1", command=lambda: click(1))
button1.pack(pady=5)

button2 = tk.Button(root, text="Кнопка 2", command=lambda: click(2))
button2.pack(pady=5)

button3 = tk.Button(root, text="Кнопка 3", command=lambda: click(3))
button3.pack(pady=5)

button4 = tk.Button(root, text="Кнопка 4", command=lambda: click(4))
button4.pack(pady=5)


result_label = tk.Label(text="")
result_label.pack(pady=10)

root.mainloop()