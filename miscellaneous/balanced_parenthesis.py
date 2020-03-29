def balanced(s):
	stack = []
	balanced = True
	i = 0
	while i < len(s) and balanced:
		if s[i] == '(':
			stack.append(s[i])
		else:
			if len(stack) == 0:
				balanced = False
			else:
				stack.pop()
		i += 1
	if len(stack) == 0 and balanced:
		return True
	return False
print(balanced('(()))'))