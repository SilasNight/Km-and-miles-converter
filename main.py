import tkinter as tk
from tkinter import ttk

class Converter:
    def __init__(self):
        combo_list = ["Km", "Miles"]
        window = tk.Tk()
        window.title("Let's convert")
        window.config(padx=20, pady=20)
        window.update()
        self.distance_type_label = tk.Label(window,text="What is the distance type:")
        self.distance_type_combo = ttk.Combobox(window)
        self.distance_type_combo["values"] = combo_list
        self.distance_label = tk.Label(window, text="How far is the distance?")
        self.distance_entry = tk.Entry(window, )


        self.distance_type_label.grid(column=0, row=0)
        self.distance_type_combo.grid(column=1, row=0)
        self.distance_label.grid(column=0, row=1)
        self.distance_entry.grid(column=1, row=1)



        window.mainloop()
    def convert(self):
        pass
    def check_type(self):
        pass
Converter()
