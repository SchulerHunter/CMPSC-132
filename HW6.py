#HW 6
#Due Date: 04/26/2019, 11:59PM
########################################
#
# Name: Hunter Schuler
# Collaboration Statement: Neither sought nor gave assistance
#
########################################
    #----- HW6 Graph code


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class Stack:
    def __init__(self):
        self.top = None

    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top, out))

    __repr__ = __str__

    def isEmpty(self):
        if self.top == None:
            return True
        return False

    def __len__(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            temp = self.top
            while temp:
                if temp.next == None:
                    return count
                else:
                    temp = temp.next
                    count += 1

    def peek(self):
        if self.isEmpty():
                return 'Stack is empty'
        return self.top.value

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.isEmpty():
            value = self.top.value
            self.top = self.top.next
            return value
        return 'Stack is empty'
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def __len__(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            temp = self.head
            while temp:
                if temp.next == None:
                    return count
                else:
                    temp = temp.next
                    count += 1

    def enqueue(self, value):
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        elif self.head.next == None:
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        else:
            value = self.head.value
            self.head = self.head.next
            return value

class Graph:
    def __init__(self, graph_repr):
        self.vertList=graph_repr

    def bfs(self, start):
        # Test if start is in graph
        try:
            self.vertList[start]
        except KeyError:
            return 'Error, start not found in Graph'
        # Create a list for all vertices on whether they were checked or not
        checked = {}
        result = []
        for key in self.vertList:
            checked[key[0]] = False
        # Create a queue for the BFS
        BFSQueue = Queue()
        # Mark the start as checked and enqueue
        BFSQueue.enqueue(start)
        checked[start] = True
        result.append(start)

        # Begin the search
        while not BFSQueue.isEmpty():
            # Pop the current node
            node = BFSQueue.dequeue()
            # Creates and sorts an adjacency list for alphabetical order
            adjList = []
            for adjacent in self.vertList[node]:
                adjList.append(adjacent[0])
            adjList.sort()
            # For each item in the adjacency list, if it hasn't been searched, queue it and append it to the search
            for adjacent in adjList:
                if not checked[adjacent]:
                    BFSQueue.enqueue(adjacent)
                    checked[adjacent] = True
                    result.append(adjacent)
        
        return result

    def dfs(self, start):
        # Test if start is in graph
        try:
            self.vertList[start]
        except KeyError:
            return 'Error, start not found in Graph'
        # Create a list for all vertices on whether they were checked or not
        checked = {}
        result = []
        for key in self.vertList:
            checked[key[0]] = False
        # Create the DFS Stack and push the start
        DFSStack = Stack()
        DFSStack.push(start)

        # Begin the search
        while not DFSStack.isEmpty():
            # Pop the current node and append it to the results
            node = DFSStack.pop()
            if not checked[node]:
                checked[node] = True
                result.append(node)
                # Create an adjacency list
                adjList = []
                for adjacent in self.vertList[node]:
                    adjList.append(adjacent[0])
                # Sort the adjacency list in reverse order
                adjList.sort(reverse=True)
                # Add each item that isnt checked to the adjacency list and mark it as checked
                for adjacent in adjList:
                    if not checked[adjacent]:
                        DFSStack.push(adjacent)
        
        return result

    def dijkstra(self,start):
        # Test if start is in graph
        try:
            self.vertList[start]
        except KeyError:
            return 'Error, start not found in Graph'
        # Create a dictionary to store all the distaces and initialize each value to infinity
        # Create a stack to keep track of the current node
        # Create a dictionary to mark nodes as visited, initialized to false
        nodeStack = Stack()
        distances = {}
        visitedNodes = {}
        for key in self.vertList:
            distances[key[0]] = float("inf")
            visitedNodes[key[0]] = False

        distances[start] = 0
        nodeStack.push(start)

        while not nodeStack.isEmpty():
            # Update the node and mark it as visited
            node = nodeStack.pop()
            visitedNodes[node] = True
            # Initilaize minimum distance for next node
            min = float('inf')
            # Search not nearest vertex not in the shortest path tree
            # Set the edge distances equal to the distance of the current node plus the distance to that edge
            # If it is less than the current distance
            for adjacent in self.vertList[node]:
                if adjacent[1] < min and visitedNodes[adjacent[0]] == False:
                    min = adjacent[1]
                    nodeStack.push(adjacent[0])
                if distances[adjacent[0]] > distances[node] + adjacent[1]:
                    distances[adjacent[0]] = distances[node] + adjacent[1]
        return distances