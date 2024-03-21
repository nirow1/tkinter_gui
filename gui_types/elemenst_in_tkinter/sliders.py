import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.scale_float = tk.DoubleVar(value=12.5)
        self.progress = ttk.Progressbar(self, variable=self.scale_float, maximum=25, length=400)
        self.scale = ttk.Scale(self, command=lambda val: print(self.scale_float.get()), from_=0,
                               to=25, length=300, variable=self.scale_float)
        self.scrolled_text = scrolledtext.ScrolledText(self, width=50, height=10)
        self.my_scale_float = tk.DoubleVar()
        self.my_progress = ttk.Progressbar(self, orient="vertical", variable=self.my_scale_float, maximum=50, length=400)
        self.progress_label = ttk.Label(self,textvariable=self.my_scale_float)
        self.my_scale = ttk.Scale(self, command=lambda val: print(self.my_scale_float.get()), from_=0,
                                  to=50, length=300, variable=self.my_scale_float)
        self.setup_ui()

    def setup_ui(self):
        self.title('Canvas')
        self.geometry('700x800')

        self.scale.pack()
        self.progress.pack()
        self.scrolled_text.pack()
        self.my_progress.pack()
        self.progress_label.pack()
        self.my_scale.pack()
        self.my_progress.start()


if __name__ == '__main__':
    win = MainWindow()
    win.mainloop()
