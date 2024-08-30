import ArrayList
import DLList
from BinarySearchTree import BinarySearchTree
from Interfaces import Set


class BinarySearchTreeWithDuplication(Set):

    def __init__(self, nil=None):
        self.binaryTree = BinarySearchTree()
        self.n = 0
        
    def size(self) -> int:
        return self.n 

    def find(self, x: object) -> object:
        if self.binaryTree.find(x) is x:
            return self.binaryTree.find_eq(x).v
        return
        # pass

    def add(self, key : object, value : object) -> bool:
        if self.binaryTree.find(key) is None:
            dllist = DLList.DLList()
            dllist.append(value)
            self.binaryTree.add(key, dllist)
        else:
            self.binaryTree.find_eq(key).v.append(value)
        self.n += 1
        # pass
    
    def remove(self, x : object) -> bool:
        self.n -= self.binaryTree.find_eq(x).v.size()
        self.binaryTree.remove(x)

        # pass


# q = BinarySearchTreeWithDuplication()
# q.add(1, "a")
# q.add(1, "b")
# q.add(2, "c")
# q.add(3, "d")
# q.add(3, "e")
# print(q.find(1))
# print(q.find(2))
# print(q.find(3))

