import tkinter as tk
from tkinter import ttk


class GetWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.entry = ttk.Entry(master=self.window)
        self.label = ttk.Label(master=self.window, text="something")
        self.setup_ui()

    def setup_ui(self):
        self.window.title("Getting and setting widgets")
        self.window.geometry("")

        self.label.pack()

        self.entry.pack()

        button = ttk.Button(master=self.window, text="Da Button", command=self.button_func)
        button.pack()

    def button_func(self):
        entry_txt = self.entry.get()
        self.label['text'] = entry_txt
        self.entry['state'] = 'disabled'
        self.label.configure()


if __name__ == '__main__':
    wind = GetWindow()
    wind.window.mainloop()
