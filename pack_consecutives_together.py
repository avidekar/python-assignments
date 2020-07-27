# Write a Python program to pack consecutive duplicates of a given list elements into sublists
# Example - [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After packing consecutive duplicates of the said list elements into sublists:
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
from itertools import groupby

def pack_duplicates(list):
    result = []
    # for num, group in groupby(list):
    #     result.append(list(group))
    #
    # print(result)

    start = 0
    temp_list = []
    while start < len(list):
        if (list[start] in temp_list) or (not temp_list):
            temp_list.append(list[start])
        elif list[start] not in temp_list:
            result.append(temp_list)
            temp_list = []
            temp_list.append(list[start])
        start += 1

    if temp_list:
        result.append(temp_list)

    print(result)

list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
pack_duplicates(list)