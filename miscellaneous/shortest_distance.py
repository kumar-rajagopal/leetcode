b = "the quick brown fox and test a string like quick jumps"
a = b.split(' ')

def short(a):
	i = 0
	j = i + 1

	s1 = 'fox'
	s2 = 'quick'
	res = [[0, len(a)]]

	while(i<j):		
		print(a[i], ' -- ', a[j])
		if (a[i] == s1 or a[i] == s2) and (a[j] == s1 or a[j] == s2):
			temp = res.pop()
			res.append([max(temp[0], i), min(temp[1], j)])
			i += 1
			j += 1
		elif a[i] == s1 and a[j] != s2:
			j -= 1
		elif a[i] != s1 and a[j] == s2:
			i += 1
		else:
			i +=1
			j -= 1
	return res
print(short(a))

