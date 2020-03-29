"""
67. Add Binary
Easy

931

186

Favorite

Share
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    last = 0
    out = ""
    while len(a) or len(b) or last:
        total = 0
        total += (int(a[-1]) if len(a) else 0)
        total += (int(b[-1]) if len(b) else 0)
        total += (last if last else 0)
        last, to_add = divmod(total, 2)
        out = out + str(to_add)
        a = a[:-1]
        b = b[:-1]
    return out[::-1]
