"""
844. Backspace String Compare
Easy

720

47

Favorite

Share
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

from collections import Counter
def backspaceCompare(S,T):
    """
    if S == '' and T == '':
        return True
    if len(S) == 0 or len(T) == 0:
        return False

    s_max = -1
    if S.find('#') >= 0:
        s_max = max([i for i,v in enumerate(S) if v == '#'])
    t_max = -1
    if T.find('#') >= 0:
        t_max = max([i for i,v in enumerate(T) if v == '#'])
    print('here')
    return S[s_max:] == T[t_max:]
    """
    def compare(s):
        stack = []
        for i in s:
            if i != '#':
                stack.append(i)
            else:
                stack.pop()
        return stack
    return compare(S) == compare(T)


print(backspaceCompare("a#c","b"))
print(backspaceCompare("ab#c","ad#c"))
print(backspaceCompare("xywrrmp","xywrrmu#p"))
print(backspaceCompare("bxj##tw","bxo#j##tw"))