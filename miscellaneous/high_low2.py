#arr = [1,2,3,3,3,3,5,5,58,10]
arr = [0,0,0,1,1,1,1,1,1,1,1,1] 
def high_low(arr, goal):
	low = 0
	high = len(arr) - 1
	while(low <= high):
		mid = low + (high - low) // 2
		if arr[mid] < goal:
			low = mid + 1
		else:
			high = mid - 1

		if goal == arr[low]:
			return low
		#print(low, high)

	return -1

def high_low_up(arr, goal):
	low = 0
	high = len(arr) - 1
	while(low <= high):
		if goal == arr[high]:
			return high
		mid = low + (high - low) // 2		
		if arr[mid] < goal:
			low = mid + 1
		else:
			high = mid - 1


		#print(low, high)

	return -1

hl = high_low_up(arr, 1)
print (hl)


