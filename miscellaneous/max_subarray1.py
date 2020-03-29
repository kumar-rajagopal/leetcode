def maxSubArray(nums):
    sum_n = 0
    max_n = min(nums)
    for i in nums:
    	if sum_n < 0:
    		sum_n = i
    	else:
    		sum_n += i
    	if max_n < sum_n:
    		max_n = sum_n
    return max_n
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
