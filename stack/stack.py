class Stack:
	def __init__(self, size):
		self._stack = [None] * size
		self.size = size
		self._top = 0

	def push(self, data): pass
	def pop(self): pass
	def popall(self): pass

	def top(self):
        return self._stack[self._top - 1]

	def isfull(self):pass
	def isempty(self): pass
