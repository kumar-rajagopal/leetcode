class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import Counter
        c = Counter(nums)
        for key,val in c.items():
            if val != 2:
                continue
            if key * 2 < k:
                return True
        return False

s = Solution()
print(s.containsNearbyDuplicate([1,0,1,1], 1))