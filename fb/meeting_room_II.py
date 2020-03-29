import heapq
class Interval(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end
def minMeetingRooms(intervals):
    count = 0
    h = []
    intervals.sort(key = lambda x: x.start)
    for interval in intervals:
        if not h or interval.start < h[0]:
            count += 1
        else:
            heapq.heappop(h)
        heapq.heappush(h, interval.end)
    return count

interval = [Interval(0, 30),Interval(5, 10),Interval(15, 20)]
print(minMeetingRooms(interval))

#Heappush = O(log n), heappop = O(log n)