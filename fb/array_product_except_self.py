"""
238. Product of Array Except Self
Medium

2185

180

Favorite

Share
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

"""
def productExceptSelf(A):
        """
        Time:  O(n)
        Space: O(n)
        """
        B = [1] * len(A)

        p = 1
        for i in range(len(A)):
            B[i] *= p
            p *= A[i]

        print(B)
        p = 1
        for i in reversed(range(len(A))):
            print("A[i] ",A[i])
            B[i] *= p
            p *= A[i]

        return B

print(productExceptSelf([1,2,3,4]))
