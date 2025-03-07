import tkinter as tk
from tkinter import ttk

class Converter:
    def __init__(self):
        self.distance_type = ""
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
        self.convert_button = tk.Button(window, text="Convert", command=self.check_type)
        self.output_box = tk.Label(window, text= " ")


        self.distance_type_label.grid(column=0, row=0)
        self.distance_type_combo.grid(column=1, row=0)
        self.distance_label.grid(column=0, row=1)
        self.distance_entry.grid(column=1, row=1)
        self.convert_button.grid(column=0, row=2, columnspan=2)
        self.output_box.grid(column=0, row=3, columnspan=2)



        window.mainloop()

    def convert(self, something):
        distance = self.distance_entry.get()
        value = float(distance) * something
        self.output(value)

    def check_type(self):
        distance_type = self.distance_type_combo.get()
        if distance_type == "Km":
            self.distance_type = "Miles"
            self.convert(0.6213711922)
        elif distance_type == "Miles":
            self.distance_type = "Km"
            self.convert(1.609344)

    def output(self, values):
        value = round(values,2)
        output = f"It's {value} {self.distance_type}"
        self.output_box.config(text=output)
        self.output_box.update()




Converter()
