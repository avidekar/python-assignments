# Your
# friend is typing
# his
# name
# into
# a
# keyboard.Sometimes, when
# typing
# a
# character
# c, the
# key
# might
# get
# long
# pressed, and the
# character
# will
# be
# typed
# 1 or more
# times.
#
# You
# examine
# the
# typed
# characters
# of
# the
# keyboard.Return
# True if it is possible
# that
# it
# was
# your
# friends
# name,
# with some characters (possibly none) being long pressed.
#
# Example
# 1:
#
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex'
# were
# long
# pressed.
# Example
# 2:
#
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e'
# must
# have
# been
# pressed
# twice, but
# it
# wasn
# 't in the typed output.
# Example
# 3:
#
# Input: name = "leelee", typed = "lleeelee"
# Output: true
# Example
# 4:
#
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It
# 's not necessary to long press any character.

def checkLongPressedName(name, typed):
    j = 0
    for c in name:
        if j == len(typed):
            return False

        # If mismatch...
        if typed[j] != c:
            # If it's the first char of the block, ans is False.
            if (j == 0) or (typed[j - 1] != typed[j]):
                return False

            # Discard all similar chars.
            cur = typed[j]
            while j < len(typed) and typed[j] == cur:
                j += 1

            # If next isn't a match, ans is False.
            if j == len(typed) or typed[j] != c:
                return False

        j += 1

    return True

a = "leelee"
b = "lleeelee"

retFlag = checkLongPressedName(a, b)
print(retFlag)