def merge(a,b):
	i = 0;
	j = 0;
	z = []
	while i < len(a) and j < len(b):
		if a[i] <= b[j]:
			z.append(a[i])
			i += 1
		else:
			z.append(b[j])
			j += 1
	return z
a = [1,3,5,6,7,9]
b = [4,10]
print(merge(a,b))

