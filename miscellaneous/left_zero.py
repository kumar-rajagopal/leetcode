"""
def left_zero(arr):
	read = len(arr) - 1
	write = len(arr) - 1
	while read >= 0:
		
		if arr[read] != 0:
			arr[write] = arr[read]
			#print(arr[read] , ' w ', arr[write])
			write = write - 1
		read -= 1
	while write >= 0:
		print(' in 2 loop ',arr[write])
		arr[write] = 0
		write = write -1
	return arr

arr = [1,2,0,59,6,0,7,0,14,68,8]
r = left_zero(arr)
print(r)
"""
arr = [1,2,0,59,6,0,7,0,14,68,8]
def lz(arr):
	zeros = [i for i,v in enumerate(arr) if v == 0]
	print(arr)
	print(zeros)
	for j in reversed(zeros):
		del arr[j]
	l = len(zeros)
	return [0] * l + arr

print(lz(arr))