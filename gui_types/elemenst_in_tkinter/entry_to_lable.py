import tkinter as tk
from tkinter import ttk


class EntryToLabel(tk.Tk):
    def __init__(self):
        super(EntryToLabel, self).__init__()
        self.string_var = tk.StringVar()
        self.label = ttk.Label(master=self, text='label', textvariable=self.string_var)
        self.entry = ttk.Entry(master=self, textvariable=self.string_var)
        self.button = ttk.Button(master=self, text='button', command=self.button_func)

        self.setup_ui()

    def setup_ui(self):
        self.title("Tkinter Variables")
        self.geometry('300x200')

        self.label.pack()

        self.entry.pack()
        self.button.pack()

    def button_func(self):
        self.string_var.set('button pressed')


if __name__ == '__main__':
    wind = EntryToLabel()
    wind.mainloop()
