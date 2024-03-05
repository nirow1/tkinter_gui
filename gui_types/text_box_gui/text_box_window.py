import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.title("Window with widgets")
        self.geometry('800x500')

        label = ttk.Label(master=self, text="This is a test")
        label.pack()

        text = tk.Text(master=self)
        text.pack()

        entry = ttk.Entry(master=self)
        entry.pack()

        button = ttk.Button(master=self, text="A button", command=self.button_function)
        button.bind('<Alt-KeyPress-a>', lambda event: print('an event'))
        button.pack()

        self.bind("<KeyPress>", lambda event: print(f"a button was pressed ({event.char})"))
        self.bind("<Motion>", self.get_pos)

        entry.bind("<FocusIn>", lambda event: print("entry field was selected"))
        entry.bind("<FocusOut>", lambda event: print("entry field was selected"))

        text.bind("<Shift-MouseWheel>", lambda event: print("mousewheel"))

    def button_function(self):
        print("button pressed")

    def get_pos(self, event):
        print(f"x: {event.x} y: {event.y}")


if __name__ == '__main__':
    window = MainWindow()
    window.mainloop()
