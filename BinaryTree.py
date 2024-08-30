import ArrayQueue
#from drawtree import draw_bst

class BinaryTree:
    class Node:
        def __init__(self, x : object, v = None) :
            self.parent = self.left = self.right = None
            self.x = x
            self.v = v

        def set_val(self, x) :
            self.x = x

        def insert_left(self) :
            self.left = BinaryTree.Node('') 
            self.left.parent = self
            return self.left

        def insert_right(self) :
            self.right = BinaryTree.Node('')
            self.right.parent = self
            return self.right

    def __init__(self) : 
        self.r = None
        self.nil = None

    def depth(self, u : Node) -> int:
        d = 0
        while u is not self.r:
            u = u.parent
            d += 1
        return d
        # pass

    def size(self) -> int:
        return self._size(self.r)
        # pass
    
    def _size(self, u : Node) -> int:
        if u == self.nil: return 0
        return 1 + self._size(u.left) + self._size(u.right)
    
    def size2(self) -> int:
        u = BinaryTree.Node(self.r)
        prev = self.nil
        next = self.nil
        n = 0
        while u != self.nil:
            if prev == u.parent:
                n += 1
                if u.left != self.nil:
                    next = u.left
                elif u.right != self.nil:
                    next = u.right
                else:
                    next = u.parent
            elif prev == u.left:
                if u.right != self.nil:
                    next = u.right
                else:
                    next = u.parent
            else:
                next = u.parent
            prev = u
            u = next
        return n
        # pass

    def height(self) -> int:
        return self._height(self.r)
        # pass
    
    def _height(self, u : Node) -> int:
        if u == self.nil: return 0
        return 1 + max(self._height(u.left), self._height(u.right))
    
    def traverse(self, u : Node):
        if u == self.nil:
            return
        self.traverse(u.left)
        self.traverse(u.right)
        # pass

    def traverse2(self):
        u = BinaryTree.Node(self.r)
        prev = self.nil
        next = self.nil
        while u != self.nil:
            if prev == u.parent:
                if u.left != self.nil:
                    next = u.left
                elif u.right != self.nil:
                    next = u.right
                else:
                    next = u.parent
            elif prev == u.left:
                if u.right != self.nil:
                    next = u.right
                else:
                    next = u.parent
            else:
                next = u.parent
            prev = u
            u = next
        # pass

    def bf_traverse(self):
        q = ArrayQueue.ArrayQueue()
        if self.r is not self.nil:
            q.add(self.r)
        while q.size() > 0:
            u = q.remove()
            print(u.x, ": ", u.v)
            if u.left is not None:
                q.add(u.left)
            if u.right is not None:
                q.add(u.right)
        # pass
            
    def first_node(self):
        w = self.r
        if w == self.nil: return self.nil
        while w.left != self.nil:
            w = w.left
        return w
    
    def next_node(self, w):
        if w.right != self.nil:
            w = w.right
            while w.left != self.nil:
                w = w.left
        else:
            while w.parent != self.nil and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w
    
    def in_order(self) :
        self._inorder(self.r)
        # pass

    def pre_order(self) :
        self._preorder(self.r)
        # pass

    def pos_order(self) :
        self._postorder(self.r)
        # pass

    def _inorder(self, u: Node):
        if u.left is not self.nil:
            self._inorder(u.left)
        print(u.x, ": ", u.v)
        if u.right is not self.nil:
            self._inorder(u.right)

    def _preorder(self, u: Node):
        print(u.x, ": ", u.v)
        if u.left is not self.nil:
            self._preorder(u.left)
        if u.right is not self.nil:
            self._preorder(u.right)

    def _postorder(self, u: Node):
        if u.left is not self.nil:
            self._postorder(u.left)
        if u.right is not self.nil:
            self._postorder(u.right)
        print(u.x, ": ", u.v)

    def __str__(self):
        l = []
        #self.in_order(self.r, l)
        return ', '.join(map(str, l))