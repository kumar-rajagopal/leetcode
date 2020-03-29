def high_low(arr, num):
	low = 0
	high = len(arr) - 1
	
	while low <= high:
		mid = low + (high - low)//2
		#print(num, low, high)

		if arr[mid] < num:
			low = mid + 1
		else:
			high = mid - 1
		if num == arr[low]:
			return (low, arr[low])
	return -1

def high_low_up(arr, num):
	low = 0
	high = len(arr) - 1
	
	
	while low <= high:
		mid = low + (high - low)//2

		if arr[mid] <= num:
			low = mid + 1
		else:
			high = mid - 1
		if num == arr[high]:
			return (high, arr[high])

	return -1
"""

def high_low_up(arr,key):
  low = 0
  high = len(arr) - 1
  mid = high//2

  while low <= high:
    #mid_elem = arr[mid]
    mid = low + (high-low)//2
    if arr[mid] <= key:
      low = mid+1
    else:
      high = mid-1
    if arr[high] == key:
       return high
  return -1
"""

arr = [1,2,5,5,5,5,5,5,58,10]
hl = high_low(arr, 5)
up = high_low_up(arr, 5)
print(hl)
print(up)

