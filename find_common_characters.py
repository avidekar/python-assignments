# Given an array A of strings made only from lowercase letters, return a list of all characters that
# show up in all strings within the list (including duplicates).  For example, if a character occurs
# 3 times in all strings but not 4 times, you need to include that character three times in
# the final answer.
# You may return the answer in any order.
# Example - Example 1:
#
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
#
# Input: ["cool","lock","cook"]
# Output: ["c","o"]


def find_common_characters(arr):
    result = []

    for char in arr[0]:
        count = arr[0].count(char)
        occurence = 1

        for str_val in range(1, len(arr)):
            if char in arr[str_val]:
                arr_count = arr[str_val].count(char)
                count = min(count, arr_count)
                occurence += 1
            else:
                break

        if occurence == len(arr):
            result.append(char)

    print(result)

arr = ["bella","label","roller"]
arr = ["cool","lock","cook"]
find_common_characters(arr)