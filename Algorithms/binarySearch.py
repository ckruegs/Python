import numpy as np

# random array of 1000 elements
array = np.random.randint(1, 1000, 1000)

print(array)
print("========================================================")

def binarySearch(array, low, high, x):
    #edge case
    if high >=low:
        mid = (high + low) // 2

        # if element is present in the middle
        if array[mid] == x:
            return mid

        # if element smaller than mid, must be in left subarray
        elif array[mid] > x:
            return binarySearch(array, low, mid -1, x)

        # else must be in right subarray
        else:
            return binarySearch(array, mid + 1, high, x)

    # if element is not in array
    else:
        return -1

x = 20

result = binarySearch(array, 0, len(array)-1, x)

if result != -1:
    print(f"Element present at {result}")
else:
    print(f"Element not present in array")
