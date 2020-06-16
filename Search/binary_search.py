"""Iterative binary search"""
# def binary_search(arr, element):
#     found = False
#     first = 0
#     last = len(arr)-1
#     while first <= last and not found:
#         mid = int((first + last)/2)
#         print(mid)
#         if arr[mid] == element:
#             found = True
#         else:
#             if element < arr[mid]:
#                 last = mid-1
#             else:
#                 first = mid+1
#     return found
#
# arr = [0,12,23,34,45,56,67,78,89,90]
# print(binary_search(arr, 99))

"""Recursive binary search"""
def recursive_binary_search(arr, element):
    # Base Case!
    if len(arr) == 0:
        return False
    # Recursive Case
    else:
        mid = int(len(arr)/2)
        # If match found
        if arr[mid] == element:
            return True
        else:
            # Call again on second half
            if element < arr[mid]:
                return recursive_binary_search(arr[:mid], element)
            # Or call on first half
            else:
                return recursive_binary_search(arr[mid+1:], element)

arr = [0,12,23,34,45,56,67,78,89,90]
print(recursive_binary_search(arr, 99))
