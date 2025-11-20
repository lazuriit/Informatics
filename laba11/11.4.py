import tkinter as tk

root = tk.Tk()
root.title("Загадочная программа")
root.geometry("400x150")

click_count = 0

def click():
    global click_count
    click_count += 1

    if click_count == 7:
        result_label.config(text="Ты настойчив! Вот тебе сюрприз: ты победил!")


button = tk.Button(text="Запустить", command=click)
button.pack()

result_label = tk.Label(text="")
result_label.pack()

root.mainloop()