import tkinter as tk
import ttkbootstrap as ttk


class MilesToKilometer:
    def __init__(self):
        self.window = ttk.Window(themename='darkly')
        self.entry_int = tk.IntVar()
        self.output_string = tk.StringVar()

    def create_ui(self):
        self.window.geometry("300x150")
        self.window.title('MtK App')
        tite_label = ttk.Label(master=self.window, text='Miles to kilometers', font=('Comic Sans MS', 22, 'bold'))

        tite_label.pack()
        input_frame= ttk.Frame(master=self.window)

        entry = ttk.Entry(master=input_frame, textvariable=self.entry_int)
        button = ttk.Button(master=input_frame, text= 'Convert', command=self.convert)
        entry.pack(side='left', padx=10)
        button.pack(side='left')
        input_frame.pack(pady=10)

        output_label = ttk.Label(master=self.window, text='output',
                                 font=('Comic Sans MS',18),
                                 textvariable=self.output_string)
        output_label.pack()

        self.window.mainloop()
        self.window.title("Demo")

    def convert(self):
        km_output = self.entry_int.get() * 1.61
        self.output_string.set(str(km_output))


if __name__ == "__main__":
    MilesToKilometer().create_ui()
