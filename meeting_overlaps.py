# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...]
# (si < ei), determine if a person could attend all meetings.
#
# Example 1:
#
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
#
# Input: [[7,10],[2,4],[3,5]]
# Output: true


def checkMeetingOverlaps(timeSlots):
    timeSlots.sort()

    for index in range(len(timeSlots) - 1):
        if timeSlots[index][-1] > timeSlots[index + 1][0]:
            return False

    return True

timeSlots = [[7,10],[3,5],[2,4]]
retFlag = checkMeetingOverlaps(timeSlots)
print(retFlag)