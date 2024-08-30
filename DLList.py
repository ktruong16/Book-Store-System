from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self) :
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0
   
    def get_node(self, i : int) -> Node:
        if i < self.n / 2:
            p = self.dummy.next
            for j in range(0, i):
                p = p.next
        else:
            p = self.dummy
            for j in range(self.n, i, -1):
                p = p.prev
        return p
        # pass
        
    def get(self, i) -> np.object:
        return self.get_node(i).x
        # pass

    def set(self, i : int, x : np.object) -> np.object:
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y
        # pass

    def add_before(self, w : Node, x : np.object) -> Node:
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u
        # pass
            
    def add(self, i : int, x : np.object)  :
        self.add_before(self.get_node(i), x)
        # pass

    def _remove(self, w : Node) :
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        # pass
    
    def remove(self, i :int) :
        try:
            if i < 0 or i >= self.n:
                raise IndexError
            else:
                w = self.get_node(i)
                self._remove(w)
                return w.x
        except IndexError:
            print("Error: Not possible to remove anything from empty list")
        # pass

    def size(self) -> int:
        return self.n

    def append(self, x : np.object)  :
        self.add(self.n, x)

    def isPalindrome(self) -> bool :
        n = self.dummy.next
        p = self.dummy.prev
        while n.x == p.x and n != self.dummy:
            n = n.next
            p = p.prev
        return n == self.dummy
        # pass

    def reverse(self) :
        c = self.dummy
        for i in range (self.n + 1):
            t = c.prev
            n = c.next
            c.prev, c.next = c.next, t
            c = n
        # pass

         
    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"


    def __getitem__(self, i) -> object:
        '''
            __getitem__: Returns the item in the position i in array format, i.e., l[i]
            where l is a list instance
            Input: 
                i: positive integer less than n
            Return: the item at index i
        '''
        if isinstance(i, slice):
            raise IndexError("Not implemented. Please use the references next and prev")
        else:
            return self.get(i)


    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x

# dll = DLList()
# dll.remove(0)
# dll.add(0, 4)
# dll.add(0, 1)
# dll.add(1, 3)
# dll.add(1, 2)
# dll.add(4, 5)
# print(dll)
# dll.remove(2)
# dll.remove(3)
# print(dll)

# dll.remove(0)
# dll.add(0, 1)
# print(dll)
# dll.add(0, 2)
# dll.add(0, 3)
# dll.add(0, 4)
# dll.add(0, 5)
# print(dll)
# dll.reverse()
# print(dll)

# print(dll.isPalindrome())
# dll.add(0, 'a')
# print(dll.isPalindrome())
#
# dll.add(0, 'h')
# dll.add(0, 'a')
# dll.add(0, 'n')
# dll.add(0, 'n')
# dll.add(0, 'a')
# dll.add(0, 'h')
# print(dll.isPalindrome())
#
# dll.add(0, 'e')
# dll.add(0, 'v')
# dll.add(0, 'e')
# print(dll.isPalindrome())
#
# dll.add(0, 's')
# dll.add(0, 'i')
# dll.add(0, 'h')
# dll.add(0, 't')
# print(dll.isPalindrome())
