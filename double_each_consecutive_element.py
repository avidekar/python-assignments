# Sometimes, while working with data, we can have a problem in which we need to perform double of
# element on each consecutive occurrence of a duplicate. This is very specific problem, but
# solution to this can prove to be very handy. Lets discuss certain ways in which this task
# can be performed.

test_list = [1, 2, 4, 2, 4, 1, 2]

temp = {}
result = []

for num in test_list:
    temp[num] = temp1 = temp.get(num,0) + num
    result.append(temp1)

print(result)