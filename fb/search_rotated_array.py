"""
33. Search in Rotated Sorted Array
Medium

2371

307

Favorite

Share
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

"""
Use modified binary search

One half will be sorted and the other will not be sorted.
Figure out which half is sorted. Figure out if the target lies in that region or not.
Use this information to determine the regions to eliminate.
"""
def binary(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1 #which is a bitwise operator equivalent to (left + right)//2
            if nums[mid] == target:
                return mid
            if target >= nums[0]:
                if nums[mid] < target and nums[mid] >= nums[0]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] < target or nums[mid] >= nums[0]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

nums = [4,5,6,7,0,1,2]
print(binary(nums, 0))

"""
this should be o(nlogn) time complexity
"""

"""
class Solution(object):
    def search(self, a, k):
        lo, hi = 0, len(a)-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if a[mid] == k:
                return mid
            elif a[mid] > k:
                if a[mid] >= a[lo]:  # left half is sorted
                    if k >= a[lo]:
                        hi = mid-1
                    else:
                        lo = mid+1
                else:  # right half is sorted
                    hi = mid-1
            else:
                if a[mid] <= a[hi]:  # right half is sorted
                    if k <= a[hi]:
                        lo = mid+1
                    else:
                        hi = mid-1
                else:  # left half is sorted
                    lo = mid+1
        return -1
"""