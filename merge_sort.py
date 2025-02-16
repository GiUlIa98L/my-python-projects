# mergeSort function splits recursively the array till it remains only individual elements strarting from the leftmost side, than center, tham right
# merge function works is way upwords sorting from pairing individual elemnt to pairing left with center, and the sorted result with right.
import random

#list of ordered numbers from 1 to 100
ordered_dataset = list(range(1, 101))
shuffled_dataset = ordered_dataset.copy()
print("Ordered input sequence:")
print(ordered_dataset)
random.shuffle(shuffled_dataset)
print("Shuffled input sequence:")
print(shuffled_dataset)

def recursive_mergeSort(lst):
    # If there is only one element left, return it as a single-element list
    if len(lst) == 1:
        print(lst)
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left_result = recursive_mergeSort(left)
    right_result = recursive_mergeSort(right)

    # so
    merged = []
    k, j = 0, 0
    # if left and right lists have still elements for comparison
    while k < len(left_result) and j < len(right_result):
        # if left list element is bigger than right list element
        if left_result[k] > right_result[j]:
            #add right element to the list (from left)
            merged.append(right_result[j])
            #increase right list index by one
            j += 1
        else:
            # add left element to the list 
            merged.append(left_result[k])
            #increase left list index by one
            k += 1

    # Add remaining elements if any
    merged.extend(left_result[k:])
    merged.extend(right_result[j:])

    print("Merged List:", merged)
    return merged

# Example list with 11 elements
data = [1, 5, 7, 2, 10, 6, 11, 8, 9, 4, 3]
print("Recursion Example Results:")
recursive_mergeSort(shuffled_dataset)
