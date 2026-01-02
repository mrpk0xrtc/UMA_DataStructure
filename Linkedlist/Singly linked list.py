class Node:
    def __init__(self, data=None):
        self.data = data
        self.link = None


class Linkedlist:
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        res = []
        p = self.first
        while p:
            res.append(str(p.data))
            p = p.link
        return " -> ".join(res)

    def IsEmpty(self):
        return self.first is None

    def InsertAtBegin(self, item):
        newNode = Node(item)
        newNode.link = self.first
        self.first = newNode
        if self.last is None:
            self.last = newNode

    def InsertAtEnd(self, item):
        newNode = Node(item)

        if self.IsEmpty():
            self.first = newNode
            self.last = newNode
            return
        self.last.link = newNode
        self.last = newNode

    def InsertAtIndex(self, item, Index):
        if Index == 0:
            self.InsertAtBegin(item)
            return
        p = self.first
        count = 0
        while p is not None and count < Index - 1:
            p = p.link
            count += 1

        if p is None:
            return False

        newNode = Node(item)
        newNode.link = p.link
        p.link = newNode

        if newNode.link is None:
            self.last = newNode

    def UpdateNode(self, item, Index):
        p = self.first
        count = 0
        while p is not None and count < Index:
            p = p.link
            count += 1
        if p is None:
            return False
        p.data = item
        return True

    def RemoveNodeAtBegin(self):
        if self.IsEmpty():
            return False

        deleted = self.first.data
        self.first = self.first.link
        if self.first is None:
            self.last = None
        return deleted

    def RemoveNodeAtEnd(self):
        if self.IsEmpty():
            return False
        elif self.first.link is None:
            deleted = self.first.data
            self.first = None
            self.last = None
            return deleted
        p = self.first
        while p.link is not self.last:
            p = p.link

        deleted = self.last.data
        p.link = None
        self.last = p
        return deleted

    def RemoveNodeAtIndex(self, Index):
        if self.IsEmpty():
            return False

        if Index == 0:
            return self.RemoveNodeAtBegin()

        p = self.first
        count = 0
        while p is not None and count < Index - 1:
            p = p.link
            count += 1

        if p is None:
            return False

        deleted = p.link.data
        p.link = p.link.link

        if p.link is None:
            self.last = p

        return deleted

    def SizeOfList(self):
        p = self.first
        count = 0
        while p is not None:
            count += 1
            p = p.link

        return count

    def Concatenate(self, otherList):
        if self.IsEmpty():
            self.first = otherList.first
            self.last = otherList.last
            return

        elif otherList.IsEmpty():
            return

        self.last.link = otherList.first
        self.last = otherList.last

    def Invert(self):
        prev = None
        current = self.first
        self.last = self.first

        while current is not None:
            nextNode = current.link
            current.link = prev
            prev = current
            current = nextNode

        self.first = prev


if __name__ == "__main__":
    n1 = Linkedlist()
    n2 = Linkedlist()

    n2.InsertAtEnd(11)
    n2.InsertAtEnd(12)

    n1.InsertAtEnd(1)
    n1.InsertAtEnd(3)
    n1.InsertAtEnd(2)
    n1.InsertAtEnd(4)

    print(n1, "Size:", n1.SizeOfList())

    n1.InsertAtIndex(5, 4)
    print("After InsertAtIndex(5,4):", n1, "Size:", n1.SizeOfList())

    n1.InsertAtBegin(9)
    print("After InsertAtBegin(9):", n1)

    n1.UpdateNode(10, 3)
    print("After UpdateNode(10,3):", n1)

    n1.RemoveNodeAtEnd()
    print("After RemoveNodeAtEnd:", n1, "Size:", n1.SizeOfList())

    n1.RemoveNodeAtBegin()
    print("After RemoveNodeAtBegin:", n1, "Size:", n1.SizeOfList())

    n1.RemoveNodeAtIndex(0)
    print("After RemoveNodeAtIndex(0):", n1, "Size:", n1.SizeOfList())

    n1.Concatenate(n2)
    print("List n2:", n2)
    print("List n1 after concatenation:", n1)

    n1.Invert()
    print("List n1 after invert:", n1)
