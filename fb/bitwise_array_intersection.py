#Intersection of Two Arrays II
#Using bitwise - is the efficient way to process data if memory is low or less disk space.
#Think of using bitwise if not able to use the entire data because of less disk space/memory

import collections
def array_intersect(nums1,nums2):
	c = collections.Counter
	return list((c(nums1) & c(nums2)).elements()) #elements will return the keys of the hash map of counter

print(array_intersect([1,2,2,1],[2,2]))