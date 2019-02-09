#Lab #5
#Due Date: 02/08/2019, 11:59PM
########################################
#
# Name: Hunter Schuler
# Collaboration Statement: Neither sought nor gave assistance
#
########################################


class SodaMachine:
    # Create all the machine variables
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.stock = 0
        self.balance = 0

    # create a function named purchase that check all the parameters to
    # make sure a purchase is allow. Returns change if needed
    def purchase(self):
        if self.stock == 0:
            return 'Product out of stock'
        elif self.balance < self.price:
            return f'Please deposit ${self.price-self.balance}'
        elif self.balance > self.price and self.stock != 0:
            change = self.balance - self.price
            self.balance = 0
            self.stock -= 1
            return f'{self.product} dispensed, take your ${change}'
        else:
            self.balance = 0
            self.stock -= 1
            return f'{self.product} dispensed'

    # A function deposit to add chase to the machine
    # also checks to see if the amount added is an integer and
    # if there is stock in the machine
    def deposit(self, amount):
        if type(amount) == int:
            if self.stock > 0:
                self.balance += int(amount)
                return f'Balance: ${self.balance}'
            else:
                return f'Sorry, out of stock. Take your ${amount} back'
        else:
            return 'error'

    # A function to restock the machine. Checks that the amount is an integer
    def restock(self, amount):
        if type(amount) == int:
            self.stock += int(amount)
            return f'Current soda stock: {self.stock}'
        else:
            return 'error'


class Line:
    # Store each coordinate value as an int
    def __init__(self, coord1, coord2):
        self.x1 = coord1[0]
        self.y1 = coord1[1]
        self.x2 = coord2[0]
        self.y2 = coord2[1]

    # return a value using the distance formula
    @property
    def distance(self):
        return round(float(((self.x2 - self.x1)**2) + ((self.y2 - self.y1)**2))**.5, 3)

    # return the slop of the line using the slop formula
    # if the denominator is 0, the slope is infinity
    @property
    def slope(self):
        try:
            return round(float((self.y2 - self.y1)/(self.x2 - self.x1)), 3)
        except ZeroDivisionError:
            return 'Infinity'
