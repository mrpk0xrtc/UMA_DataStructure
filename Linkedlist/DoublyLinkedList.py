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
        pass

    def RemoveNodeAtEnd(self):
        pass

    def RemoveNodeAtIndex(self, Index):
        pass

    def SizeOfList(self):
        pass

    def Concatenate(self, otherList):
        pass

    def Invert(self):
        pass
