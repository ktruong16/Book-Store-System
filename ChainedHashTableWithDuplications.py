from Interfaces import Set
from DLList import DLList
import ChainedHashTable 

class ChainedHashTableWithDuplications(Set):
    def __init__(self) :
        self.chainHashTable = ChainedHashTable.ChainedHashTable()
        self.n = 0

    def size(self) -> int:
        return self.n
        
    def find(self, key : object) -> object :
        if self.chainHashTable.find(key) is not None:
            s = ""
            dllist = self.chainHashTable.t[self.chainHashTable.hash(key)]
            for j in range(dllist.size()):
                if j == dllist.size() - 1:
                    s += str(dllist.get(j).value)
                else:
                    s += str(dllist.get(j).value + ", ")
            return s

        
    def add(self, key : object, value : object) :
        if self.chainHashTable.find(key) is None:
            self.chainHashTable.add(key, value)
        else:
            self.chainHashTable.t[self.chainHashTable.hash(key)].append(self.chainHashTable.Node(key, value))
        self.n += 1
        # pass


    def remove(self, key : int)  -> object:
        if self.chainHashTable.find(key) is not None:
            self.chainHashTable.remove(key)
            self.n -= 1
        # pass
    
    
    def __str__(self):
        return self.chainHashTable.__str__()


# duplicate = ChainedHashTableWithDuplications()
# duplicate.add(1, "a")
# duplicate.add(1, "b")
# duplicate.add(2, "c")
# duplicate.add(3, "d")
# duplicate.add(3, "e")
# print(duplicate.find(1))
# print(duplicate.find(2))
# print(duplicate.find(3))

