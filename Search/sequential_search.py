
"""In Unordered List"""
def unordered_seq_search(arr, element):
    """General squential search, works on unordered list"""
    # starting position
    pos = 0
    # target become false if element found in the list
    found = False

    while pos < len(arr) and not found:
        # if element found in the list
        if arr[pos] == element:
            found = True
        else:
            pos += 1
    return found


"""In Ordered List"""

def ordered_seq_search(arr, element):
    """General squential search, works on unordered list"""
    # starting position
    pos = 0
    # target become false if element found in the list
    found = False
    # Stop marker
    stopeed = False

    while pos < len(arr) and not found and not stopeed:
        # if element found in the list
        if arr[pos] == element:
            found = True
        else:
            # when list element is greater than the element to be found
            if arr[pos] > element:
                stopeed = True
            else:
                pos += 1
    return found

arr_unord = [1,3,4,2,5,6,7,45,3,45,9,0]
print(unordered_seq_search(arr_unord, 123))

arr_ord = [0,12,23,34,45,56,67,78,89,90]
print(ordered_seq_search(arr_ord, 12))