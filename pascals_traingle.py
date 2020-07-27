# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

def getPascalsTriangle(numRows):
    Tri = [[1]]
    for i in range(1, numRows):
        row = [1]
        for j in range(1, i):
            row.append(Tri[i-1][j-1] + Tri[i-1][j])
        row.append(1)
        Tri.append(row)
    return Tri

printRow = getPascalsTriangle(5)
print(printRow)