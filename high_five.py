# Given a list of scores of different students, return the average score of each student's top five
# scores in the order of each student's id.
#
# Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.
# The average score is calculated using integer division.

# Example - Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation:
# The average of the student with id = 1 is 87.
# The average of the student with id = 2 is 88.6. But with integer division their average
# converts to 88.

def get_avg_of_top_five_scores(arr):
    result = {}
    for item in arr:
        if item[0] in result:
            result[item[0]].append(item[1])
        else:
            result[item[0]] = [item[1]]

    def sort_avg(list):
        list = sorted(list, reverse=True)
        return int(sum(list[0:5])/5)

    final = []
    for item in result:
        final.append([item, sort_avg(result[item])])

    print(final)

arr = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
get_avg_of_top_five_scores(arr)
