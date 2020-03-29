"""
49. Group Anagrams
Medium

1586

108

Favorite

Share
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

"""
def ana(ana_list, i=0, j=1, res=[]):
	if i >= len(ana_list):
		return
	res.append(ana_list[i])
	while i < len(ana_list)-1 and j < len(ana_list)-1 and sorted(ana_list[i]) not in res and sorted(ana_list[j]) not in res:
		#print(ana_list[i],  ana_list[j])
		#return
		if sorted(ana_list[i]) == sorted(ana_list[j]):			
			res.append(ana_list[j])
		j += 1
	i += 1
	#print(res, i, j)
	#return
	print(i,j)
	ana(ana_list, i, j, res)
	return res

print(ana(ana_list))
"""
from collections import Counter
#ana_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
ana_list = ["",""]
c = Counter([''.join(sorted(x)) for x in ana_list])
print("counter ",c)
res = []
seen = {}
for k,v in c.items():
	data = []
	for i,j in enumerate(ana_list):
		if sorted(j) == sorted(k) and seen.get(j) is None:
			data.append(j)
			seen[j] = 1
	res.append(data)
print(res)

"""
Python solution 1

Sort and group by group identifier, then sort each group normally.
"""
import itertools
def groupAnagrams1(strs):
    return [sorted(g) for _, g in itertools.groupby(sorted(strs, key=sorted), sorted)]
#Or "breaking it down" to maybe make it more readable for beginners and because I just noticed that in Firefox
# it violates my self-imposed "no scrollbars" rule (I usually use Chrome and didn't think it differed):


def groupAnagrams2(strs):
    groups = itertools.groupby(sorted(strs, key=sorted), sorted)
    #print('ga2 grps ',groups)
    #print("ga2 print")
    #print([' '+ str(_).join(members) for _, members in groups])
    #print('after')
    return [sorted(members) for _, members in groups]
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("GA2: ",groupAnagrams2(strs))
"""
Python solution 2

Using defaultdict to collect the groups.
"""
import collections
def groupAnagrams3(strs):
    groups = collections.defaultdict(list)
    print("g ",groups)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    print("k ", groups.keys(), ' v ',groups.values())
    return list(map(sorted, groups.values()))

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams3(strs))


