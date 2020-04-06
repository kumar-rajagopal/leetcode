"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

from collections import defaultdict, deque


def ladderLength(beginWord, endWord, wordList):
        d = defaultdict(list)  # build a graph like this {'h*t': ['hit', 'hot']}
        for word in wordList:
            for i in range(len(word)):
                d[word[:i] + '*' + word[i + 1:]].append(word)
        q, visited = deque([(beginWord, 1)]), set()
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            visited.add(word)
            for i in range(len(word)):
                for w in d[word[:i] + '*' + word[i + 1:]]:
                    if w not in visited:
                        q.append((w, length + 1))
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(beginWord, endWord, wordList))
