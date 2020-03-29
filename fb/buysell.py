"""
121. Best Time to Buy and Sell Stock
Easy

2524

119

Favorite

Share
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
def buysell(nums):
	min_price,max_profit = nums[0],0
	for price in nums:
		min_price = min(min_price,price)
		profit = price - min_price
		max_profit = max(max_profit, profit)
	return max_profit

print(buysell([7,1,5,3,6,4]))

"""
1
min_price = min(7,7) =7
profit = 7 -7 =0
max_profit = max(0,0) = 0

2
min_price = min(7,1) = 1
profit = 1 - 1 = 0
max_profit = max(0,0) = 0

3
min_price = min(1,5) = 1
profit = 5 - 1 = 4
max_profit = max(0,4) = 4

4
min_price = min(1,3) = 1
profit = 3 - 1 = 2
max_profit = max(4,2) = 4

5
min_price = min(1,6) = 1
profit = 6 - 1 = 5
max_profit = max(4,5) = 5

6
min_price = min(1,4) = 1
profit = 4 -1 = 3
max_profit = max(5,3) = 5
