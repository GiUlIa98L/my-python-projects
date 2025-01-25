from grid import Grid
class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.temp_grid = Grid(width, height, cell_size)
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.grid.fill_random()
        #start and stop button
        self.run = False
       
    def draw(self, window):
        self.grid.draw(window)
    #method that counts how many neighbour are alive for each cell
    def count_live_neighbours(self, grid, row, column):
        live_neighbours = 0 
        #list of touples all cells around the central one
        neighbours_offset = [(-1,-1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
        for offset in neighbours_offset:
            new_row = (row + offset[0]) % self.rows
            new_column = (column + offset[1]) % self.columns
            if self.grid.cells[new_row][new_column] == 1:
                live_neighbours += 1
        return live_neighbours
    #check if the simulation is running
    def is_running(self):
        return self.run
    #start simulation
    def start(self):
        self.run = True
    #stop simulation
    def stop(self):
        self.run = False
    #clear the simulation if is not running
    def clear(self):
        if self.is_running() == False:
            self.grid.clear()
    def create_random(self):
        if self.is_running() == False:
            self.grid.fill_random()
    def toggle_cell(self, row, column):
        if self.is_running() == False:
            self.grid.toggle_cell(row, column)
    #update method following the game rules only if the simulation is running
    def update(self):
        if self.is_running():
            for column in range(self.columns):
                for row in range(self.rows):
                    live_neighbours = self.count_live_neighbours(self.grid, row, column)
                    cell_value = self.grid.cells[row][column]
                    if cell_value == 1: 
                        if (live_neighbours < 2) or (live_neighbours > 3):
                            self.temp_grid.cells[row][column] = 0
                    else:
                        if live_neighbours == 3: 
                            self.temp_grid.cells[row][column] = 1
            #update
            for column in range(self.columns):
                for row in range(self.rows):
                    self.grid.cells[row][column] = self.temp_grid.cells[row][column]
