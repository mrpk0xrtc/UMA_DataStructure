class Node:
	def __init__(self, cargo):
		self.cargo = cargo
		self.next = None

class CircularLinkedList:
	def __init__(self):
		self.ptr = None
	
	def __len__(self):
		size = 1 if self.ptr else 0
		current = self.ptr
		while current.next != self.ptr:
			size += 1
			current = current.next
		return size

	def __str__(self):
		res = []
		current = self.ptr
		while current.next != self.ptr:
			res.append(str(current.cargo))
			current = current.next
		res.append(str(current.cargo))
		res.append(str(self.ptr.cargo))
		return ' -> '.join(res)
	
	def __add__(self, other):
		if type(other) != type(self):
			node = Node(other)
			other = LinkedList()
			other.insert(node)
		return self.concatenate(other)
	
	def reach_index(self, index):
		current = self.ptr
		index %= len(self)

		if index == -1:
			while current.next != self.ptr:
				current = current.next
		else:
			for i in range(index):
				current = current.next

		return current

	def insert(self, cargo):
		node = Node(cargo)

		if not self.ptr:
			node.next = node
			self.ptr = node
			return

		current = self.reach_index(-1)
		node.next = self.ptr
		current.next = node

	def insert_at(self, index, cargo):
		node = Node(cargo)
		current = self.ptr

		if index % len(self) == 1 or index == 0:
			self.insert_at_start(cargo)
			return
		elif index < 0:
			raise IndexError("Out of range")

		current = self.reach_index(index-1)
		node.next = current.next
		current.next = node

		if node.next == self.ptr: self.tail = node

	def insert_at_start(self, cargo):
		node = Node(cargo)
		tail = self.reach_index(-1)

		node.next = self.ptr
		self.ptr = node
		tail.next = node
	
	def update_node(self, index, cargo):
		current = self.reach_index(index)
		current.cargo = cargo
	
	def remove(self):
		current = self.reach_index(len(self)-2)
		current.next = self.ptr
	
	def remove_at_start(self):
		tail = self.reach_index(-1)
		current = self.ptr.next
		tail.next = current
		self.ptr = current
	
	def remove_at(self, index):
		if index % len(self) == 0:
			self.remove_at_start()
			return

		current = self.reach_index(index-1)
		current.next = current.next.next
	
	def concatenate(self, other):
		current = self.reach_index(-1)
		otherptr = other.reach_index(-1)

		current.next = other.ptr
		otherptr.next = self.ptr
		return self
	
	def reverse(self):
		current = self.ptr
		after = current.next
		head = self.ptr
		tail = self.reach_index(-1)

		current.next = tail

		while after.next != head:
			tmp = after.next
			after.next = current
			current = after
			after = tmp

		after.next = current
		self.ptr = after

if __name__ == "__main__":
	n1 = CircularLinkedList()
	n2 = CircularLinkedList()
	n2.insert(20)
	n2.insert(22)
	n2.insert(21)
	n1.insert(1)
	n1.insert(3)
	n1.insert(2)
	n1.insert(4)
	n1.insert_at_start(90)
	n1.insert_at(0, 12)
	n1.insert_at(2, 11)
	n1.insert_at(6, 13)
	n1.insert_at(10, 19)
	n1.update_node(8, 15)
	print(n1, len(n1))
	print(n2, len(n2))
	n1 += n2
	print(n1, len(n1))
	n1.remove()
	print(n1, len(n1))
	n1.remove_at_start()
	print(n1, len(n1))
	n1.remove_at(3)
	print(n1, len(n1))
	n1.remove_at(9)
	print(n1, len(n1))
	n1.reverse()
	print(n1, len(n1))
