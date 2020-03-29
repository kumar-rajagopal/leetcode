
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    pre, ans = None, 0
    dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, None: 10000}
    for c in s:
        ans += dic[c] if dic[pre] >= dic[c] else dic[c] - dic[pre] * 2
        pre = c
    return ans

print(romanToInt('XIVMDI'))