"""
139. Word Break
Medium

2152

119

Favorite

Share
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be 
segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

def word_break(s, wdict):
	print("start ",len(s))
	res = ''
	for i in wdict:
		res += s.replace(i,'')
		print("r ",res)
		if len(res) == len(s) or '':
			return True
	return False

s = "a"
wordDict = ["a"]

print(word_break(s,wordDict))

#Below wont work, used only to test subset
s = "leetcode"
wordDict = ["leet", "code"]
print(word_break(s,wordDict))

s = "applepenapple"
wordDict = ["apple", "pen"]
print(word_break(s,wordDict))

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(word_break(s,wordDict))
