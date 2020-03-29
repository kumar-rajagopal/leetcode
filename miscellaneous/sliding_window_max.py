#Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
#Output: [3,3,5,5,6,7] 

a = [1,3,-1,-3,5,3,6,7]
k = 3
a = [1,-1]
k = 1
"""
def win_max(a, k, i=0, res=[]):
    if k == len(a)+1:
       return -1
    s = a[i:k]
    b = max(s)
    res.append(b)
    win_max(a[i+1:], k, res=res)
    return res

r = win_max(a,k)
print(r)
"""

def maxSlidingWindow(nums, k, i=0, res = []):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return nums
    if len(nums) + 1 == k:
        return []
    n = nums[i:k]
    if n:
        res.append(max(n))
        maxSlidingWindow(nums[i+1:], k, i)
    return res

print(maxSlidingWindow(a,k))