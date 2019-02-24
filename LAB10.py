#Lab #10
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

class Stack:
    def __init__(self):
        self.top = None

    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        # Check if there is a top value to determine if the stack has any items
        if self.top == None:
            return True
        return False

    def __len__(self):
        # If the stack is empty, there are no items
        # Otherwise loop to find the end of the stack
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
        # Simply return the top of the stack unless empty
        if self.isEmpty():
                return 'Stack is empty'
        return self.top.value

    def push(self,value):
        # Just add to the top of the stack
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        # If there are values in the stack, remove the top item
        if not self.isEmpty():
            value = self.top.value
            self.top = self.top.next
            return value
        return 'Stack is empty'
