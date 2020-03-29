
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
from itertools import permutations
import collections
def sum3(nums):
	p = permutations(nums,3)
	seen = {}
	result_set = []
	for i in p:
		s = sorted(i)
		k = ''.join(map(str,s))
		if sum(i) == 0 and not seen.get(k):
				seen[k] = 1
				result_set.append(list(i))
	return result_set

#(o(n^2) solution)
def threeSum(nums):
        num = sorted(nums)
        i,result = 0, set()
        while i < len(num) - 2:
            j, k = i + 1, len(num) - 1
            while j < k:
                if num[i] + num[j] + num[k] == 0:
                    result.add((num[i], num[j],num[k]))
                    j += 1
                elif num[i] + num[j] + num[k] > 0:
                    k -= 1
                else:
                    j += 1
            i+=1
        
        return [list(t) for t in result]

print(sum3([-1, 0, 1, 2, -1, -4]))
print(threeSum([-1, 0, 1, 2, -1, -4]))

from itertools import permutations
from collections import defaultdict
def sum3p(nums):
	result_list = []
	seen = {}
	p = list(permutations(nums,3))
	for n in p:
		i = sorted(n)
		#s = ''.join(map(str,i))
		if not seen.get(tuple(i)) and sum(n) == 0:
			seen[tuple(i)] = 1
			result_list.append(list(n))
	return result_list

print(sum3p([-1, 0, 1, 2, -1, -4]))



"""
(-1, 0, 1)
(-1, 1, 0)
(-1, 2, -1)
(-1, -1, 2)
(0, -1, 1)
(0, 1, -1)
(1, -1, 0)
(1, 0, -1)
(2, -1, -1)

Actual answer
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""