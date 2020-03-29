def findAnagrams(s, p):
    j = 0
    st = 0
    end = len(p)
    res = []
    while st < len(s) and end < len(s):
        frag = s[st:end]
        print(frag, set(frag), set(p))
        if set(frag) == set(p):
        	res.append(st)
        st = end
        #j = end
        end = end + len(p)
    return res
print(findAnagrams("abab","ab"))


        