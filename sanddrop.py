import tkinter as tk
import numpy as np
class SandDrop:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SandDrop")
        self.sand_pixel_size = 10
        self.canvas = tk.Canvas(self.root, bg="black", height=400, width=400)
        self.canvas.pack()
        self.game_running()

    def game_running(self):
        self.root.update()
        cols = self.canvas.winfo_width() // self.sand_pixel_size
        rows = self.canvas.winfo_height() // self.sand_pixel_size

        current_grid = np.zeros((rows, cols), dtype=int)

        for i in range(rows):
            for j in range(cols):
                x1 = i * self.sand_pixel_size
                y1 = j * self.sand_pixel_size
                x2 = x1 + self.sand_pixel_size
                y2 = y1 + self.sand_pixel_size
                if(np.zeros[i][j] == 1):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", width=2)
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", width=2)
        self.root.mainloop()
SandDrop()