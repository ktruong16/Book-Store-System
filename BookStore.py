import DLList
import MaxStack
import SLLStack
import algorithms
import Book
import SortableBook
import ArrayQueue
import ArrayList
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
import AdjacencyList
import time



class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
    def __init__(self) :
        self.bookCatalog = ArrayList.ArrayList()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        self.indexKey = ChainedHashTable.ChainedHashTable()
        self.indexSortedPrefix = BinarySearchTree.BinarySearchTree()
        self.bookSortedCatalog = ArrayList.ArrayList()
        # self.similaGraph = AdjacencyList.AdjacencyList(0)
        

    def loadCatalog(self, fileName : str) :
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        with open(fileName,encoding='utf8') as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                b = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(b)
                # self.indexSortedPrefix.add(b.title, self.bookCatalog.size() - 1)
                self.bookSortedCatalog.append(SortableBook.SortableBook(key, title, group, rank, similar))
                self.indexKey.add(key, self.bookCatalog.size() - 1)

            self.similaGraph = AdjacencyList.AdjacencyList(self.bookCatalog.size())
            for i in range(self.bookCatalog.size()):
                l = self.bookCatalog[i].similar.split()
                for k in range(1, len(l)):
                    j = self.indexKey.find(l[k])
                    if j is not None:
                        self.similaGraph.add_edge(i, j)

            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

        return self.bookCatalog.size()

    def addBookByIndex(self, i : int) :
        '''
        addBookByIndex: Inserts into the shopping cart the book with index i
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.push(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def addBookByKey(self, s : str) :
        '''
        addBookByIndex: Inserts into the shopping cart the book with key s
        input: 
            s: key string    
        '''
        i = self.indexKey.find(s)
        if i is not None:
            start_time = time.time()
            self.shoppingCart.push(self.bookCatalog.get(i))
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {self.bookCatalog.get(i)} \n{elapsed_time} seconds")
        # pass

    def addBookByPrefix(self, s : str) :
        '''
        addBookByPrefix: Inserts into the shopping cart the book with prefix s
        input: 
            s: Prefix    
        '''
        # Validating the index. Otherwise it  crashes
        i = self.indexSortedPrefix.find(s)
        if i is not None:
            start_time = time.time()
            self.shoppingCart.add(self.bookCatalog.get(i))
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {self.bookCatalog.get(i)} \n{elapsed_time} seconds")
        # pass

    def pathLength(self, s1: str, s2: str) :
        i = self.indexKey.find(s1)
        j = self.indexKey.find(s2)
        distance = self.similaGraph.distance(i, j)
        print(f"{s1} and {s2} are at distance {distance}")
        return distance



    def searchBookByInfix(self, infix : str) -> int:
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string 
        returns: 
            the number of books that contains infix in its title   
        '''
        # numberOfBooks = 0
        # for u in self.bookCatalog:
        #     if infix in u.title:
        #         if numberOfBooks == 50:
        #             return numberOfBooks
        #         print(u)
        #         numberOfBooks += 1
        # return numberOfBooks

        # bestSellers = BinaryHeap.BinaryHeap()
        # for u in self.bookCatalog:
        #     if infix in u.title:
        #         bestSellers.add(u)
        #
        # for i in range(bestSellers.size()):
        #     print(bestSellers.remove())

        heap = BinaryHeap.BinaryHeap()
        numberOfBooks = 0

        for book in self.bookCatalog:
            if infix in book.title:
                numberOfBooks += 1
                heap.add(book)
        while heap.size() > 0:
            book = heap.remove()
            index = self.indexKey.find(book.key)
            l = self.similaGraph.out_edges(index)
            print(f"{book.key}: {book.title}")
            for i in range(len(l)):
                print(f"Similar: {self.bookCatalog.get(l[i]).title}")
        return numberOfBooks

    def sortUsingMergeSort(self) :
        algorithms.merge_sort(self.bookSortedCatalog)

    
    def sortUsingQuickSort(self) :
        algorithms.quick_sort(self.bookSortedCatalog)

    def searchBookUsingBinarySearch(self, prefix : str) :
        s = SortableBook.SortableBook("", prefix, "", 0, None)
        j = algorithms.binary_search(self.bookSortedCatalog, self.bookSortedCatalog.size(), s)
        print(self.bookSortedCatalog.get(j))

    def removeFromShoppingCart(self) :
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")
            return u

    def checkIsPalindrome(self, word : str) :
        list = DLList.DLList()
        for x in word:
            list.add(0, x)
        print(list.isPalindrome())

# #LAB_1
# store = BookStore()
# # OPTION 1
# store.loadCatalog("books.txt")
# # OPTION 9
# store.removeFromShoppingCart()
# # OPTION 2
# store.addBookByIndex(0)
# store.addBookByIndex(542683)
# store.addBookByIndex(271341)
# store.addBookByIndex(135670)
# store.addBookByIndex(407012)
# # OPTION 9
# store.removeFromShoppingCart()
# store.removeFromShoppingCart()
# store.removeFromShoppingCart()
# store.removeFromShoppingCart()
# store.removeFromShoppingCart()
# # OPTION 5
# print("# of Books Found: ", store.searchBookByInfix(""))
# print("# of Books Found: ", store.searchBookByInfix("World of Pa"))
# print("# of Books Found: ", store.searchBookByInfix("Tears of the Wo"))

# # LAB_2
# store = BookStore()
# # OPTION 1
# store.loadCatalog("books.txt")
# # OPTION 9
# store.removeFromShoppingCart()
# # OPTION 2
# store.addBookByIndex(0)
# store.addBookByIndex(542683)
# store.addBookByIndex(271341)
# store.addBookByIndex(135670)
# store.addBookByIndex(407012)
# # OPTION 9
# store.removeFromShoppingCart()
# store.removeFromShoppingCart()
# store.removeFromShoppingCart()
# store.removeFromShoppingCart()
# store.removeFromShoppingCart()
# # OPTION 5
# print("# of Books Found: ", store.searchBookByInfix(""))
# print("# of Books Found: ", store.searchBookByInfix("World of Pa"))
# print("# of Books Found: ", store.searchBookByInfix("Tears of the Wo"))
# print(store.shoppingCart.max())

# # LAB_3
# store = BookStore()
# # OPTION 1
# store.loadCatalog("books.txt")
# # OPTION 3
# store.addBookByKey("1567302181")
# store.addBookByKey("0525444475")
# # OPTION 9
# store.removeFromShoppingCart()
# store.removeFromShoppingCart()

# LAB_4
# store = BookStore()
# # OPTION 1
# store.loadCatalog("books.txt")
# # OPTION 4
# store.addBookByPrefix("Tears of the S")
# store.addBookByPrefix("World of Po")
# # OPTION 9
# print(store.removeFromShoppingCart().title)
# print(store.removeFromShoppingCart().title)

# LAB_5
# store = BookStore()
# # OPTION 1
# store.loadCatalog("books.txt")
# # OPTION 4
# store.addBookByInfix("")
# store.addBookByInfix("World of Po")

# LAB_6
# store = BookStore()
# # OPTION 1
# store.loadCatalog("books.txt")
# # OPTION 6
# store.sortUsingMergeSort()
# # OPTION 7
# store.sortUsingQuickSort()
# # OPTION 8
# store.searchBookUsingBinarySearch("Tears of the S")
# store.searchBookUsingBinarySearch("World of Po")

# LAB_7
# store = BookStore()
# # OPTION 1
# store.loadCatalog("books.txt")
# # OPTION 5
# store.searchBookByInfix("The Art of Machine Piecing")
# store.searchBookByInfix("The Best of Howard Jones")
# # OPTION 10
# store.pathLength("0807842591", "1557509646")
# store.pathLength("B00005M2DR", "B00005M2DZ")
