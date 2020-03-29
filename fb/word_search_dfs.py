"""
79. Word Search
Medium

1725

84

Favorite

Share
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
 horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Complexity
Consider the worst situation, which is, every element in board is traversed and the for iteration is executed
completely. In this case, the time complexity is O(m^2 * n^2). And because we used a two-dimensional array markUsed, 
the space complexity is O(mn).

"""

def process(board, word):
	if not board:
		return False
	for i in range(0,len(board)):
		for j in range(0,len(board[0])):
			if dfs(board, i, j, word):
				return True
	return False

# check whether can find word, start at (i,j) position    
def dfs(board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    print("w: ",word[0])
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian 
    # check whether can find "word" along one direction
    res = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) \
    or dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED"
print(process(board, word))