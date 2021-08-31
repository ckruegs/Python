import numpy as np

# random array of 1000 elements
array = np.random.randint(1, 1000, 1000)

print(array)
print("========================================================")

# divide the function
def partition(arr,low,high):
    i = ( low-1 )
    pivot = arr[high] # set pivot element
    for j in range(low , high):
        # if current element is smaller
        if arr[j] <= pivot:
            # increment through array
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
# sort
def quickSort(arr,low,high):
    if low < high:
        # index
        pi = partition(arr,low,high)
        # sort the partitions
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
# main
arr = array
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print (arr[i],end=" ")