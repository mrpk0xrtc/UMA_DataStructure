class Stack:
    def __init__(self, size):
        self.size = size
        self._top = 0
        self._stack = [None] * size

    def __str__(self):
        return str(self._stack)

    def __len__(self):
        return self.size

    def isfull(self):
        if self._top == self.size:
            return True
        return False

    def isempty(self):
        if self._top == 0:
            return True
        return False

    def push(self, data):
        if self.isfull():
            raise Exception("Stack is full")
        self._stack[self._top] = data
        self._top += 1
        return True

    def pop(self):
        if self.isempty():
            return None
        self._top -= 1
        poped = self._stack[self._top]
        self._stack[self._top] = None
        return poped

    def popall(self):
        res = []
        while self._top: res.append(self.pop())
        return res

    def top(self):
        return self._stack[self._top - 1]

if __name__ == "__main__":
    s = Stack(4)
    print(s, len(s))
    s.push(1)
    s.push(3)
    s.push(2)
    print(s, len(s), s.top())
    print(s.pop())
