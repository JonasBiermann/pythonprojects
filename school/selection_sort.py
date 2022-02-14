from re import L


def selectionSort(list):
    indexing_length = range(0, len(list)-1)

    for i in indexing_length:
        minValue = i
        for j in range(i+1, len(list)):
            if list[j] < list[minValue]:
                minValue = j

        if minValue != i:
            list[minValue], list[i] = list[i], list[minValue]
    return list

print(selectionSort([1,2,5,2,1,3,5,6,3,12,3,4,21,3]))