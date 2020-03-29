def mergesort(alist):
	if len(alist) > 1:
		mid = len(alist)//2
		lhalf = alist[:mid]
		shalf = alist[mid:]

		mergesort(lhalf)
		mergesort(shalf)

		i,j,k = 0,0,0
		while i < len(lhalf) and j < len(shalf):
			if lhalf[i] < shalf[j]:
				alist[k] = lhalf[i]
				i += 1
			else:
				alist[k] = shalf[j]
				j += 1
			k += 1

		while i < len(lhalf):
			alist[k] = lhalf[i]
			i += 1
			k += 1
		while j < len(shalf):
			alist[k] = shalf[j]
			j += 1
			k += 1
	return alist
print (mergesort([54,26,93,17,77,31,44,55,20]))