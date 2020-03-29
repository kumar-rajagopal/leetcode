grid = [['1','1','0','0','0'],
['0','1','0','0','1'],
['1','0','0','1','1'],
['0','0','0','0','0'],
['1','0','1','0','1']]

grid1 = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]

def numOfIslands(grid):
    if len(grid) < 1:
        return 0
    islandCount = 0
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            #print(grid[i][j])
            if grid[i][j] == '1':
                islandCount += 1
                #print(islandCount)
                changeLandToWater(grid, i, j)
    return islandCount

def changeLandToWater(grid, r, c):
    #check if row nmber exceeds grid row length
    #check if column nuumber exceeds grid col length
    #r or row number could be negative becuase of looking down or left via recursion, so check for negative
    #c or col num can be negative because of looking down or left via recursion, so check for negative
    if (r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == '0'):
        return
    grid[r][c] = '0'
    changeLandToWater(grid, r-1, c) #down
    changeLandToWater(grid, r+1, c) #up
    changeLandToWater(grid, r, c-1) #left
    changeLandToWater(grid, r, c+1) #right

    #return grid

print(numOfIslands(grid))

row = len(grid)
col = len(grid[0])
def dfs(grid, row, col, i, j):
    if len(grid) == 0:
        return 0
    if grid[i][j] == '0':
        return
    islandCount = 0


