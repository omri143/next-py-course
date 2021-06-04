def intersection(list1, list2):
    return set(list1[list1.index(k)] for k in list2 if k in list1)


print(intersection([2, 3, 4, 7, 2], [2, 4, 5, 3]))
