from circular_linkedlist import CircularLinkedList

if __name__ == "__main__":
	n = int(input().split()[0])
	k = int(input().split()[0])

	ls = CircularLinkedList()

	for i in range(1, n+1):
		ls.insert(i)

	current = ls.ptr
	after = ls.ptr

	while (current.next != current):
		count = 1
		while (count != k):
			after = current
			current = current.next
			count += 1

		after.next = current.next
		current = after.next

	print(current.cargo)
