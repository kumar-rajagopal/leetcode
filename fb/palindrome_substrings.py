"""
647. Palindromic Substrings
Medium

1342

71

Favorite

Share
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they 
consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""

def countSubstrings(s):
        """
        :type s: str
        :rtype: int
        """
        print(s)
        leftrights = [(x,x) for x in list(range(len(s)))] + [(x,x+1) for x in list(range(len(s)-1))]
        print(leftrights)
        count = 0
        for left, right in leftrights:
            while left >= 0 and right < len(s) and s[left]==s[right]:
                count += 1
                left -= 1
                right += 1
        return count

print(countSubstrings('aaa'))
#O(n^2)


"""
Another soln
"""

def countSubstrings(self, s):
        n = len(s)

        def extend(i, j):
            count = 0
            while i >= 0 and j < n and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
            return count

        return sum(extend(i, i) + extend(i, i + 1) for i in range(n))

#The above may be O(n^2) or O(n)

#or

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # better soln; reverse string and find lcs
        length = count = len(s)
        if not length:
            return count
        
        for i in range(length-1):
            # even length
            start, end = i, i+1
            while start > -1 and end < length and s[start] == s[end]:
                start -= 1
                end += 1
                count += 1
            
            # odd length
            start, end = i, i+2
            while start > -1 and end < length and s[start] == s[end]:
                start -= 1
                end += 1
                count += 1
            
        
        return count