# An element in a sorted array can be found in O(log n) time via binary search. But suppose we rotate an ascending order sorted array at some pivot unknown to you beforehand. So for instance, 1 2 3 4 5 might become 3 4 5 1 2. Devise a way to find an element in the rotated array in O(log n) time.
#
# sortedPivotedArray
#
# Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
#          key = 3
# Output : Found at index 8
#
# Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
#          key = 30
# Output : Not found
#
# Input : arr[] = {30, 40, 50, 10, 20}
#         key = 10
# Output : Found at index 3

def pivotedBinarySearch(nums, key):
    n = len(nums)
    pivot = getPivot(nums, 0, n - 1)
    if pivot == -1:
        return binarySearch(nums, 0, n - 1, key)
    if nums[pivot] == key:
        return pivot
    if nums[0] <= key:
        return binarySearch(nums, 0, pivot - 1, key)
    return binarySearch(nums, pivot + 1, n, key)

def getPivot(nums, start, end):
    if end < start: return -1
    if end == start: return start

    mid = int((start + end) / 2)
    if mid < end and nums[mid] > nums[mid + 1]:
        return mid
    if mid > start and nums[mid] < nums[mid - 1]:
        return (mid-1)
    if nums[start] >= nums[mid]:
        return getPivot(nums, start, mid-1)
    return getPivot(nums, mid + 1, end)

def binarySearch(nums, start, end, key):
    if end < start:
        return -1

    mid = int((start + end)/2)
    if key == nums[mid]:
        return mid
    if key > nums[mid]:
        return binarySearch(nums, mid + 1, end, key)
    return binarySearch(nums, start, mid - 1, key)


nums = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 9
retIndex = pivotedBinarySearch(nums, key)
print(retIndex)