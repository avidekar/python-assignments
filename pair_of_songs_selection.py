# In a list of songs, the i-th song has a duration of time[i] seconds.
#
# Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
# Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

# Example 1:
#
# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
import collections

def pair_songs(time):

    remain = collections.defaultdict(list)
    count = 0
    # [30,20,150,100,40]
    for t in time:
        key = t % 60
        com_key = (60-key) % 60
        if com_key in remain:
            count += len(remain[com_key])
        remain[key].append(t)
        print(remain)
        print("-------------------")
    print(count)

time = [30,20,150,100,40]
pair_songs(time)