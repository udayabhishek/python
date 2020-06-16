"""Grokking Algorithm"""

def quicksort(arr):
    if len(arr) == 0:
        return arr
    else:
        pivot = arr[0]
        print(f"pivot {pivot}")
        left = [i for i in arr[1:] if i <= pivot]
        print(f"left: {left}")
        right = [i for i in arr[1:] if i > pivot]
        print(f"right: {right}")
        return quicksort(left) + [pivot] + quicksort(right)

arr = [2, 5, 4, 6, 7, 3, 1, 4, 12, 11]
print(quicksort(arr))




"""UDEMY"""
def quick_sort(arr):
    quick_sort_help(arr, 0, len(arr)-1)


def quick_sort_help(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first, last)
        quick_sort_help(arr, first, splitpoint-1)
        quick_sort_help(arr, splitpoint+1, last)


def partition(arr, first, last):
    pivotvalue = arr[first]

    leftmark = first + 1
    rightmark = last

    done = False

    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark += 1

        while leftmark <= rightmark and arr[rightmark] >= pivotvalue:
            rightmark -= 1

        if leftmark > rightmark :
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark


arr = [2, 5, 4, 6, 7, 3, 1, 4, 12, 11]
quick_sort(arr)
print(arr)
