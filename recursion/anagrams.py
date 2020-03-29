def anagrams(s):
	if len(s) <= 1:
		return s
	else:
		tmp = []
		print('calling.... ',tmp)
		for i in anagrams(s[1:]):
			print('looping ',s[1:])
			for j in range(len(s)):
				print("str part upto j: ",i[:j], " first and sec ",s[0:1], " remain ",i[j:])
				tmp.append(i[:j] + s[0:1] + i[j:])
				print('tmp: ',tmp)
		return tmp
print(anagrams('abc')) #['abc', 'bac', 'bca', 'acb', 'cab', 'cba']

def all_perms(elements):
    if len(elements) <=1:
        return elements
    else:
        tmp = []
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])
        return tmp
print(all_perms('abc'))