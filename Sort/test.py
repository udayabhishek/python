# def test(arr):
#     for n in range(len(arr)-1, 0, -1):
#         for i in range(0, n):
#             if arr[i] > arr[i+1]:
#                 temp = arr[i+1]
#                 arr[i+1] = arr[i]
#                 arr[i] = temp
#         # arr[n] = arr[i+1]
#
# arr = [2, 5, 4, 6, 7, 3, 1, 4, 12, 11]
# test(arr)
# print(arr)
#
# def selection_sort(arr):
#     for n in range(len(arr)-1, 0, -1):
#         position = 0
#         for j in range(1, n+1):
#             if arr[j] > arr[position]:
#                 position = j
#         temp = arr[n]
#         arr[n] = arr[position]
#         arr[position] = temp
#
# arr1 = [9,8,7,6]
# selection_sort(arr1)
# print(arr1)

"""Sum using recursion function"""
def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:len(arr)])


arr = [2, 5, 6, 1, 6, 2, 9]
print(sum(arr))

""" Find max using recursion"""

def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        sub_max = max(arr[1:])
        return arr[0] if arr[0] > sub_max else sub_max

print(f"MAX: {max(arr)}")
