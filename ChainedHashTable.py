from Interfaces import Set
from DLList import DLList
import numpy as np

class ChainedHashTable(Set):
    class Node() :
        def __init__(self, key, value) :
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList) :
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2**self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=np.object)
        for i in range(n):
            t[i] = self.dtype()
        return t


    def hash(self, key : int) -> int :
        return self.z * hash(key) % (2**self.w) >> (self.w - self.d)

    def size(self) -> int:
        return self.n

    def find(self, key : object) -> object :
        l = self.t[self.hash(key)]
        for y in range(len(l)):
            if l[y].key == key:
                return l[y].value
        return None
        # pass

    def add(self, key : object, value : object) :
        if self.find(key) is not None:
            return False
        if self.n + 1 > len(self.t):
            self.resize()
        self.t[self.hash(key)].append(self.Node(key, value))
        self.n += 1
        return True
        # pass

    def remove(self, key : int)  -> object:
        l = self.t[self.hash(key)]
        for i in range(len(l)):
            u = l[i]
            if u.key == key:
                l.remove(i)
                self.n -= 1
                if 3 * self.n <= len(self.t):
                    self.resize()
            return u.value
        return None
        # pass

    def resize(self):
        if self.n == len(self.t):
            self.d += 1
        else:
            self.d -= 1
        a = self.alloc_table(2**self.d)
        for j in range(len(self.t)):
            for i in range(self.t[j].size()):
                a[self.hash(self.t[j].get(i).key)].append(self.t[j].get(i))
        self.t = a
        # pass

    def __str__(self):
        s = "["
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += str(k.key)
                s += ":"
                s += str(k.value)
                s += ";"
        return s + "]"


# cht = ChainedHashTable()
# print(cht.remove(0))
# print(cht.find(2))
# cht.add(1, "first")
# cht.add(2, "second")
# cht.add(3, "fourth")
# print(cht.size())
# print(cht.find(3))
# cht.remove(3)
# print(cht.size())
# print(cht.find(3))
# cht.add(3, "third")
# cht.add(4, "fourth")
# cht.add(5, "fifth")
# print(cht.size())
# print(cht.find(3))

