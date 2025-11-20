import tkinter as tk

root = tk.Tk()
root.title("Светофор")
root.geometry("300x150")

tk.Button(text="Красный", command=lambda: root.config(bg="red")).pack(pady=5)
tk.Button(text="Жёлтый", command=lambda: root.config(bg="yellow")).pack(pady=5)
tk.Button(text="Зелёный", command=lambda: root.config(bg="green")).pack(pady=5)

root.mainloop()