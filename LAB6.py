#Lab #6
#Due Date: 02/08/2019, 11:59PM
########################################
#
# Name: Hunter Schuler
# Collaboration Statement: Neither sought nor gave assistance
#
########################################


class Vector:
    # Create a length for dimension, a list for the vector info, and a returnable for returning the object
    def __init__(self, vector_list):
        self.vector = vector_list
        self.len = len(vector_list)
        self.returnable = f'Vector({self.vector})'

    # Overrides the add function, checking that both inputs are the same type and length
    def __add__(self, other):
        if type(other) == type(self):
            if other.len == self.len:
                sumVec = []
                for i in range(self.len):
                    sumVec.append(self.vector[i]+other.vector[i])
                vector = Vector(sumVec)
                return vector
            else:
                return "Error - Invalid dimensions"
        else:
            return "Error - Invalid operation"

    # Overrides the subtraction function, checking that both are the same type and length
    def __sub__(self, other):
        if type(other) == type(self):
            if other.len == self.len:
                subVec = []
                for i in range(self.len):
                    subVec.append(self.vector[i]-other.vector[i])
                vector = Vector(subVec)
                return vector
            else:
                return "Error - Invalid dimensions"
        else:
            return "Error - Invalid operation"

    # Overrides the multiplication function, and if the other object isn't a vector, it returns a scalar
    # Multiplication. Also checks size to allow for proper size.
    def __mul__(self, other):
        if type(other) == type(self):
            if other.len == self.len:
                dot = 0
                for i in range(self.len):
                    dot += self.vector[i]*other.vector[i]
                return dot
            else:
                return "Error - Invalid dimensions"
        elif type(other) == int:
            scaleVec = []
            for i in range(self.len):
                scaleVec.append(self.vector[i] * other)
            vector = Vector(scaleVec)
            return vector
        else:
            return "Error - Invalid operation"

    # r-functions in case the vector is the second value to a scalar
    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    # Override the equality and inequality
    def __eq__(self, other):
        if type(other) == type(self):
            if other.vector == self.vector:
                return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    # Return the returnable value through the string function to remove all quotes
    # Otherwise it returns the class type and a memory address
    def __repr__(self):
        return str(self.returnable)