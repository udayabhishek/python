def selection_sort(a):
    for slot in range(len(arr)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, slot+1):
            if a[location] > arr[positionOfMax]:
                positionOfMax = location

        temp = a[slot]
        arr[slot] = arr[positionOfMax]
        arr[positionOfMax] = temp

    # return key

arr = [3,5,4,7,1]
print(selection_sort(arr))
print(arr)
