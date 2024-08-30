import numpy as np
import ArrayStack
import ChainedHashTable
import DLList
import BinaryTree
import operator

class Calculator:
    def __init__(self) :
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k :str, v : float) :
        self.dict.add(k,v)

    def print_expression(self, s : str) -> str :
        if self.matched_expression(s):
            t = ''
            for i in s:
                if self.dict.find(i) is not None:
                    t += str(self.dict.find(i))
                else:
                    t += i
            return t

    def matched_expression(self, s : str) -> bool :
        stack = ArrayStack.ArrayStack()
        for k in range(len(s)):
            char = s[k]
            if char == '(':
                stack.push(char)
            elif char == ')':
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()

        if stack.n == 0:
            return True
        else:
            return False


    def build_parse_tree(self, exp : str) ->str:
        if self.matched_expression(exp):
            t = BinaryTree.BinaryTree()
            t.r = t.Node('')
            u = t.r
            for char in exp:
                if char == '(':
                    u.insert_left()
                    u = u.left
                elif char == '+' or char == '-' or char == '/' or char == '*':
                    u.x = char
                    u.insert_right()
                    u = u.right
                elif self.dict.find(char):
                    u.x = self.dict.find(char)
                    u = u.parent
                elif char == ')':
                    u = u.parent
            return t
        

    def _evaluate(self, u):
        if u is None:
            return 0

        if u.left is None and u.right is None:
            return u.x

        left_sum = self._evaluate(u.left)
        right_sum = self._evaluate(u.right)

        if u.x == '+':
            return left_sum + right_sum
        elif u.x == '-':
            return left_sum - right_sum
        elif u.x == '*':
            return left_sum * right_sum
        elif u.x == '/':
            return left_sum / right_sum
        # pass

    def evaluate(self, exp):
        try:
            parseTree = self.build_parse_tree(exp)
            return round(self._evaluate(parseTree.r), 2)
        except:
            return 0

'''
s = Calculator()
print(s.evaluate("((a*b)+(c*d))"))
s.set_variable("a", 1.3)
s.set_variable("b", 2.1)
s.set_variable("c", 2.2)
s.set_variable("d", 3.0)
print(s.evaluate("((a*b)+(c*d))"))
'''
# s = Calculator()
# # OPTION 1
# print(s.matched_expression("(a+b)*)c -d)"))
# print(s.matched_expression("(a+b(*(c -d)"))
# print(s.matched_expression(")a+b(*(c -d)"))
# print(s.matched_expression("a+b*c-d"))
# print(s.matched_expression("(a+b)*(c -d)"))

# print(s.print_expression(""))
# print(s.print_expression("((a * b) + (c * d))"))
# s.set_variable("a", 1.3)
# s.set_variable("b", 2.1)
# s.set_variable("c", 2.2)
# s.set_variable("d", 3.0)
# print(s.print_expression("((a*b)+(c*d))"))

# s = Calculator()
# print(s.evaluate(""))
# print(s.evaluate("((a∗b)+(c∗d))"))
# s.set_variable("a", 1.3)
# s.set_variable("b", 2.1)
# s.set_variable("c", 2.2)
# s.set_variable("d", 3.0)
# print(s.evaluate("((a*b)+(c*d))"))
