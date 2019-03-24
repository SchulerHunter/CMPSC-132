#LAB X
#Due Date: 04/07/2019, 11:59PM
########################################
#
# Name: Hunter Schuler
# Collaboration Statement: I neither sought nor gave assistance
#
########################################


class MaxHeapPriorityQueue:
    def __init__(self):
        self.heap = []
        self.size = 0

    def __len__(self):
        # Len should always just return the size
        return self.size

    def parent(self, index):
        # The parent is always the index - 1 with a floor divide
        if index == 1:
            return None
        return self.heap[(index - 1) // 2]

    # The left child of a provided index is 2 * index
    # and the right is just + 1. Since this is 1:n, both
    # must be subtracted by 1

    def leftChild(self, index):
        try:
            return self.heap[(index * 2) - 1]
        except IndexError:
            return None

    def rightChild(self, index):
        try:
            return self.heap[index * 2]
        except IndexError:
            return None

    def swap(self, index1, index2):
        self.heap[index1-1], self.heap[index2 -
                                       1] = self.heap[index2-1], self.heap[index1-1]

    def insert(self, x):
        # Adjust the size and add the item to the end of the heap list
        self.size += 1
        self.heap.append(x)
        index = self.size-1
        # Sort through the list until the proper place is found for the inserted item
        while index > 0:
            parentIndex = (index - 1) // 2
            parent = self.heap[parentIndex]
            # If the inserted child is greater than the parent, they must be swapped
            if parent < x:
                self.heap[index] = parent
                index = parentIndex
                continue
            break
        self.heap[index] = x

    def deleteMax(self):
        if self.size <= 0:
            return None
        else:
            # Store the max value
            max = self.heap[0]
            # Swap the first and last elements and decrease the size
            self.swap(1, self.size)
            self.size -= 1
            self.heap.pop()
            # Loop through the children recursively until a leaf is reached
            index = 0
            childIndex = index * 2 + 1
            # If the next child is in the index do a search comparing the left to the right
            while childIndex < self.size:
                rChildIndex = childIndex + 1
                if rChildIndex < self.size and self.heap[rChildIndex] > self.heap[childIndex]:
                    # If the right is greater than the left swap the right child with the parent
                    childIndex = rChildIndex
                # Swap the parent and child value, then determine the new left child index
                if self.heap[childIndex] > self.heap[index]:
                    self.swap(index+1, childIndex+1)
                    index = childIndex
                    childIndex = index * 2 + 1
                else:
                    break
            return max

def heapSort(numList):
    # Create a heap and add all values
    sort_heap = MaxHeapPriorityQueue()
    for i in range(len(numList)):
        sort_heap.insert(numList[i])
    result = []
    # Loop through the heap removing each max value and adding it to the beginning of the list
    while sort_heap.size > 0:
        result.insert(0, sort_heap.deleteMax())
    return result
