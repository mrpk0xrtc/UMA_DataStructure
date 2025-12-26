def comb(n, k):
	if k > n: raise ValueError("k must be less than or equal to n")
	if k == 0 or n == k: return 1
	return comb(n-1, k-1) + comb(n-1, k)

if __name__ == "__main__":
	n, k = int(input()), int(input())
	print(comb(n, k))

