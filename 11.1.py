import tkinter as tk
import random

def show_message():
    messages = [
        "Ты сегодня сделаешь что-то крутое!",
        "Сегодня — хороший день для чая.",
        "Тебя следующая оценка — 5!"
    ]
    label.config(text=random.choice(messages))

root = tk.Tk()
root.title("Случайное предсказание")
root.geometry("300x150")

button = tk.Button(text="Скажи мне что-нибудь", command=show_message)
button.pack()

label = tk.Label(text="")
label.pack()

root.mainloop()