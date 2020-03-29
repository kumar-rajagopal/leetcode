class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __repr__(self):
    return "[({},{})]".format(self.start,self.end)

#[1,3],[2,6],[8,10],[15,18]
interval = [Interval(4,5), Interval(1,3), Interval(12,14), Interval(13,16),Interval(0,6), Interval(7,9)]

def merge_list(interval):

    interval.sort(key=lambda x: x.start)
    print("act data sorted: ",interval)
    #act data sorted:  [[(0,2)], [(1,3)], [(4,5)], [(7,9)], [(12,14)], [(13,16)]]
    
    result = [interval[0]]
    print("res ",result)
    for i in range(1, len(interval)):
        prev, current = result[-1], interval[i]
        print(prev ,' pc ',current, ' ',current.start, ' ', current.end)
        if current.start <= prev.end: 
            prev.end = max(prev.end, current.end)
        else:
            result.append(current)
    return result
print(merge_list(interval))


"""
def find_busy_intervals(v1):

  if v1 == None or len(v1) == 0 :
    return None

  v2 = []
  v2.append(pair(v1[0].first,v1[0].second))

  for i in xrange(1, len(v1)):
    x1 = v1[i].first
    y1 = v1[i].second
    x2 = v2[len(v2) - 1].first
    y2 = v2[len(v2) - 1].second

    if y2 >= x1:
      v2[len(v2)-1].second = max(y1, y2)
    else:
      v2.append(pair(x1,y1))

  return v2;

print(find_busy_intervals([(1, 5), (3, 7), (4, 6), (6, 8)]))
"""