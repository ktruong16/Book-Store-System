from Interfaces import Queue
import numpy as np

class SLLQueue(Queue):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.x = x
            
    def __init__(self) :
        self.head = None
        self.tail = None
        self.n = 0

    def add(self, x :np.object) :
        u = self.Node(x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.n += 1
        return True
        # pass

    def remove(self) -> np.object:
        try:
            if self.n == 0:
                raise IndexError
            else:
                x = self.Node(self.head.x)
                self.head = self.head.next
                self.n -= 1
                if self.n == 0:
                    self.tail = None
                return x
        except IndexError:
            print("Error: Not possible to remove an empty linked list.")
        # pass

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x


# queue = SLLQueue()
# queue.remove()
# queue.add(1)
# queue.add(2)
# queue.add(3)
# queue.add(4)
# queue.add(5)
# print(queue)
# queue.remove()
# print(queue)
# queue.remove()
# print(queue)
# queue.remove()
# print(queue)
# queue.remove()
# print(queue)
# queue.remove()
# print(queue)