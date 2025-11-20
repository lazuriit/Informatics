import tkinter as tk
import random

root = tk.Tk()
root.title("Угадай число")
root.geometry("300x200")

secret_number = random.randint(1, 100)

def check_guess():
    try:
        guess = int(entry.get())

        if guess == secret_number:
            result_label.config(text="Ты угадал!")
        elif guess < secret_number:
            result_label.config(text="Больше!")
        else:
            result_label.config(text="Меньше!")

    except ValueError:
        result_label.config(text="Введите число!")


label_info = tk.Label(text="Я загадал число от 1 до 100!")
label_info.pack()

entry = tk.Entry()
entry.pack()

button = tk.Button(text="Угадать", command=check_guess)
button.pack()

result_label = tk.Label(text="")
result_label.pack()

root.mainloop()