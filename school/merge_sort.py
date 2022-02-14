def mergeSort(arr):
    if len(arr) > 1:
        leftArr = arr[:len(arr)//2]
        rightArr = arr[len(arr)//2:]

        #recursion
        mergeSort(leftArr)
        mergeSort(rightArr)

        #merge
        i = 0
        j = 0
        k = 0
        while i < len(leftArr) and j <  len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1
        
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1
    return arr
print(mergeSort([6, 3, 1, 4, 7, 9, 4, 2, 34, 7, 9, 5, 34, 6, 8, 4]))
