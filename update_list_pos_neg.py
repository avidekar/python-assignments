# Given an array of positive and negative integers {-1,6,9,-4,-10,-9,8,8,4} (repetition allowed)
# sort the array in a way such that the starting from a positive number, the elements should be
# arranged as one positive and one negative element maintaining insertion order. First element
# should be starting from positive integer and the resultant array should look like
# {6,-1,9,-4,8,-10,8,-9,4}

def update_list(a):
    for i in range(0, len(a)):
        # print("Element ",a[i])
        if (i % 2 == 0):
            # print("Positive index",i)
            if (a[i] < 0):
                # print("Negative element .. Finding next positive...")
                find_next_positive_swap(i)
        elif (i % 2 == 1):
            # print("Negative index",i)
            if (a[i] > 0):
                # print("Positive element .. Finding next negative...")
                find_next_negative_swap(i)
    print(a)
    return

def find_next_negative_swap(i):
    for j in range(i, len(a)):
        if (a[j] < 0):
            ele = a[j]
            del a[j]
            a.insert(i, ele)
            # print(a)
            return
    return

def find_next_positive_swap(i):
    for j in range(i, len(a)):
        if (a[j] > 0):
            ele = a[j]
            del a[j]
            a.insert(i, ele)
            # print(a)
            return
    return

a=[-1, 6, 9, -4, -10, -9, 8, 8, 4]
print(a)
update_list(a)