import tkinter as tk
from tkinter import ttk

class Converter:
    def __init__(self):
        combo_list = ["Km", "Miles"]
        window = tk.Tk()
        window.title("Let's convert")
        self.distance_type_label = tk.Label(window,text="What is the distance type:")
        self.distance_type_combo = ttk.Combobox(window)
        self.distance_type_combo["values"] = combo_list

        self.distance_type_label.grid(column=0, row=0)
        self.distance_type_combo.grid(column=2, row=0)



        window.mainloop()
    def convert(self):
        pass
    def check_type(self):
        pass
Converter()
