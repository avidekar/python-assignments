# Sometimes while working with Python lists we can have a problem in which we need to extract
# the frequency of elements in list. But this can be added work if we have more than 1 list we
# work on. Lets discuss certain ways in which this task can be performed.

test_list1 = [1, 3, 2, 4, 5, 1, 2]
test_list2 = [4, 1, 4, 3, 4, 2, 4]
test_list3 = [1, 4, 5, 3, 4, 5, 4]
result_dict = {}
for idx in set(test_list1 + test_list2 + test_list3):
    result_dict[idx] = [test_list1.count(idx), test_list2.count(idx), test_list3.count(idx)]

print(result_dict)