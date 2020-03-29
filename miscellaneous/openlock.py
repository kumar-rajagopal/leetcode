"""
Open the Lock
  Go to Discuss
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: 
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: 
for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the 
lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of 
turns required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:
Input: deadends = ["0000"], target = "8888"
Output: -1
Note:
The length of deadends will be in the range [1, 500].
target will not be in the list deadends.
Every string in deadends and the string target will be a string of 4 digits from the 10,000 possibilities 
'0000' to '9999'.
time complexity: O(N)
"""
#BFS - short path
class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        
        if target in deadends or '0000' in deadends:
            return -1
        
        if target == '0000':
            return 0
        
        min_step = 0
        deadends = set(deadends)
        deadends.add('0000')
        queue = collections.deque(['0000'])
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if cur == target:
                    return min_step
                trans = self.transform(cur)
                for tran in trans:
                    if tran not in deadends:
                        queue.append(tran)
                        deadends.add(tran)
            min_step += 1
        return -1
                
    def transform(self, target):
        transforms = []
        for i in range(len(target)):
            op1 = str((int(target[i])+1)%10) # 0 becomes 1, 9 becomes 0
            op2 = str((int(target[i])+9)%10) # 0 becomes 9, 9 becomes 8
            transforms.append(target[:i]+op1+target[i+1:])
            transforms.append(target[:i]+op2+target[i+1:])
        return transforms

#BFS - avoids TLE(time limit exceeded)
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # its important to add this line to avoid TLE error
        deadends = set(deadends)
        # Boundary Condition
        if target in deadends or '0000' in deadends:
            return -1
        # Create a dict to store the possible moves from any digit
        moves = {'0': ['1', '9'], '9': ['0', '8']}
        for i in range(1, 9):
            moves[str(i)] = [str(i-1), str(i+1)]
        # BFS
        queue = [('0000',0)]
        seen = set()
        while queue:
            curCode, numMoves = queue.pop(0)
            if curCode == target:
                return numMoves
            for i in range(4):
                for move in moves[curCode[i]]:
                    nextCode = curCode[:i] + move + curCode[i+1:]
                    if nextCode not in deadends and nextCode not in seen:
                        queue.append((nextCode, numMoves+1))
                        seen.add(nextCode)
        # If not possible, return -1
        return -1