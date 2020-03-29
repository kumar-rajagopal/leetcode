"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

"""
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if self.is_palindrome(s): return True
        left, right = 0, len(s)-1
        while left<right:
            if s[left] != s[right]:
                return self.is_palindrome(s[:left]+s[left+1:]) or self.is_palindrome(s[:right]+s[right+1:])
            left, right = left+1, right-1
        return False
        
    def is_palindrome(self, s):
        if s == s[::-1]: return True
        else: return False
#O(n) time complexity