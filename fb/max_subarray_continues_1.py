def max_sub(nums):
	max_n = min(nums)
	sum_n = 0
	for n in nums:
		if sum_n < 0:
			sum_n = n
		else:
			sum_n += n
		if sum_n > max_n:
			max_n = sum_n
	return max_n

print(max_sub([-2,1,-3,4,-1,2,1,-5,4]))
