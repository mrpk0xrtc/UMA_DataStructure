from tokenizer import tokenize
from stack import Stack
from string import ascii_letters, digits

operators = [['None', '('], ['+', '-'], ['*', '/', '%'], ['^']]

def is_prior(op1, op2, eq=False):
	o1, o2, j = 0, 0, 0
	for i in operators:
		o1 = j if op1 in i else o1
		o2 = j if op2 in i else o2
		j += 1
	if o1 > o2: return True
	elif eq and o1 == o2: return True
	else: return False

def to_postfix(tokens):
	stack = Stack(len(tokens))
	out = ''
	for token in tokens:
		if token in ascii_letters + digits: out += token
		elif token == '(': stack.push('(')
		elif token == ')':
			while True:
				tmp = stack.pop()
				if tmp == '(': break
				out += tmp
		else:
			if is_prior(token, stack.top()): stack.push(token)
			else:
				while True:
					tmp = stack.pop()
					if tmp == '(':
						stack.push(tmp)
						stack.push(token)
						break
					elif is_prior(token, tmp) or (token == tmp) and (token == '^'):
						if tmp: stack.push(tmp)
						stack.push(token)
						break
					else: out += tmp
	out += ''.join(stack.popall())
	return out

def to_prefix(tokens):
	stack = Stack(len(tokens))
	out = ''
	for token in tokens[::-1]:
		if token in ascii_letters + digits: out += token
		elif token == ')': stack.push(')')
		elif token == '(':
			while True:
				tmp = stack.pop()
				if tmp == ')': break
				out += tmp
		else:
			if is_prior(token, stack.top(), True): stack.push(token)
			else:
				while True:
					tmp = stack.pop()
					if tmp == ')':
						stack.push(tmp)
						break
					elif is_prior(token, tmp, True):
						if tmp: stack.push(tmp)
						stack.push(token)
						break
					else: out += tmp
	out += ''.join(stack.popall())
	return out[::-1]

if __name__ == "__main__":
	tokens = tokenize(input())
	print(to_postfix(tokens))
	print(to_prefix(tokens))
