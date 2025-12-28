class Queue:
    def __init__(self, Max_size):
        self.Max_size = Max_size
        self.queue = [None] * Max_size
        self.front = 0
        self.rear = -1

    def IsEmpty(self):
        return self.front > self.rear

    def IsFull(self):
        return self.rear == self.Max_size - 1

    def Enqueue(self, data):
        if self.IsFull():
            return False
        self.rear += 1
        self.queue[self.rear] = data
        return True

    def Dequeue(self):
        if self.IsEmpty():
            return None
        item = self.queue[self.front]
        self.front += 1
        return item

    def Peek(self):
        if self.IsEmpty():
            return None
        return self.queue[self.front]

    def ReverseQueue(self):
        if self.IsEmpty():
            return None

        i = self.front
        j = self.rear

        while i < j:
            self.queue[i], self.queue[j] = self.queue[j], self.queue[i]
            i += 1
            j -= 1

        return self.queue[self.front : self.rear + 1]
