class Solution:
    def productExceptSelf(self, nums):
        prod, prodR, result = 1, 1, []
        for n in nums:
            result.append(prod)
            prod *= n

        for i in range(len(nums)-1, -1, -1):
            print('res ',result[i])
            result[i] *= prodR
            prodR *= nums[i]
        return result
if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))
