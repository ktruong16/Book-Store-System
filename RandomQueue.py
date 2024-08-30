import random 
from Interfaces import Queue 
import ArrayQueue


class RandomQueue(Queue):
    def __init__(self):
        self.queue = ArrayQueue.ArrayQueue()


    def add(self, x : object):
        '''
            add: Add the value x to the Queue
            Inputs:
                x: Object type, i.e., any object
        '''
        self.queue.add(x)

    def remove(self) -> object:
        '''
            remove: remove the next (previously added) value, y, from the
                    Queue and return y. The Queue’s queueing discipline 
                    decides which element should be removed.
            Return: Object type
        '''
        try:
            if self.queue.size() == 0:
                raise IndexError
            y = random.randint(0, self.queue.size() - 1)
            temp = self.queue.a[self.queue.j]
            self.queue.a[self.queue.j] = self.queue.a[y]
            self.queue.a[y] = temp
            self.queue.remove()
            return y
        except IndexError:
            print("Error: Nothing can be removed when queue is empty")
    
    def size(self) -> int:
        return self.queue.size()

# randomqueue = RandomQueue()
# randomqueue.remove()
# randomqueue.add(1)
# randomqueue.add(2)
# randomqueue.add(3)
# randomqueue.add(4)
# randomqueue.add(5)
# print(randomqueue.queue)
# print(randomqueue.remove())
# print(randomqueue.queue)
# print(randomqueue.remove())
# print(randomqueue.queue)
# print(randomqueue.remove())
# print(randomqueue.queue)
# print(randomqueue.remove())
# print(randomqueue.queue)
# print(randomqueue.remove())
# print(randomqueue.queue)
