n = [1,3,5,7]
def num_list(n):
        if len(n) == 1:
		return n[0]
	return n[0] + num_list(n[1:])
print(num_list(n))
