class Queue:
    def __init__(self, Max_size):
        self.Max_size = Max_size
        self.queue = [None] * Max_size
        self.front = self.rear = -1

    def IsEmpty(self):
        return self.front == -1

    def IsFull(self):
        return self.front == (self.rear + 1) % self.Max_size

    def Enqueue(self, data):
        if self.IsFull():
            return False
        if self.IsEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.Max_size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.IsEmpty():
            return False
        deleted = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 2) % self.Max_size
        return deleted
