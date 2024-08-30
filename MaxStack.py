from Interfaces import Stack
import SLLStack


class MaxStack(Stack) :
    def __init__(self):
        self.stack = SLLStack.SLLStack()
        self.maxStack = SLLStack.SLLStack()
        
    def max(self) ->object:
        '''
            Returns the max element
        '''
        return self.maxStack.head.x
        # pass
    
    def push(self, x : object) : 
        '''
            push: Insert an element in the tail of the stack 
            Inputs:
                x: Object type, i.e., any object
        '''
        max = x

        if self.maxStack.size() != 0 and max < self.maxStack.head.x:
            max = self.maxStack.head.x

        self.stack.push(x)
        self.maxStack.push(max)
        # pass

    def pop(self) -> object:
        '''
            pop: Remove the last element in the stack 
            Returns: the object of the tail if it is no empty
        '''
        if self.stack.n > 0:
            self.maxStack.pop()
            return self.stack.pop()
        elif self.stack.n == 0:
            self.stack.pop()
            return;
        # pass

    def size(self) -> int:
        return self.stack.size()

# maxstack = MaxStack()
# maxstack.pop()
# maxstack.push(3)
# maxstack.push(1)
# maxstack.push(4)
# maxstack.push(2)
# print(maxstack.stack)
# print(maxstack.max())
# print(maxstack.pop())
# print(maxstack.pop())
# print(maxstack.stack)
# print(maxstack.max())
# print(maxstack.pop())
# print(maxstack.max())