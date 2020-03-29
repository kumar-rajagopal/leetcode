"""
Perfect Squares
  Go to Discuss
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


Time complexity: O(n^(n+1)) because in the worst case we can search n + 1 level in depth
(worst case the perfect squares are made up all by 1s) from 0 and the tree can thus contains up to 
n^(n+1) nodes (n^0 + n^1 + n^2 + ... + n^(n-1) + n^n).

Space complexity: O(n^n) because of the queue used to store each level we are iterating through.

Uses BFS shortest path
"""

def numSquares(self, n):
    if n < 2:
        return n
    lst = []
    i = 1
    while i * i <= n:
        lst.append( i * i )
        i += 1
    cnt = 0
    toCheck = {n}
    while toCheck:
        cnt += 1
        temp = set()
        for x in toCheck:
            for y in lst:
                if x == y:
                    return cnt
                if x < y:
                    break
                temp.add(x-y)
        toCheck = temp

    return cnt