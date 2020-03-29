"""
713. Subarray Product Less Than K
Medium

709

33

Favorite

Share
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""

def maxS(arr, k):
	p = 1
	res = []

	for i in arr:
		p *= i
		if p < k:
			res.append(p)
	return res
print(maxS([10, 5, 2, 6], 100))