class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        print('here')
        for n in range(0,len(nums)):
            print(nums[n], target)
            if nums[n] == target:
                return n
        return -1

s = Solution()
s.search([5], 5)
