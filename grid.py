import pygame, random
class Grid:
    #method that generate a grid and fills it with zeros
    def __init__(self, width, height, cell_size):
        #calculate rows and columns number
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        #generate a list of zeros long columns and repeat the process times rows
        self.cells = [[0 for _ in range(self.columns)]  for _ in range(self.rows)]
    #method that draws dead or alive cells
    def draw(self, window):
        for row in range(self.rows):
            for column in range(self.columns):
                color = (0, 255, 0) if self.cells[row][column] else (55, 55, 55)
                pygame.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, self.cell_size-1, self.cell_size-1))
    #random initial state
    def fill_random(self):
        for row in range(self.rows):
            for column in range(self.columns):
                #25% cells alive and 75% dead
                self.cells[row][column] = random.choice([1, 0, 0, 0])
    #clear grid
    def clear(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = 0
    # change the cell state from user input
    def toggle_cell(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.cells[row][column] = not self.cells[row][column]
