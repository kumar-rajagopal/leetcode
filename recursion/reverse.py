def reverse_s(s1):
	s = list(s1)
	i = 0
	j = len(s)-1
	while(i <= j):
		s[i],s[j] = s[j],s[i]
		i +=1
		j -= 1
	print(s)
reverse_s('hello')