def insertion_sort(a):
    for i in range(1, len(a)-1):
        for j in range(i+1, 0, -1):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp



arr = [3,5,4,7,1]
print(insertion_sort(arr))
print(arr)