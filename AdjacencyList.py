"""An implementation of the adjacency list representation of a graph"""
import numpy

import DLList
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()
            
    def add_edge(self, i : int, j : int):
        self.adj[i].append(j)
        # pass
        
    def remove_edge(self, i : int, j : int):
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return
        # pass
                
    def has_edge(self, i : int, j: int) ->bool:
        for k in self.adj[i]:
            if k == j:
                return True
        return False
        # pass
        
    def out_edges(self, i) -> List:
        return self.adj[i]
        # pass

    def in_edges(self, j) -> List:
        out = ArrayList.ArrayList()
        for i in range(self.n):
            if self.has_edge(i, j):
                out.append(i)
        return out
        # pass

    def bfs(self, r :int):
        seen = numpy.zeros(self.n, numpy.bool_)
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        seen[r] = True
        while q.size() > 0:
            i = q.remove()
            print(i)
            for j in self.out_edges(i):
                if not seen[j]:
                    q.add(j)
                    seen[j] = True
        # pass

    def dfs(self, r :int):
        c = numpy.zeros(self.n, numpy.bool_)
        s = ArrayStack.ArrayStack()
        s.push(r)
        c[r] = True
        while s.size() > 0:
            i = s.pop()
            print(i)
            for j in self.out_edges(i):
                if not c[j]:
                    c[j] = True
                    s.push(j)
        # pass

    def distance(self, r : int, dest: int):
        c = numpy.zeros(self.n, numpy.bool_)
        p = numpy.zeros(self.n)
        s = ArrayStack.ArrayStack()
        s.push(r)
        p[r] = 0
        while s.size() > 0:
            i = s.pop()
            if not c[i]:
                c[i] = True
                neighbors = self.out_edges(i)
                for j in neighbors:
                    if not c[j]:
                        s.push(j)
                        p[j] = p[i] + 1
                        if j == dest:
                            return int(p[j])
        # pass

    def size(self) -> int :
        return self.n
                      
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s


# g = AdjacencyList(4)
# g.add_edge(0, 1)
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(3, 0)
# g.add_edge(0, 2)
# print(g.has_edge(0, 1))
# print(g.has_edge(1, 3))
# print(g.in_edges(2))
# print(g.out_edges(0))
# print(g.bfs(0))
# print(g.dfs(1))

