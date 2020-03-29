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
	stack = []
	res = [0] * len(T) #In order to pre calculate temp diff 0, i.e no need to traverse if the temp diff does not exist
	for ind,val in enumerate(T):	
		while stack and stack[-1][0] < val:
			prev_temp = stack.pop()
			temp_diff = val - prev_temp[0]
			res[prev_temp[1]] = ind - prev_temp[1]
		stack.append([val, ind])
	return res

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))