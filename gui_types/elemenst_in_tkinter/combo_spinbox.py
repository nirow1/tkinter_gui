import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.title("Window with widgets")
        self.geometry('500x400')

        # combobox
        items = ["cum", "juzz", "load"]
        sperm_string = tk.StringVar(value=items[0])
        combo = ttk.Combobox(self)
        combo["values"] = items
        combo.pack()
        combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text=f"Selected val: {sperm_string.get()}"))
        combo_label = ttk.Label(self, text="a label")
        combo_label.pack()

        # spinbox
        spin_int = tk.IntVar(value=12)
        spinbox = ttk.Spinbox(self, from_=3, to=20,
                              command=lambda: print(spin_int.get()), textvariable=spin_int)
        spinbox.bind('<<Increment>>', lambda event: print("up"))
        spinbox.bind('<<Decrement>>', lambda event: print("down"))
        # spinbox['value'] = [1, 2, 3, 4]
        spinbox.pack()


if __name__ == '__main__':
    wind = MainWindow()
    wind.mainloop()
