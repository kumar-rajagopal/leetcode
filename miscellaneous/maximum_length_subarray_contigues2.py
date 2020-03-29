"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one,
return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
"""

def max_sub(arr, k):
	cache = {0:0}
	total = 0
	remain = 0
	longest = 0
	for i in range(len(arr)):
		total += arr[i]
		remain = total - k
		if remain in cache:
			longest = max(longest, cache[remain] + 1)
			print("REM ",i,remain,cache, longest)
		if total not in cache:
			print('tot ',i,total)
			cache[total] = i + 1
	return longest
print(max_sub([1, -1, 5, -2, 3], 3))

def max_sub1(arr, k):
	remain = 0
	total = 0
	max_len = 0
	cache = {}
	for i in arr:
		total += i
		if total not in cache:
			cache[total] = i
		remain = total - k
		if remain == 0:
			max_len = max(max_len, i + 1)
		elif cache.get(remain):
			max_len = max(max_len, i - cache[remain])
	return max_len

print(max_sub1([1, -1, 5, -2, 3], 3))

