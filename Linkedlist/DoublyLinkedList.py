class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        res = []
        p = self.first

        while p:
            res.append(str(p.data))
            p = p.next
        return " <-> ".join(res)

    def IsEmpty(self):
        return self.first is None

    def InsertAtBegin(self, item):
        newNode = Node(item)
        if self.IsEmpty():
            self.first = self.last = newNode
            return

        newNode.next = self.first
        self.first.prev = newNode
        self.first = newNode

    def InsertAtEnd(self, item):
        newNode = Node(item)
        if self.IsEmpty():
            self.first = self.last = newNode
            return

        self.last.next = newNode
        newNode.prev = self.last
        self.last = newNode

    def InsertAtIndex(self, item, Index):
        if Index == 0:
            self.InsertAtBegin(item)
            return
        p = self.first
        count = 0
        while p and count < Index - 1:
            p = p.next
            count += 1

        if not p:
            return False

        newNode = Node(item)
        newNode.next = p.next
        newNode.prev = p
        if p.next:
            p.next.prev = newNode
        else:
            self.last = newNode

        p.next = newNode

    def UpdateNode(self, item, Index):
        p = self.first
        count = 0
        while p and count < Index:
            p = p.next
            count += 1

        if p:
            p.data = item
        else:
            return False

    def RemoveNodeAtBegin(self):
        if self.IsEmpty():
            return False
        data = self.first.data
        if self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None
        return data

    def RemoveNodeAtEnd(self):
        prev = self.last.prev
        prev.next = None
        self.last = prev
        return self.last.data

    def RemoveNodeAtIndex(self, Index):
        if Index == 0:
            return self.RemoveNodeAtBegin()

        count = 0
        current = self.first

        while count < Index:
            current = current.next
            count += 1

        if not current:
            raise IndexError("Out of range")
        if not current.next:
            self.last = current.prev

        prev = current.prev
        prev.next = current.next
        current.next.prev = prev
        return current.data

    def __len__(self):
        current = self.first
        size = 0
        while current != None:
            size += 1
            current = current.next
        return size

    def __add__(self, other):
        if type(other) != type(self):
            node = Node(other)
            other = DoublyLinkedList()
            other.insert(node)
        return self.Concatenate(other)

    def Concatenate(self, other):
        self.last.next = other.first
        other.first.prev = self.last
        self.last = other.last
        return self

    def Invert(self):
        current = self.first
        tail = self.last
        self.first = tail
        self.last = current

        while current != tail:
            tmp = current.next

            n = None if not current.next else current.next.data
            p = None if not current.prev else current.prev.data

            current.next = current.prev
            current.prev = tmp

            current = tmp

        current.next = current.prev
        current.prev = None

if __name__ == "__main__":
    l = DoublyLinkedList()
    l2 = DoublyLinkedList()
    l.InsertAtBegin(1)
    l.InsertAtEnd(3)
    l.InsertAtEnd(2)
    l.InsertAtEnd(9)
    l.InsertAtEnd(5)
    l.UpdateNode(4, 1)
    l2.InsertAtBegin(10)
    l2.InsertAtEnd(12)
    l2.InsertAtEnd(11)
    print(l, len(l))
    print(l2, len(l2))
    l += l2
    print(l, len(l))
    l.RemoveNodeAtBegin()
    l.RemoveNodeAtEnd()
    print(l, len(l))
    l.RemoveNodeAtIndex(4)
    print(l, len(l))
    l.Invert()
    print(l, len(l))
