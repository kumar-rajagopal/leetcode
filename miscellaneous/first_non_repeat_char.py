"""
"Salesforce is the best company to work for"
"""
from collections import Counter
def nonRepeat(s):
	s = s.lower()
	c = Counter(s)
	for i in s:
		if c[i] == 1:
			return i
	return None

print(nonRepeat("Salesforce is the best company to work for"))