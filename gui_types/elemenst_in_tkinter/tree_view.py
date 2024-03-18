import tkinter as tk
from tkinter import ttk
from random import choice


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.table = ttk.Treeview(self, columns=('first', 'last', 'email'), show='headings')
        self.setup_ui()

    def setup_ui(self):
        self.title('Canvas')
        self.geometry('700x500')

        first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan']
        second_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook']
        emails = ['gmail.com', 'outlook.com', 'seznam.cz']

        self.table.heading('first', text='First name')
        self.table.heading('last', text='Last name')
        self.table.heading('email', text='Email')
        self.table.pack(fill='both', expand=True)

        for i in range(1, 101):
            fn = choice(first_names)
            sn = choice(second_names)
            self.table.insert(parent='', index=0, values=(fn, sn, f"{fn.lower()}.{sn.lower()}@{choice(emails)}"))

        self.table.insert(parent='', index=tk.END, values=("XXXX", "YYYY", "ZZZZ"))

        #  events
        self.table.bind('<<TreeviewSelect>>', self.item_select)
        self.table.bind('<Delete>', self.delete_items)

    def item_select(self, _):
        for i in self.table.selection():
            print(self.table.item(i)['values'])

    def delete_items(self, _):
        for i in self.table.selection():
            self.table.delete(i)


if __name__ == '__main__':
    win = MainWindow()
    win.mainloop()
