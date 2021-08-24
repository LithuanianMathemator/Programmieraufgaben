
class MaxHeap:

    def __init__(self, keys):
        # building maxheap before asigning to self
        buildmaxheap(keys)

        self.keys = keys

    def maximum(self):
        # first element of maxheap is maximum
        return self.keys[0]

    def extractMax(self):
        n = len(self.keys)
        self.keys[0], self.keys[n-1] = self.keys[n-1], self.keys[0]
        # extracting the maximum
        maximum = self.keys.pop()
        # making sure array is heap again
        maxHeapify(self.keys, 0)
        # returning maximum
        return maximum

    def increaseKey(self, i, k):
        # not an increase
        if k < self.keys[i]:
            return "k too small"
        self.keys[i] = k
        # initial parent
        parent = (i-1)//2
        while i > 0 and self.keys[parent] < self.keys[i]:
            # swap
            self.keys[i], self.keys[parent] = self.keys[parent], self.keys[i]
            # new node is now former parent node
            i = parent
            # new parent node is parent of former parent node
            parent = (i-1)//2

    def insert(self, k):
        n = len(self.keys)-1
        n = n + 1
        self.keys.append(-1)
        self.increaseKey(n, k)

    def heapSort(self):
        # list to append to
        sorted = []
        while len(self.keys) > 0:
            # appending maximum, extracting maximum
            sorted.append(self.extractMax())
        # reassigning sorted to self
        self.keys = sorted


def maxHeapify(A, i):
    l = 2*i+1
    r = 2*i+2
    n = len(A)-1
    largest = i

    # looking for biggest node out of i, left and right
    if l <= n and A[l] > A[i]:
        largest = l

    if r <= n and A[r] > A[largest]:
        largest = r

    # swap if maxheap not fulfilled
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        # recursion
        maxHeapify(A, largest)


def buildmaxheap(A):
    n = len(A)-1
    # looping through non-leaves from bottom
    for i in range(n//2, -1, -1):
        maxHeapify(A, i)
