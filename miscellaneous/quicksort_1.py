def quickSort(alist, first, last):
	if first < last:
		partition = qs_helper(alist, first, last)
		quickSort(alist,first,partition-1)
		quickSort(alist,partition+1,last)

def qs_helper(alist, left, right):
	pv = alist[left]
	lm = left+1
	rm = right
	done = False
	while not done:
		while lm <= rm and alist[lm] <= pv:
			lm += 1
		while alist[rm] >= pv and rm >= lm:
			rm -=1
		if rm < lm:
			done = True
		else:
			temp = alist[lm]
			alist[lm] = alist[rm]
			alist[rm] = temp
	temp = alist[left]
	alist[left] = alist[rm]
	alist[rm] = temp

	return rm



alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist,0,len(alist)-1)
print(alist)