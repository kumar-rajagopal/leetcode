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
def maxSubArrayLen(nums, k):
    sum_table = {} # key: sum(nums[:i+1]), value: i
    total = 0
    max_len = 0
    for i in range(0, len(nums)):
        total += nums[i]
        if not sum_table.has_key(total):
            sum_table[total] = i
        remain = total - k
        if remain == 0:
            max_len = max(i+1, max_len)
        elif sum_table.has_key(remain):
            max_len = max(i - sum_table[remain], max_len)
    
    return max_len

# OR

def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cache = {0:0}
        total_sum = 0
        longest_length = 0
        for i in range(len(nums)):
            total_sum += nums[i]
            rem = total_sum - k
            if rem in cache:
                longest_length = max(longest_length, i - cache[rem] + 1)
            if total_sum not in cache:
                cache[total_sum] = i + 1
        return longest_length