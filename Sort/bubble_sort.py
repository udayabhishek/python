def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        print(f"i -> {i}")
        for j in range(i):
            print(f"j -> {j}")
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

arr = [9,8,7,6,5,4,3,2,1]
bubble_sort(arr)
print(arr)





