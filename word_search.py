# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent"
# cells are those horizontally or vertically neighboring. The same letter cell may not be
# used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
def search_word(board, word):
    row_len = len(board)
    col_len = len(board[0])

    for i in range(row_len):
        for j in range(col_len):
            if board[i][j] == word[0]:
                result = search_for_further_letters(board, row_len, col_len,
                                                    i, j, word[1:])
                if result:
                    return True
    return False

def search_for_further_letters(board, row_len, col_len, i, j, target):
    temp = board[i][j]
    if len(target) == 0:
        return True
    board[i][j] = '#' #?
    for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
        if 0<=x<row_len and 0<=y<col_len and target[0] == board[x][y]:
            dec = search_for_further_letters(board, row_len, col_len,
                                             x, y, target[1:])
            if dec:
                return True
    board[i][j] = temp
    return False

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCB" # False
word = "ABCCED" # True

retFlag = search_word(board, word)
print(retFlag)