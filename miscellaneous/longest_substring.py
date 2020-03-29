"""
3. Longest Substring Without Repeating Characters
Medium

6651

389

Favorite

Share
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


Please see and vote for my solutions for these similar problems.
1208. Get Equal Substrings Within Budget
3. Longest Substring Without Repeating Characters
159. Longest Substring with At Most Two Distinct Characters
340. Longest Substring with At Most K Distinct Characters
992. Subarrays with K Different Integers
424. Longest Repeating Character Replacement
209. Minimum Size Subarray Sum
713. Subarray Product Less Than K
76. Minimum Window Substring
"""

def lengthOfLongestSubstring(s):
    counter = dict()
    res = 0
    left = 0
    for right in range(len(s)):
        if s[right] not in counter:
            counter[s[right]] = 1
            res = max(res, right - left + 1)
        else:
            while s[left] != s[right]:
                counter.pop(s[left])
                left += 1
            left += 1
    return res


def lengthOfLongestSubstring1(s):
    last, res, st = {}, 0, 0
    for i, v in enumerate(s):
        if v not in last or last[v] < st:
            res = max(res, i - st + 1)
        else:
            st = last[v] + 1
        last[v] = i
    return res