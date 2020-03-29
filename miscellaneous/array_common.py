def arr_common(a, b, c):
	i = 0
	j = 0
	k = 0
	result = []

	while(i < len(a) and j < len(b) and k < len(c)):
		if a[i] == b[j] and a[i] == c[k]:
			result.append(a[i])
			i = i+1
			j = j+1
			k = k+1
		if a[i] <= b[j] and a[i] <= c[k]:
			i = i + 1
		elif b[j] <= a[i] and b[j] <= c[k]:
			j = j +1
		else:
		#elif c[k] <= a[i] and c[k] <= b[j]:
			k = k + 1

	return result

a = [6,7,10,25,30,63]
b = [-6,-3,-1,6,30,633]
c = [-1,6,30,34,100]
print(arr_common(a,b,c))