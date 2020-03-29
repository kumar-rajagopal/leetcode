class Interval:
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def __repr__(self):
		return "[{},{}]".format(self.start,self.end)


values = [Interval(4,5), Interval(20,30)]
#interval = [Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]

print(values[0][0])