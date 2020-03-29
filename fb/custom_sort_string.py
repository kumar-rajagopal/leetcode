"""
791. Custom Sort String
Medium

384

128

Favorite

Share
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order 
that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
 

Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.

[Python] priority queue beats 99.93%

"""
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        dic = collections.defaultdict(int)
        for i, s in enumerate(S):
            dic[s] = i
        pq = []
        for t in T:
            if t in dic:
                pq.append((dic[t], t))
            else:
                pq.append((26, t))
        heapq.heapify(pq)
        res = ""
        while pq:
            i, c = heapq.heappop(pq)
            res += c
        return res


from collections import defaultdict
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        toNum = defaultdict(lambda: 26, {c:i for i,c in enumerate(S)})
        return "".join(sorted(T, key=lambda x: toNum[x]))
"""
This sends a key function to Python's sorted which will sort T based on the ordering in S constructed using a
defaultdict. Those characters in T that can't be found in S will have the default value of 26. 
Based on the constraints of the problem, the key 26 will never be set via the characters of S so those will be 
arranged as an innocuous postfix in the return value.

Indeed, since the number of unique characters in T is bounded by a small constant (26), one could use Counting 
Sort to solve the problem in O(n). However, my aim was simplicity and succinctness here.
"""