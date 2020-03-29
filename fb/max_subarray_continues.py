"""
53. Maximum Subarray
Easy

4334

145

Favorite

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, 
which is more subtle.
"""
def max_sub_array(nums):
	max_n = min(nums)
	sum_n = 0
	for i in nums:
		if sum_n < 0:
			sum_n = i
		else:
			sum_n += i
		if sum_n > max_n:
			max_n = sum_n
	return max_n

"""
i 	sum_n	max_n
-	0		-5
-2	-2		-2
1	1		1
-3	-2		1
4	4		4
-1	3		4
2	5		5
1	6		6
-5	-5		6
4	4		6
"""

print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))

"""
Using Divide and Conquer approach, we can find the maximum subarray sum in O(nLogn) time. Following is the Divide and 
Conquer algorithm.

"""

# A Divide and Conquer based program 
# for maximum subarray sum problem 
  
# Find the maximum possible sum in 
# arr[] auch that arr[m] is part of it 
def maxCrossingSum(arr, l, m, h) : 
      
    # Include elements on left of mid. 
    sm = 0; left_sum = -10000
      
    for i in range(m, l-1, -1) : 
        sm = sm + arr[i] 
          
        if (sm > left_sum) : 
            left_sum = sm 
      
      
    # Include elements on right of mid 
    sm = 0; right_sum = -1000
    for i in range(m + 1, h + 1) : 
        sm = sm + arr[i] 
          
        if (sm > right_sum) : 
            right_sum = sm 
      
  
    # Return sum of elements on left and right of mid 
    return left_sum + right_sum; 

  
# Returns sum of maxium sum subarray in aa[l..h] 
def maxSubArraySum(arr, l, h) : 
      
    # Base Case: Only one element 
    if (l == h) : 
        return arr[l] 
  
    # Find middle point 
    m = (l + h) // 2
  
    # Return maximum of following three possible cases 
    # a) Maximum subarray sum in left half 
    # b) Maximum subarray sum in right half 
    # c) Maximum subarray sum such that the  
    #     subarray crosses the midpoint  
    return max(maxSubArraySum(arr, l, m), 
               maxSubArraySum(arr, m+1, h), 
               maxCrossingSum(arr, l, m, h)) 
              
  
# Driver Code 
arr = [2, 3, 4, 5, 7] 
n = len(arr) 
  
max_sum = maxSubArraySum(arr, 0, n-1) 
print("Maximum contiguous sum is ", max_sum)