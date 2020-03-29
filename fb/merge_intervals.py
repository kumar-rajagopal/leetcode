class Interval:
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def __repr__(self):
		return "[{}, {}]".format(self.start, self.end)

def merge_interval(intervals):
	intervals.sort(key=lambda x: x.start)
	print(intervals)
	#print('inter ',intervals[0].end)
	result = [intervals[0]] 
	for i in range(1,len(intervals)):
		prev, current = result[-1],intervals[i] #stack - read array as though you are tilting it vertically and 
												#then LIFO will be result[-1]
		if current.start < prev.end:
			prev.end = max(current.end, prev.end)
		else:
			result.append(intervals[i])
	return result

intervals = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
print(merge_interval(intervals))

"""
Complexity Analysis

Time complexity : O(n\log{}n)O(nlogn)

Other than the sort invocation, we do a simple linear scan of the list, so the runtime is dominated by the 
O(nlgn)O(nlgn) complexity of sorting.

Space complexity : O(1)O(1) (or O(n)O(n))

If we can sort intervals in place, we do not need more than constant additional space. Otherwise, 
we must allocate linear space to store a copy of intervals and sort that.

"""