import tkinter as tk
import numpy as np
class SandDrop:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SandDrop")
        self.sand_pixel_size = 10
        self.canvas = tk.Canvas(self.root, bg="black", height=400, width=400)
        self.canvas.pack()
        self.canvas.update()
        self.rows = self.canvas.winfo_height() // self.sand_pixel_size
        self.cols = self.canvas.winfo_width() // self.sand_pixel_size
        self.current_grid = np.zeros((self.rows, self.cols), dtype=int)
        self.game_running()


    def game_running(self):
        self.draw_board()
        self.update_board()
        self.root.after(100, self.game_running)
        self.root.mainloop()

    def draw_board(self):
        self.canvas.delete("all")
        for i in range(self.rows):
            for j in range(self.cols):
                x1 = i * self.sand_pixel_size
                y1 = j * self.sand_pixel_size
                x2 = x1 + self.sand_pixel_size
                y2 = y1 + self.sand_pixel_size
                if(self.current_grid[i][j] == 1):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", width=2)
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", width=2)

    def update_board(self):
        new_grid = np.copy(self.current_grid)
        for i in range(self.cols):
            for j in range(self.rows):
                if j < self.rows:
                        if(self.current_grid[i][j] == 1):
                            if j < self.rows - 1:
                                below = self.current_grid[i][j + 1]
                                if below == 0:
                                    new_grid[i][j + 1] = 1
                                    new_grid[i][j] = 0
        self.current_grid = new_grid
SandDrop()