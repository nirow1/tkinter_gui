import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.menu = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.help_menu = tk.Menu(self.menu, tearoff=False)
        self.sub_menu = tk.Menu(self.menu, tearoff=False)
        self.configure(menu=self.menu)
        self.setup_ui()

    def setup_ui(self):
        self.title('Canvas')
        self.geometry('700x500')

        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.menu.add_cascade(label="Elp", menu=self.help_menu)
        self.menu.add_cascade(label="Sub Menu", menu=self.sub_menu)

        self.file_menu.add_command(label="New", command=lambda: print("New File"))
        self.file_menu.add_command(label="Open", command=lambda: print("Open File"))

        help_check_str = tk.StringVar()
        self.help_menu.add_command(label="Elp entry", command=lambda: print(help_check_str.get() + " EEELP BLEASE"))
        self.help_menu.add_checkbutton(label="check", onvalue="ON", offvalue="OFF", variable=help_check_str)
        menu_button = ttk.Menubutton(self, text="Menu")
        menu_button.pack()

        button_sub_menu = tk.Menu(menu_button, tearoff=False)
        button_sub_menu.add_command(label="entry °1", command=lambda: print("test 1"))
        button_sub_menu.add_checkbutton(label="check 1")
        menu_button.configure(menu=button_sub_menu)

        menu_sub_menu = tk.Menu(self.sub_menu, tearoff=False)
        menu_sub_menu.add_command(label="shit", command=lambda: print("double shit"))
        menu_sub_menu.add_command(label="shit2", command=lambda: print("TRIPPELE shit"))
        self.sub_menu.add_command(label="important info", command=lambda: print("first shit"))
        self.sub_menu.add_cascade(label="click me", menu=menu_sub_menu)

        self.file_menu.add_separator()


if __name__ == '__main__':
    win = MainWindow()
    win.mainloop()
