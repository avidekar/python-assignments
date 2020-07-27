# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

def group_anagrams(strs):
    result = []
    grouped_dict = {}
    for word in strs:
        sorted_word = "".join(sorted(word))

        if sorted_word not in grouped_dict:
            grouped_dict[sorted_word] = [word]
        else:
            grouped_dict[sorted_word].append(word)

    for key in grouped_dict:
        result.append(grouped_dict[key])

    print(result)

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
group_anagrams(strs)