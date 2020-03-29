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
from collections import deque
def subsets(nums):
	subset = []
	q = deque([([], 0)])
	while q:
		res, n = q.popleft()
		subset.append(res)
		for i in range(n,len(nums)):
			q.append((' '.join(res) + str(nums[i]), i+1))

	return subset

print(subsets([1,2,3]))