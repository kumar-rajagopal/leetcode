# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18]
class Interval(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def __repr__(self):
		return "[{}, {}]".format(self.start, self.end)

def merge(interval):
	interval.sort(key=lambda x: x.start)
	result = [interval[0]]
	for i in range(1, len(interval)):
		prev,current = result[-1],interval[i]
		if current.start<prev.end:
			prev.end = max(current.end,prev.end)
		else:
			result.append(interval[i])
	return result

interval = [Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]
print(merge(interval))