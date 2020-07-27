def findTriplets(arr, final_sum):

    #found = False
    n = len(arr)
    result = []
    for i in range(n - 1):
        num_set = set()
        for j in range(i+1, n):
            x = final_sum - (arr[i] + arr[j])

            if x in num_set:
                result.append([arr[i] , arr[j], x])
            else:
                num_set.add(arr[j])

    print(result)

arr = [0, -1, 2, -3, 1]
final_sum = 0
findTriplets(arr, final_sum)