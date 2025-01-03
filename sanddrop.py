import pygame
import numpy as np

class SandDrop:
    def __init__(self):
        pygame.init()
        self.sand_pixel_size = 10
        self.width, self.height = 600, 600
        self.rows = self.height // self.sand_pixel_size
        self.cols = self.width // self.sand_pixel_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("SandDrop")
        self.clock = pygame.time.Clock()
        self.current_grid = np.zeros((self.rows, self.cols), dtype=int)
        self.running = True


    def run(self):
        while self.running:
            self.handle_events()
            self.update_board()
            self.draw_board()
            pygame.display.flip()
            self.clock.tick(60)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                col = x // self.sand_pixel_size
                row = y // self.sand_pixel_size
                if 0 <= row < self.rows and 0 <= col < self.cols:
                    self.current_grid[row][col] = 1

    def update_board(self):
        below_right = False
        below_left = False
        new_grid = np.copy(self.current_grid)
        for row in range(self.rows):
            for col in range(self.cols):

                if self.current_grid[row][col] == 1:

                    if row < self.rows - 1 and self.current_grid[row + 1][col] == 0:
                        new_grid[row + 1][col] = 1
                        new_grid[row][col] = 0
                    else:

                        below_left = col > 0 and row < self.rows - 1 and self.current_grid[row + 1][col - 1] == 0
                        below_right = col < self.cols - 1 and row < self.rows - 1 and self.current_grid[row + 1][col + 1] == 0

                        if below_left and below_right:
                            # Randomly decide which way to move
                            if np.random.choice([True, False]):
                                new_grid[row + 1][col - 1] = 1
                            else:
                                new_grid[row + 1][col + 1] = 1
                            new_grid[row][col] = 0
                        elif below_left:
                            new_grid[row + 1][col - 1] = 1
                            new_grid[row][col] = 0
                        elif below_right:
                            new_grid[row + 1][col + 1] = 1
                            new_grid[row][col] = 0

        self.current_grid = new_grid


    def draw_board(self):
        self.screen.fill((0, 0, 0))
        for row in range(self.rows):
            for col in range(self.cols):
                color = (0, 0, 0) if self.current_grid[row][col] == 0 else (255, 255, 255)
                pygame.draw.rect(
                    self.screen,
                    color,
                    pygame.Rect(
                        col * self.sand_pixel_size,
                        row * self.sand_pixel_size,
                        self.sand_pixel_size,
                        self.sand_pixel_size,
                        ),
                )


game = SandDrop()
game.run()
