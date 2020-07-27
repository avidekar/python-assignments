# Sometimes, while working with python lists we can have a problem in which we need to perform a merge operation on string of lists. This merge is consecutive to convert multiple spaces to one. Lets discuss certain way in which this can be performed.

test_list = ['Gfg', '', '', '', 'is', '', '', 'best', '']

count = 0
res = []
for ele in test_list:
    if ele == '':
        count += 1
        if count%2 == 0:
            res.append('')
            count = 0
    else:
        res.append(ele)

print(res)
