"""
621. Task Scheduler
Medium

1598

271

Favorite

Share
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters 
represent different tasks. Tasks could be done without original order. Each task could be done in one interval. 
For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n 
intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

"""
"""
Here is what I learn from @awice and solution approach 3.

There are two cases: #[0]
if n is small enough for all tasks to run without idle the answer would be len(tasks)
if n is not small enough
it would be like the Figure 2 in https://leetcode.com/problems/task-scheduler/Figures/621_Task_Scheduler_new.PNG
the answer of the case2 is the number of total number of square in the Figure 2

in Figure 2, we can see
n (cooling interval) is 4
max_count is 4, max_count is the max number of each task that is going to be executed
t is 2, t is the number of task with max_count, which is 'A' and 'B', they both have to be executed 4 times

t is the left over of the last row in Figure 2 #[1]
max_count-1 is the height of the Figure 2 except last row #[2]
n+1 is the width of the Figure
so in case2 the answer is (max_count-1)*(n+1)+t

in case2 there would be no way that t is 0
if t is zero, that means the last row don't have idle
if the last row don't have idle, there would be no idle for all the rows
in that case, it is case1

the answer is not possible to be smaller then len(tasks)
if your case2 answer is smaller than len(tasks), it is wrong
the situation would be case1
that is why we take the max out of two cases #[3]
"""
class Solution(object):
    def leastInterval(self, tasks, n):
        task_count = list(collections.Counter(tasks).values())
        max_count = max(task_count) #[2]
        t = task_count.count(max_count) #[1]
        return max(len(tasks), (max_count-1)*(n+1)+t) #[3]


def _leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        n += 1
        ans = 0
        d = collections.Counter(tasks)
        heap = [-c for c in d.values()]
        heapq.heapify(heap)
        while heap:
            stack = []
            cnt = 0
            for _ in range(n):
                if heap:
                    c = heapq.heappop(heap)
                    cnt += 1
                    if c < -1:
                        stack.append(c + 1)
            for item in stack:
                heapq.heappush(heap, item)
            ans += heap and n or cnt # == if heap then n else cnt
        return ans
        
    
    # O(n) # of the most frequent tasks, say longest, will determine the legnth
    # to void counting idle intervals, we count (longest - 1) * (n + 1)
    # then count how many will in the last cycle which means finding ties
    # if counted number is less than # of tasks which means 
    # less frequent tasks can be always placed in such cycle
    # and it won't cause any conflicts with requirement since even most frequent can be settle
    # finally, return max(# of task, total counted number)
    
    def leastInterval(self, tasks, n):
        d = collections.Counter(tasks)
        counts = d.values()
        longest = max(counts)
        ans = (longest - 1) * (n + 1)
        for count in counts:
            ans += count == longest and 1 or 0
        return max(len(tasks), ans)
#Time complexity - O(nlogn)