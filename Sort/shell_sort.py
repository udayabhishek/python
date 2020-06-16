def shell_sort(arr):
    print(print(f"sublistcount {len(arr)}"))
    sublistcount = int(len(arr)/2)

    while sublistcount > 0:
        for start in range(sublistcount):
            print("******Start*****")
            print(arr)
            print(start)
            print(sublistcount)
            gap_insertion_sort(arr, start, sublistcount)
            print("******End*****")

        print(f"sublistcount {sublistcount}")
        sublistcount = int(sublistcount/2)

def gap_insertion_sort(arr, start, gap):
    print(f"start {start}")
    print(f"gap {gap}")
    for i in range(start+gap, len(arr), gap):
        currentvalue = arr[i]
        position = i
        print(f"currentvalue {currentvalue}")
        print(f"position {position}")
        # print(f"{}")
        while position >= gap and arr[position-gap] > currentvalue:
            arr[position] = arr[position-gap]
            position = position-gap

        arr[position] = currentvalue

arr = [2, 5, 4, 6, 7, 3, 1, 4, 12, 11]
shell_sort(arr)
print(arr)
