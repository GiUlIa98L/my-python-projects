import pygame, sys
from grid import Grid
from simulation import Simulation
# Initialize pygame
pygame.init()
#window size
WINDOW_HEIGHT = 750
WINDOW_WIDTH = 750
#cell size
CELL_SIZE = 25
#window background color
GREY = (29,29,29)
#frames per second
FPS = 12

# Set up the display (width x height)
window = pygame.display.set_mode(( WINDOW_WIDTH, WINDOW_HEIGHT))
#set time of the simulation
clock = pygame.time.Clock()
#initialise the simulation object:
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

#simulation loop for updating the grid and the window
#runs till we close the simulations
while True:
    #1. event handling
    for event in pygame.event.get():
        # quit the game and the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #button pressing event to select cells
        if event.type == pygame.MOUSEBUTTONDOWN:
            #get the mouse coordinates
            pos = pygame.mouse.get_pos()
            row = pos[1] // CELL_SIZE
            column = pos[0] // CELL_SIZE
            simulation.toggle_cell(row, column)
        #if player press a key
        if event.type == pygame.KEYDOWN:
            #if press enter key start simulation
            if event.key == pygame.K_RETURN:
                simulation.start()
                # Set a title for the window
                pygame.display.set_caption("Game of Life is running")
            #else press space key stop simulation
            elif event.key == pygame.K_SPACE:
                simulation.stop()
                pygame.display.set_caption("Game of Life has paused")
            #change simulation speed: f speed up and s slow down by 2 FPS
            elif event.key == pygame.K_f:
                FPS += 2
            elif event.key == pygame.K_s:
                if FPS >= 5:
                    FPS -= 2
            #clear or create random grid 
            elif event.key == pygame.K_r:
                simulation.create_random()
            elif event.key == pygame.K_c:
                simulation.clear()
    #2. updating state
    simulation.update()
    #3. Drawing
    window.fill(GREY)
    #call the draw method
    simulation.draw(window)
    #update display 12 times per second at most
    pygame.display.update()
    clock.tick(FPS) 