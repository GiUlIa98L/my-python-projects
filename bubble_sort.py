# Bubble Sort algorithm, which sorts an array by repeatedly comparing adjacent elements and swapping them if they are in the wrong order.
#first shuffle an input sequence
import random

#list of ordered numbers from 1 to 100
ordered_dataset = list(range(1, 101))
shuffled_dataset = ordered_dataset.copy()
print("Ordered input sequence:")
print(ordered_dataset)
random.shuffle(shuffled_dataset)
print("Shuffled input sequence:")
print(shuffled_dataset)

#now use the shuffle algorithm:
temp_dataset = shuffled_dataset.copy()
n_correct = 0
while n_correct != len(temp_dataset)-1:
    #reset the variable that counts the positions already correct 
    n_correct = 0
    for i in range(0, len(temp_dataset)-1):
        #compare two consecutive numbers
        left_n = temp_dataset[i]
        right_n = temp_dataset[i+1]
        #if the number on the left is bigger than the one of the right change positions
        if left_n > right_n:
            temp_dataset[i] = right_n
            temp_dataset[i+1] = left_n
        else: 
            n_correct += 1

print("reordered dataset:")
print(temp_dataset)