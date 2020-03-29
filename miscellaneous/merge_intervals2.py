# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18]

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)
        

interval = [Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]
def merge_interval(interval):
    interval.sort(key=lambda x: x.start)
    result = [interval[0]]
    
    for i in range(1,len(interval)):
        prev, current = result[-1], interval[i]
        if current.start < prev.end:
            prev.end = max(prev.end, current.end)
        else:
            result.append(interval[i])
    return result


print(merge_interval(interval))


def merge(intervals):
    intervals = intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for i in range(1,len(intervals)):
        prev = result[-1]
        current = intervals[i]
        print("PC: ",prev,current) #PC:  [1, 3] [2, 6]
        if current[0] < prev[1]:
            prev[1] = max(current[1],prev[1])
        else:
            #print(result)
            result.append(intervals[i])
    return result
print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))