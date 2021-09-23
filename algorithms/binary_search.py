"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, right, left, value):
    """Your code goes here."""
    mid = (right + left) // 2
    current_value = input_array[mid]
    if mid == right and current_value != value:
        return -1
    if current_value == value:
        return mid
    if value < current_value:
        return binary_search(input_array, right=mid - 1, left=left, value=value)
    if value > current_value:
        return binary_search(input_array, right=right, left=mid + 1, value=value)
    return -1


def itr_bs(inp, val):
    right = len(inp) - 1
    left = 0
    while left <= right:
        mid = (right + left) // 2
        if val == inp[mid]:
            return mid
        if val < inp[mid]:
            right = mid - 1
        if val > inp[mid]:
            left = mid + 1
    return -1


test_list = [1, 3, 9, 11, 15, 19, 29, 100, 112, 134, 1000]
test_val1 = 15
test_val2 = 13
t = [3, 1, 29, 25, 33, 9, 19, 50, 112, 132, 1000]

for i in range(len(t)):
    print(f"Found: {t[i]}", binary_search(input_array=test_list, right=len(test_list) - 1, left=0, value=t[i]))
    print(f"ITR Found: {t[i]}", itr_bs(test_list, t[i]))
