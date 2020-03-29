"""
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""
from collections import Counter
s = "leetcode"
s = "lovelveetczode"
c = Counter(s)
print(c)
def uniq(s , c):
	for i in range(len(s)):
		if c[s[i]] == 1:
			return i
	return -1
r = uniq(s, c)
print(r)
"""
d = {}
r = []
count = 0
for i,j in enumerate(s):
	if j not in d:
		d[j] = 1
	else:
		d[j] = d[j] + 1
		break
"""		
