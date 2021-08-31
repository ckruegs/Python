def mergeSort(input):
    size = len(input)
    if size > 1:
        middle = size // 2
        arrLeft = input[:middle]
        arrRight = input[middle:]

        mergeSort(arrLeft)
        mergeSort(arrRight)

        p = 0
        q = 0
        r = 0

        leftSize = len(arrLeft)
        rightSize = len(arrRight)
        while p < leftSize and q < rightSize:
            if arrLeft[p] < arrRight[q]:
                input[r] = arrLeft[p]
                p += 1
            else:
                input[r] = arrRight[q]
                q += 1

            r += 1

        
        while p < leftSize:
            input[r] = arrLeft[p]
            p += 1
            r += 1

        while q < rightSize:
            input[r]=arrRight[q]
            q += 1
            r += 1

input = [100, 45, 33, 55, 356, 11, 1000, 999, 987]
print(f"Input Array:{input}\n")
print(input)
mergeSort(input)
print(f"Sorted Array:{input}\n")
print(input)
