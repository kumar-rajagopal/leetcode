def canAttendMeetings(intervals):
    if len(intervals) == 0:
        return True
    print(intervals)
    intervals.sort(key=lambda intervals: intervals[0])
    print(intervals)
    result = [intervals[0]]
    for i in range(1,len(intervals)):
        prev = result[-1]

        #PRE  [6, 15] [6, 17]
        #PRE  [6, 17] [13, 20]
        #PRE  [2, 4] [7, 10]
        current = intervals[i]
        print('PRE ',prev, current)
        if current[0] < prev[1]:
            return False
        prev[0],prev[1] = min(prev[0],current[0]), max(prev[1],current[1])
        result.append(prev)
    return True

print(canAttendMeetings([[7,10],[2,4]]))