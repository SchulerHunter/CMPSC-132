#Lab #9
#Due Date: 03/01/2019, 11:59PM
########################################
#
# Name: Hunter Schuler
# Collaboration Statement: I neither sought nor gave assitance
#
########################################
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__

class OrderedLinkedList:
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
        return ('Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def add(self, value):
        node = Node(value)
        # If the list is empty, initialize it with the value as both the head and tail
        if self.isEmpty():
            self.head = node
            self.tail = node
        # If the value is greater than the head, then just push it to the front
        elif node.value > self.head.value:
            node.next = self.head
            self.head = node
        # Otherwise test the value through the list
        else:
            temp = self.head
            while temp:
                # If there is no more next values, the added value is the lowest, and will be added as the tail
                # If it is greater then a value in the list, it will be added in the correct position
                # Otherwise test the next value
                if temp.next == None:
                    temp.next = node
                    self.tail = node
                    break
                elif node.value > temp.next.value:
                    node.next = temp.next
                    temp.next = node
                    break
                else:
                    temp = temp.next

    def pop(self):
        # If there are no values, return that the list is empty
        if self.isEmpty():
            return 'List is empty'
        # Otherwise if the value after the head is empty, then the head is the only value and the
        # list is reset to nothing
        elif self.head.next == None:
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        # If none of the above two cases, loop through the list to remove the last value,
        # whose next item will be none
        else:
            temp = self.head
            while temp:
                if temp.next.next == None:
                    self.tail = temp
                    value = temp.next.value
                    temp.next = None
                    return value
                else:
                    temp = temp.next

    def isEmpty(self):
        # Simply test if the list as been initialized
        if self.head == None:
            return True
        return False

    def __len__(self):
        # If the list is not initialized, return 0, otherwise loop to the end
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
