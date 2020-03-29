"""
def bin_search(arr, num):
	""Find num and return index"
	low = 0
	high = len(arr) - 1
	while (high >= low):
		mid = low + (high - low) // 2
		if num == arr[mid]:
			return(mid)
		if num < arr[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return -1


arr = [1,45,67,345,566,789,5670,7000,10000]
print(bin_search(arr, 5670))
"""

def bin_search(arr, num):
	arr.sort()
	low = 0
	high = len(arr) -1
	while high >= low:
		mid = low + (high - low) // 2
		if arr[mid] == num:
			return (mid)
		if num < arr[mid]:
			high = high - 1
		else:
			low = mid + 1
	return -1
arr = [176,188,199,200,210,222,1,10,20,47,59,63,75,88,99,107,120,133,155,162]
print(bin_search(arr, 200))