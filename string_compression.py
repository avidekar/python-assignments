# Given
# an
# array
# of
# characters, compress
# it in -place.
#
# The
# length
# after
# compression
# must
# always
# be
# smaller
# than or equal
# to
# the
# original
# array.
#
# Every
# element
# of
# the
# array
# should
# be
# a
# character(not int)
# of
# length
# 1.
#
# After
# you
# are
# done
# modifying
# the
# input
# array in -place,
# return the
# new
# length
# of
# the
# array.
#
# Follow
# up:
# Could
# you
# solve
# it
# using
# only
# O(1)
# extra
# space?
#
#
# Example
# 1:
#
# Input:
# ["a", "a", "b", "b", "c", "c", "c"]
#
# Output:
# Return
# 6, and the
# first
# 6
# characters
# of
# the
# input
# array
# should
# be: ["a", "2", "b", "2", "c", "3"]
#
# Explanation:
# "aa" is replaced
# by
# "a2".
# "bb" is replaced
# by
# "b2".
# "ccc" is replaced
# by
# "c3".

def getStrCompressed(chars):
    count = 1
    current_position = 0

    # if it's a single character, just return a
    # a basic array with count
    if len(chars) == 1:
        chars.append("1")
        return chars

    # loop till the 2nd last character is analyzed
    while current_position < len(chars) - 1:

        # assume that we haven't reached the 2nd last character
        # if next character is the same as the current one, delete
        # the current one and increase our count
        while current_position < len(chars) - 1 and \
                chars[current_position] == chars[current_position + 1]:
            del chars[current_position]
            count += 1

        # if next character isn't the same, time to add the count to
        # the list. Split the number into
        # character list (e.g. 12 will become ["1", "2"]
        # insert those numbers behind the character and increment position
        for x in str(count):
            chars.insert(current_position + 1, str(x))
            current_position += 1

        # great, on to the next character
        current_position += 1

        # if we are now at the last character, it's a lonely character
        # give it a counter of 1 and exit the looping
        if current_position == len(chars) - 1:
            chars.append("1")
            break

        count = 1

    return chars

str = ["a", "a", "b", "b", "c", "c", "c"]
retList = getStrCompressed(str)
print(retList)