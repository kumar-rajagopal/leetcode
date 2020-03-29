"""
def f(n):
	if n <= 0:
		return n
	return n + int(f(n/2))
print(f(4))
"""
def f(func, item):
	i =0
	for i in range(len(item)):
		if func(item):
			print('here')
			item[i] = item
	del item[i]
f(True,[1,2,3])