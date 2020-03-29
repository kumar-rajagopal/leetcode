s = "abcabcbb"
def lengthOfLongestSubstring(s):
    dic, res, start, = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in dic:
            print('idx ',i ,' ', ch , ' -- start -- ',start , ' dic[ch]+1 - ',dic[ch]+1)
            start = max(start, dic[ch]+1)
            print('AFTER idx ',i ,' ', ch , ' -- start -- ',start , ' dic[ch]+1 - ',dic[ch]+1)
            res = max(res, i-start+1)
            print('i-start+1 = ',i-start+1,' res ', res)
        dic[ch] = i
    return res
r = lengthOfLongestSubstring(s)
print(r)


