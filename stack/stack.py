class Stack:
    def __init__(self, size):
        self.size = size
        self._top = -1
        self._stack = [None] * size

    def isfull(self):
        if self._top == self.size - 1:
            return True
        return False

    def isempty(self):
        if self._top < 0:
            return True
        return False

    def push(self, data):
        if self.isfull():
            return False
        self._top += 1
        self._stack[self._top] = data
        return True

    def pop(self):
        if self.isempty():
            return False
        poped = self._stack[self._top]
        self._top -= 1
        return poped

    def popall(self):
        if self.isempty():
            return False
        all_stack = self._stack
        self._top = -1
        self._stack = [None] * self.size
        return all_stack

    def top(self):
        if self.isempty():
            return None
        return self._stack[self._top]
