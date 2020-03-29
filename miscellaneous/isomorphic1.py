#foo != bar
#foo == app

def iso(s1,s2):
	s1 = s1.lower()
	s2 = s2.lower()
	if len(s1) != len(s2):
		return False

	#result = [(s1[0],s2[0])]
	result = {s1[0]:s2[0]}
	i = 1
	j = 1
	while i < len(s1) and i < len(s2):
		if result.get(s1[i]):
			val = result.get(s1[i])
			if val and val == s2[i]:
				result[s1[i]] = s2[i]
			elif val and val != s2[i]:
				return False
		result[s1[i]] = s2[i]
		i += 1
	return True

print(iso('foo','bar'))

