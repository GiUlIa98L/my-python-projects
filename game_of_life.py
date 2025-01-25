import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
#import matplotlib
#print(matplotlib.get_backend())

#setting up the states 
ALIVE = 255
DEAD = 0
states = [ALIVE, DEAD]

#return a random initial cells states configuration in a grid with dimension (N,N)
def first_generation(N):
    return np.random.choice(states, N*N, p=[0.2, 0.8]).reshape(N, N)

#copy the grid so we can calculate the new generation line by line
def update(frameNum, img, grid, N):

    new_gen = grid.copy()
    #compute the sum of all the alive neighbours
    for col in range(N):
        for row in range(N):
            total = int((grid[col , (row-1)%N] + grid[col , (row+1)%N] + grid[(col+1)%N, row] + grid[(col-1)%N, row] + 
                        grid[(col+1)%N, (row-1)%N] + grid[(col+1)%N, (row+1)%N] + grid[(col-1)%N, (row-1)%N] + grid[(col-1)%N, (row-1)%N])/255)
            if grid[col, row] == ALIVE:
                if (total < 2) or (total > 3):
                    new_gen[col, row] = DEAD
            else: 
                if total == 3: 
                    new_gen[col, row] = ALIVE
    # update data 
    img.set_data(new_gen) 
    grid[:] = new_gen[:] 
    return img, 

# main() function 
def main(): 
        
    # set grid size 
    N = 100
    # set animation update interval milliseconds
    updateInterval = 100
    # declare grid 
    grid = np.array([]) 
    grid = first_generation(N) 
    # set up animation 
    fig, ax = plt.subplots() 
    img = ax.imshow(grid, interpolation='nearest') 
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ), 
                                  frames = 1000, 
                                  interval=updateInterval) 
    plt.show() 
    plt.close('all')
  
# call main 
if __name__ == '__main__': 
    main() 
#next feature input the starting state and store different starting states