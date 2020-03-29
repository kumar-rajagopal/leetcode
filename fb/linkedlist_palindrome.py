"""
234. Palindrome Linked List
Easy

1573

233

Favorite

Share
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

def isPalindrome(self, head):
    vals = []
    while head:
        vals += head.val,
        head = head.next
    return vals == vals[::-1]