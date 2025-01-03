import pygame
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
        self.rectangles = {}
        self.current_grid = np.zeros((self.rows, self.cols), dtype=int)
        #self.canvas.bind("<Motion>", self.on_hover)
        self.canvas.bind("<Button 1>", self.on_click)
        self.initialize_grid()
        self.game_running()

    def game_running(self):
        self.update_board()
        self.root.after(50, self.game_running)
        self.root.mainloop()

    def initialize_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * self.sand_pixel_size
                y1 = row * self.sand_pixel_size
                x2 = x1 + self.sand_pixel_size
                y2 = y1 + self.sand_pixel_size
                tag = f"cell-{row}-{col}"
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", width=2, tags=tag)
                self.rectangles[(row, col)] = rect

    def update_board(self):
        new_grid = np.copy(self.current_grid)
        for row in range(self.rows):
            for col in range(self.cols):
                if self.current_grid[row][col] == 1:
                    below = self.current_grid[row + 1][col]
                    left = self.current_grid[]


        self.current_grid = new_grid
        self.update_canvas()

    def update_canvas(self):
        for row in range(self.rows):
            for col in range(self.cols):
                color = "black" if self.current_grid[row][col] == 1 else "white"
                self.canvas.itemconfig(self.rectangles[(row, col)], fill=color)

    # def on_hover(self, event):
    #     col = event.x // self.sand_pixel_size
    #     row = event.y // self.sand_pixel_size
    #     if 0 <= row < self.rows and 0 <= col < self.cols:
    #         self.current_grid[row][col] = 1
    def on_click(self, event):
      col = event.x // self.sand_pixel_size
      row = event.y // self.sand_pixel_size
      if 0 <= row < self.rows and 0 <= col < self.cols:
          self.current_grid[row][col] = 1

SandDrop()
