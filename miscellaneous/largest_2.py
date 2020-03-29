a = [1,7,5,2,67,8]
def largest_2(a):
	l = 0
	j = 0
	while j < 2:
		l = a[0]
		for i in range(1,len(a)):
			if a[i] > l:
				l = a[i]
		print(l)
		a.remove(l)
		print(a)
		j += 1
	print(l)
largest_2(a)

a = [3,6,12,7,10,15,8,11]
a.sort()
print(a)
def range_n(a):
	#st = [[a[0]]]
	res = []
	seen = {}
	for n in range(0,len(a)):
		temp = a[n]
		if temp not in seen:
			new_list = [a[n]]
			i = 1
			while i < len(a):
				if a[i] not in seen:
					if a[i] == temp - 1:
						new_list.append(a[i])
						temp = a[i]
					elif a[i] == temp + 1:
						seen[a[i]] = 1
						temp = a[i]
				i += 1
			res.append(new_list)
	return res

print(range_n(a))