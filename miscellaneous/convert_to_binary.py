from pythonds.basic import Stack
def rem_stack(num):
	r_stack = Stack()
	while num > 0:
		rem = num % 2
		r_stack.push(rem)
		num = num // 2
		print(rem)

	bin_str = ''
	while not r_stack.isEmpty():
		bin_str += str(r_stack.pop())
	return bin_str

print(rem_stack(17))