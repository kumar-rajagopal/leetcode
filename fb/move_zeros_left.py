"""
283. Move Zeroes
Easy

2040

74

Favorite

Share
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

def move_zeroes(nums):
	zeroes = [i for i,v in enumerate(nums) if v == 0]
	#print(zeroes)
	for k in reversed(zeroes):
		print(k, nums[k])
		del nums[k]
	nums += [0] * len(zeroes)
	return nums

print(move_zeroes([0,1,0,3,12]))