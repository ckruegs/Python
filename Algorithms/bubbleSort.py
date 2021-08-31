unsorted = [100, 45, 33, 55, 356, 11, 1000, 999, 987]

def bubbleSort(unsorted):
    # Iterate through entire unsorted list
    for i in range(0, len(unsorted) -1):
        # Iterate through each item until the final item
        for j in range(len(unsorted) -1):
            # If current item is less than item to the right...
            if (unsorted[j] > unsorted[j+1]):
                # Swap current item with item to the right
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
    return unsorted


print(f"The unsorted list is: {unsorted}")

print(f"The sorted list is: {bubbleSort(unsorted)}")