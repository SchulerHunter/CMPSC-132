#Lab #11
#Due Date: 03/15/2019, 11:59PM
########################################
#
# Name: Hunter Schuler
# Collaboration Statement: I neither sought nor gave assistance
#
########################################
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None

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
        # Check if there is a top value to determine if the stack has any items
        if self.head == None:
            return True
        return False

    def __len__(self):
        # If the queue is not initialized, return 0, otherwise loop to the end
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
        # If the queue is empty, add the item to the beginning and end
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        # If there are no values, return that the list is empty
        if self.isEmpty():
            return 'Queue is empty'
        # Otherwise if the value after the head is empty, then the head is the only value and the
        # list is reset to nothing
        elif self.head.next == None:
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        # If none of the above two cases, make the new head the item it points to
        else:
            value = self.head.value
            self.head = self.head.next
            return value
