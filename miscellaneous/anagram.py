def is_anagram(a,b):
	s1 = 0
	s2 = 0
	for i in range(0,len(a)):
		s1 += ord(a[i]) - ord('a')
	for j in range(0,len(b)):
		s2 += ord(b[j]) - ord('a')
	anagram = False
	if s1 ==  s2:
		anagram = True

	return anagram

print(is_anagram('aple','pleap'))