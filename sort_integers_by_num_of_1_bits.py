# Given an integer array arr. You have to sort the integers in the array in ascending order by the
# number of 1's in their binary representation and in case of two or more integers have the same
# number of 1's you have to sort them in ascending order.
# Return the sorted array.
# Input: arr = [0,1,2,3,4,5,6,7,8]
# Output: [0,1,2,4,8,3,5,6,7]
# Explantion: [0] is the only integer with 0 bits.
# [1,2,4,8] all have 1 bit.
# [3,5,6] have 2 bits.
# [7] has 3 bits.
# The sorted array by bits is [0,1,2,4,8,3,5,6,7]

def sort_by_bits(nums):

    nums.sort(key=count_bits)
    print(nums)

def count_bits(n):

    count = 0
    while n:
        count += n & 1
        n >>= 1

    return count


nums = [0,1,2,3,4,5,6,7,8]
sort_by_bits(nums)