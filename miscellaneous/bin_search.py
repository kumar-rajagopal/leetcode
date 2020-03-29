arr = [1,10,20,47,59,63,75,88,99,103]
def bs(arr, target):
	low = 0
	high = len(arr) -1
	count = 0
	while low <= high:
		count = count + 1
		mid = low + (high - low)//2
		if arr[mid] == target:
			return(mid)
		if target < arr[mid]:
			#discard all array elements greater than mid as target is present some where below
			high = mid - 1
		else:
			low = mid + 1
	return -1 

ans = bs(arr, 103) 
print(ans)
