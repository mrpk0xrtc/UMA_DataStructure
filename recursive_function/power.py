def pow(a, b):
	if b == 1:
		return a
	return pow(a, b-1) * a

if __name__ == "__main__":
	n1, n2 = int(input()), int(input())
	print(pow(n1, n2))

