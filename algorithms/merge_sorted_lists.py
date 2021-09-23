def merge_lists(lst1, lst2):
    # Write your code here
    new_arr = []
    i = 0
    j_l = 0
    while i < len(lst1) - 1:
        if j_l > 2:
            break
        for j in lst2:
            if j < lst1[i]:
                new_arr.append(j)
                j_l += 1
                break
            else:
                new_arr.append(lst1[i])
                i += 1
    return new_arr

l1 = [1,3,5,7,9,11]
l2 = [4,6]

print(merge_lists(l1,l2))