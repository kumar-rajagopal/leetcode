class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k-1]


from heapq import nlargest
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return nlargest(k,nums)[-1] #this is a min heap and so -1 will result in largest element 

#heap(q) - o(n*log(k)) where n is the number of list items and k is the number of largest item