#Quiz 2 - Coding Part
#March 26th, 2019
#######################
## QUESTION 1
def negatives(numList, i=0):
    finalList = []
    if i < len(numList):
        if numList[i] < 0:
            finalList.append(numList[i])
        finalList = finalList + negatives(numList, i+1)
    return finalList

## QUESTION 2
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)
    
    __repr__ = __str__

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        # Adds a new node at the beginning of the list
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def findLast(self):
        #Write your code here
        if self.head is None:
            return None
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        return temp
