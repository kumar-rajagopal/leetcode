"""
295. Find Median from Data Stream
Hard

1331

27

Favorite

Share
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""
class Median:
	def __init__(self):
		self.stack = [(float('inf'), None)] #to create a min stack

	def addNum(self, num):
		self.stack.append((min(self.stack[-1][0], num),num))

	def findMedian(self):
		l = len(self.stack)-1
		mid_idx = l // 2 + 1
		#print(l, ' midx ',mid_idx, self.stack)
		if l % 2 == 0: #even
			#print('stack ',self.stack, self.stack[mid_idx], ' m minus 1 ',self.stack[mid_idx-1])	
			middle = [self.stack[mid_idx][0], self.stack[mid_idx-1][0]]
			print('mid ',self.stack,  ' ', middle)
			return  sum(middle)// 2
		else:
			print('in else ',self.stack[mid_idx][1])
			return self.stack[mid_idx][1]
m = Median()
m.addNum(1)
m.addNum(2)
print (m.findMedian())
m.addNum(3)
print (m.findMedian())