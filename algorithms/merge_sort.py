def split_array(array):
    mid = len(array) // 2
    return array[:mid], array[mid:]

def merge(left, right):
    i=j=0
    arr = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    while j < len(right):
        arr.append(right[j])
        j += 1
    while i < len(left):
        arr.append(left[i])
        i += 1
    return arr

def merge_sort(array):
    """Sort array using merge sort.
    Divide array
    sort children
    merge array
    Args:
        array (list): the array to be sorted
    """
    if len(array) <= 1:
        return array

    left, right = split_array(array)
    left_array = merge_sort(left)
    right_array = merge_sort(right)
    return merge(left_array, right_array)

arr = [1, 1000, 32, 689, 89, 909, 0,5,2,21,9,100,90]

m = merge_sort(arr)

print(m)
