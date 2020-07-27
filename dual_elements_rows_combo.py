# coding=utf-8
# Sometimes, while working with data, we can have a problem in which we need to find
# combinations in list. This can be a simple. But sometimes, we need to perform a variation of
# it and have a dual element row instead of a single element. Let’s discuss certain ways in
# which this task can be performed.

test_list = [[3, 4], [5, 6], [7, 8]]

res = [test_list[index - len(test_list)] + test_list[index + 1 - len(test_list)]
       for index, inner_list in enumerate(test_list)]

print(res)