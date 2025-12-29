def tokenize(string):
	arr = string.split()
	for ptr in arr:
		index = arr.index(ptr)
		arr[index:index+1] = list(arr[index])
	return arr
