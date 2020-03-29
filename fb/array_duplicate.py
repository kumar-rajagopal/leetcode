def removeDuplicates(nums):
    for i in range(len(nums)-1, 0, -1): #Read from reverse because pop is used to remove duplicates
        if nums[i] == nums[i-1]:
            #del nums[i]
            nums.pop(i)
    return len(nums)

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
