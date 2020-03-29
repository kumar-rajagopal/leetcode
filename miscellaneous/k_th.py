from collections import Counter
s = "aaabbfghcvbuaaannmjgbbnesbbbmaaai"
s = "ababbc"
k = 2
c = Counter(s)

res = []
"""
def long(s, k):
    for ch in set(s):
        if c[ch] == k:
            print('chk: ',ch, ' -- ',k)
            sp = s.split(ch)
            print("sp: ",sp)

print("AS: ",s)
long(s,k)
"""       

def long(s,k):
    print("STRING ",s)
    if len(s) < k:
        return 0
    
    (count, rarest) = min((count, ch) for ch, count in Counter(s).items())
    print("RAR: ",count, ' -- ',rarest)
    if count >= k:
        print('in cnt eq')
        return len(s)
    else:
        print('in else')
        return max(long(ss, k) for ss in s.split(rarest))

r = long(s,k)
print(r)

