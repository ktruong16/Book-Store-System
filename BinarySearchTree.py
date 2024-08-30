from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self, nil=None):
        super().__init__()
        self.n = 0
        self.nil = nil
        
    def clear(self):
        self.r = self.nil
        self.n = 0

    def new_node(self, x):
        u = BinaryTree.Node(x)
        u.left = u.right = u.parent = self.nil
        return u
    
        
    def find_last(self, x : object) -> BinaryTree.Node:
        w = self.r
        prev = self.nil
        while w is not self.nil:
            prev = w
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return prev
        # pass
        
    def add_child(self, p : BinaryTree.Node, u : BinaryTree.Node) -> bool:
        if p is self.nil:
            self.r = u
        else:
            if u.x < p.x:
                p.left = u
            elif u.x > p.x:
                p.right = u
            else:
                return False
            u.parent = p
        self.n += 1
        return True
        # pass

    def find_eq(self, x : object) -> object:
        w = self.r
        while w is not None:
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return self.nil
        # pass
    
    def find(self, x: object) -> object:
        w = self.r
        z = self.nil
        while w is not self.nil:
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.x
        if z is self.nil:
            return self.nil
        return z.v
        # pass
        
    def add(self, key : object, value : object) -> bool:
        p = self.find_last(key)
        return self.add_child(p, BinaryTree.Node(key, value))
       # pass
        
    def add_node(self, u : BinaryTree.Node) -> bool:
        p = self.find_last(u.x)
        return self.add_child(p, u)
        # pass
    
    def splice(self, u: BinaryTree.Node):
        if u.left is not self.nil:
            s = u.left
        else:
            s = u.right
        if u is self.r:
            self.r = s
            p = self.nil
        else:
            p = u.parent
            if p.left is u:
                p.left = s
            else:
                p.right = s
        if s is not self.nil:
            s.parent = p
        self.n -= 1
        # pass

    def remove_node(self, u : BinaryTree.Node):
        if u.left is self.nil or u.right is self.nil:
            self.splice(u)
        else:
            w = u.right
            while w.left is not self.nil:
                w = w.left
            u.x = w.x
            self.splice(w)
        # pass

    def remove(self, x : object) -> bool:
        if self.find_eq(x):
            w = self.find_eq(x)
            self.remove_node(w)
            return True
        else:
            return False
        # pass
             
    def __iter__(self):
        u = self.first_node()
        while u != self.nil:
            yield u.x
            u = self.next_node(u)


# q = BinarySearchTree()
# print(q.remove(0))
# print(q.find(2))
# q.add(3, "third")
# q.add(2, "second")
# q.add(1, "first")
# print(q.size())
# print(q.find(2.5))
# q.remove(3)
# print(q.size())
# print(q.find(3))
# q.add(3, "third")
# q.add(5, "fifth")
# q.add(4, "fourth")
# print(q.size())
# print(q.find_eq(3.4))
# print(q.find(3.4))
# print("In order")
# q.in_order()
# print("Pre order")
# q.pre_order()
# print("Post order")
# q.post_order()
# print("bf traversal")
# q.bf_traverse()
# print(q.height())
