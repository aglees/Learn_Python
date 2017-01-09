# using old-style Python objects, hence no (object) in declaration
class binHeap:

    def __init__(self):
        # heapList is initialized with a single-zero. 
        # this enables the first real element to come in at pos.1
        # making the child location math easier [2n and 2n+1]
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        # while you haven't hit the zero-th index (bad)
        while i // 2 > 0:
            # if the child is less than parent
            if self.heapList[i] < self.heapList[i // 2]:
                # use a temp variable to swap those nodes in the list
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            # set i to the parent node in prep for running this again
            # once it gets to i == 1 then the while will finish
            i = i // 2

    def percDown(self, i):
        # while we haven't gone past the end of the list
        while (i*2) <= self.currentSize:
            # get the minimm child node index
            mc = self.minChild(i)
            # compare current node to min child node, and swap required
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            # repeat for where min child used to be
            i = mc

    def minChild(self, i):
        # checks if there is a right child-node
        # if not, returns the left child-node
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            # compare and return min left and right child nodes
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        # min value is at the root, but into temp variable
        retval = self.heapList[1]
        # move the last list item to root
        self.heapList[1] = self.heapList[self.currentSize]
        # reduce current size by one
        self.currentSize = self.currentSize - 1
        # remove the last element
        self.heapList.pop()
        # run the percDown methods starting at the root node
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        # floor divide list to get the penultimate nodes
        i = len(alist) // 2
        # as we have a zero-th element, the new size will be size of added list
        self.currentSize = len(alist)
        # add the new list to the heap
        self.heapList = [0] + alist[:]
        # while we haven't hit the zeroth element (bad)
        while i > 0:
            # perDown those penultimate nodes
            self.percDown(i)
            # move towards the root node
            i = i - 1
            