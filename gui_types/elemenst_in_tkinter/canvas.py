import tkinter as tk
from tkinter import ttk


class Canvas(tk.Tk):
    def __init__(self):
        super(Canvas, self).__init__()
        self.canvas = tk.Canvas(self, bg='white')
        self.mouse_button_pressed = False
        self.brush_size = 2
        self.setup_ui()

    def setup_ui(self):
        self.title('Canvas')
        self.geometry('700x500')

        self.canvas.bind("<ButtonPress-1>", self.set_mouse)
        self.canvas.bind("<ButtonRelease-1>", self.set_mouse)
        self.canvas.bind('<Motion>', self.draw_on_canvas)
        self.canvas.bind('<MouseWheel>', self.adjust_brush_size)
        self.canvas.pack()

    def set_mouse(self, event):
        self.mouse_button_pressed = not self.mouse_button_pressed

    def draw_on_canvas(self, event):
        if self.mouse_button_pressed:
            x = event.x
            y = event.y
            self.canvas.create_oval((x - self.brush_size/2, y - self.brush_size/2,
                                     x + self.brush_size/2, y + self.brush_size/2),
                                    fill='red')

    def adjust_brush_size(self, event):
        if event.delta > 0:
            self.brush_size += 2
        else:
            self.brush_size -= 2

        self.brush_size = max(0, min(self.brush_size, 50))


if __name__ == '__main__':
    can = Canvas()
    can.mainloop()
