"""
16. 3Sum Closest
Medium


Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
def threeSumClosest(self, nums, target):
    nums.sort()
    res = sum(nums[:3])
    for i in xrange(len(nums)):
        l, r = i+1, len(nums)-1
        while l < r:
            s = sum((nums[i], nums[l], nums[r]))
            if abs(s-target) < abs(res-target):
                res = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else: # break early 
                return res
    return res

#The sort is O(nlogn) and the for loop is O(n^2). So it is O(n^2 + nlogn) = O(n^2) in total.