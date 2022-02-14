def quickSort(list):
    length = len(list)
    if length <= 1:
        return list
    else:
        pivot = list.pop()
    itemsGreater = []
    itemsLower = []

    for item in list:
        if item > pivot:
            itemsGreater.append(item)
        else:
            itemsLower.append(item)
    return quickSort(itemsLower) + [pivot] + quickSort(itemsGreater)

print(quickSort([5, 2, 3, 5, 6, 3, 2, 34, 56,3 , 2, 3]))