def num_of_islands(grid):
	if len(grid) == 0:
		return 0
	num_of_islands_count = 0
	for i in range(0,len(grid)):
		for j in range(0,len(grid[0])):
			if grid[i][j] == '1':
				num_of_islands_count += 1
				change_land_to_water(grid, i, j)
	return num_of_islands_count

def change_land_to_water(input, r, c):
	if (r < 0 or c < 0 or r >= len(input) or c >= len(input[0]) or input[r][c] == '0'):
	#if (r < 0 or c < 0 or r >=len(grid) or c >= len(grid[0]) or grid[r][c] == '0'):
		return
	input[r][c] = '0'
	change_land_to_water(input, r-1, c)
	change_land_to_water(input, r+1, c)
	change_land_to_water(input, r, c-1)
	change_land_to_water(input, r, c+1)

grid = [['1','1','0','0','0'],
['0','1','0','0','1'],
['1','0','0','1','1'],
['0','0','0','0','0'],
['1','0','1','0','1']]
print(num_of_islands(grid))