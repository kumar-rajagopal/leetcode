#foo != bar
#foo == app

def isomorphic(s1,s2):
	i = 0
	seen = {}
	for i in range(0,len(s1)):
		seen[s1[i]] = s2[i]
	print(seen)
	#while i < len(s1):
isomorphic('baa','aba')