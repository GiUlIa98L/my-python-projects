#algorithms that scramble a dataset 
import random
import numpy as np
#keeps reproducibility otherwise uses the random function by default
def myfunction():
  return 0.1
#list of ordered numbers from 1 to 100
ordered_dataset = list(range(1, 101))
random.shuffle(ordered_dataset, myfunction)
print(ordered_dataset) 
#or generate directly unique random numbers from 1 to 100
unique_random_array = np.random.choice(np.arange(1, 101), size=100, replace=False)
print(unique_random_array)