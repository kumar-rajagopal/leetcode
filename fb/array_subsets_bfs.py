"""
78. Subsets
Medium

1845

49

Favorite

Share
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Running time

This algorithm runs in O(2^n) time, which is very slow, because there are 2n possible sets in a power set for an 
input set with n elements. The algorithm must perform this many steps to calculate all the sets. 
"""
def bfs(nums):
	res = []
	q = [([],0)]
	while q:
		arr,n = q.pop(0)
		res.append(arr)
		for i in range(n,len(nums)):
			print(i)
			q.append((' '.join(arr) + str(nums[i]),i + 1))
		print(q)
	return res

print(bfs([1,2,3]))
"""
0
[('1', 1)]
1
[('1', 1), ('2', 2)]
2
[('1', 1), ('2', 2), ('3', 3)]
1
[('2', 2), ('3', 3), ('12', 2)]
2
[('2', 2), ('3', 3), ('12', 2), ('13', 3)]
2
[('3', 3), ('12', 2), ('13', 3), ('23', 3)]
2
[('13', 3), ('23', 3), ('1 23', 3)]
[[], '1', '2', '3', '12', '13', '23', '1 23']

"""

"""
or use bit wise operation - https://coderbyte.com/algorithm/print-all-subsets-given-set
"""
