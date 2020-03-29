a = [6,7,10,25,30,45,63]
b = [-6,-3,6,45,633]
c = [-1,6,30,34,36,37,39,45,45]

def arr_common(a,b,c):
	result = []
	i,j,k = 0,0,0

	while(i < len(a) and j < len(b) and k < len(c)):
		if a[i] == b[j] and b[j] == c[k]:
			result.append(a[i])
			i = i + 1
			j = j + 1
			k = k + 1
		elif a[i] < b[j]:
			i = i + 1
		elif b[j] < c[k]:
			j = j + 1
		else:
			k = k + 1
	return result


print(arr_common(a,b,c))

or

list(set(a) & set(b) & set(c))