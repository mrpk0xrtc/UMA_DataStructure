class SparseArray:
    def __init__(self):
        self.sparse = []

    def insert(self, object, Index):
        for i, item in enumerate(self.sparse):
            if item[0] == Index:
                self.sparse[i] = (Index, object)
                return

        self.sparse.append((Index, object))

    def delete(self, Index):
        new_list = []
        removed = None

        for i, item in enumerate(self.sparse):
            if item[0] == Index:
                removed = item[1]
            else:
                new_list.append(item)

        self.sparse = new_list
        return removed

    def find(self, object):
        for item in self.sparse:
            if item[1] == object:
                return item[0]
        return -1


if __name__ == "__main__":
    arr = SparseArray()

    arr.insert(12, 2)
    arr.insert(7, 5)
    arr.insert(20, 10)
    print(arr)

    arr.insert(99, 5)
    print(arr)

    deleted = arr.delete(2)
    print(deleted, arr)

    idx = arr.find(99)
    print(idx)

    idx = arr.find(123)
    print(idx)
