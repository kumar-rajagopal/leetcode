s1 = 'foo'
s2 = 'bar'

s1 = 'app'
s2 = 'foo'

storage = {}
i = 0
j= 0
while i < len(s1) and j < len(s2):
	storage[s1[i]] = s2[j]
	i = i+1
	j= j+1
print (storage)