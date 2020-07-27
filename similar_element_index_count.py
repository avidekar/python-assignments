# Sometimes, while working with Python list, we can have a problem in which we need to check if one element has similar index occurrence in other list. This can have possible application in many domains. Lets discuss certain ways in which this task can be performed.

test_list1 = [1, 3, 5, 6, 8]
test_list2 = [4, 3, 6, 6, 10]

res = sum(x == y for x,y in zip(test_list1, test_list2))
print(res)