"""
Evaluate Reverse Polish Notation
  Go to Discuss
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
def polish(arr):
	stack = []
	for i in range(len(arr)):
		if arr[i] == '+' or arr[i] == '-' or arr[i] == '*' or arr[i] == '/':
			op1 = stack.pop()
			op2 = stack.pop()
			stack.append(helper(arr[i], op1, op2))
		else:
			stack.append(int(arr[i]))
	return stack.pop()

def helper(op, op1,op2):
	if op == '+':
		return op1 + op2
	elif op == '-':
		return op2 - op1
	elif op == '*':
		return op1 * op2
	else:
		return int(float(op2/op1))

print(polish(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))


