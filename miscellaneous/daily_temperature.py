"""
Daily Temperatures
  Go to Discuss
Given a list of daily temperatures T, return a list such that, for each day in the input, 
tells you how many days you would have to wait until a warmer temperature. 
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. 
Each temperature will be an integer in the range [30, 100].
"""
def dailyTemperatures(T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    n = len(T)
    res, stack, = [0]*n, []
    for i, t in enumerate(T):
        print("entry stack ",i,t,stack)
        while stack and stack[-1][0] < t:
            prev_t = stack.pop()
            res[prev_t[1]] = i - prev_t[1]
            print('pop stack ',prev_t, res[prev_t[1]])      
        stack.append((t, i))
    return res

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

def temperature(T):
    res,stack = [0] * len(T), []
    for i,j in enumerate(T):
        while stack or stack[-1][0] < j:
            prev_t = stack.pop()
            res[prev_t[1]] = i - prev_t[1]
        stack.append((j,i)) 
    return res