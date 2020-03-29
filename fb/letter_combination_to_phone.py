"""
17. Letter Combinations of a Phone Number
Medium

2200

297

Favorite

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could 
represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any 
letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


from itertools import permutations
def test(combo):
    d2a = { '1': '',    '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl', '6': 'mno',
        '7': 'pqrs','8': 'tuv', '9': 'wxyz',
        '0': ' '}
    ans = [''] if combo else [] #Initialize to aray of strings
    for c in combo: 
        #Produce all combinations of for example '22' - ['aa', 'ba', 'ca', 'ab', 'bb', 'cb', 'ac', 'bc', 'cc']
        ans = [r+e for e in d2a[c] for r in ans]
    return ans

print("TST ",test('22'))

"""
This will be depth first search algorithm and time and space complexity of O(^3n)
I believe space complexity since this is depth first search would be O(h) 
where h is the height of the tree in this case len(digits), this is because the recursion stack for the very first 
path down the tree would be going down the far left side. This is effectively the longest path we could take.

Time complexity would be the time to visit every node in the tree so It should be O(3^n) where n is the number of 
digits
"""

"""
Using iter tools
"""
import itertools
def letterCombinations(s):
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        letter_s = [d[c] for c in s]
        return [''.join(x) for x in itertools.product(*letter_s) if x]

print(letterCombinations('22'))