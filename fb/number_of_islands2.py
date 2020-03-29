"""
Implements DFS algorithm - This is a variation of undirected graph
The grid will be read as list of individual string and not as list of strings. Python strings are immutable.
"""

def num_of_islands(islands):
	if len(islands) == 0:
		return 0
	islandCount = 0
	for i in range(0,len(islands)):
		for j in range(0,len(islands[0])):
			if islands[i][j] == '1':
				islandCount += 1
				setLandToWater(islands, i, j)
	return islandCount

def setLandToWater(input, r, c):
	if (r < 0 or c < 0 or r >= len(input) or c >= len(input[0]) or input[r][c] == '0'):
		return
	input[r][c] = '0'
	setLandToWater(input, r-1, c) #left element of row
	setLandToWater(input, r+1, c) #right element of the row
	setLandToWater(input, r, c-1) #down column
	setLandToWater(input, r, c+1) #up column



input = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]
grid = [['1','1','0','0','0'],
['0','1','0','0','1'],
['1','0','0','1','1'],
['0','0','0','0','0'],
['1','0','1','0','1']]
print(num_of_islands(grid))

"""
Time complexity: O(ROW x COL) if DFS is used. If implemented with BFS then it is O(V+E) - vertices and edjes
"""