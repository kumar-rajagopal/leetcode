def zeros_to_right(nums):
	zeros = [i for i,v in enumerate(nums) if v == 0]
	for j in reversed(zeros):
		del nums[j]
	nums += [0]*len(zeros)
	return nums

res = zeros_to_right([0,1,0,3,12])
print(res)