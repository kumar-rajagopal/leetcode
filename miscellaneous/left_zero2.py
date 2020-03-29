arr = [1,2,0,59,6,0,7,0,14,68,8]

def left_zero(arr):
	count = 0
	i = 0
	while (i <= len(arr)):
		print(i, arr[i])
		if arr[i] == 0:
			count = count + 1
			arr.pop(i)
		i = i + 1
	return (arr)

print(arr)
r = left_zero(arr)
print(r)