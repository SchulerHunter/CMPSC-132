#Lab #2
#Due Date: 01/25/2019, 11:59PM
########################################
#
# Name: Hunter Schuler
# Collaboration Statement: Neither sought nor gave any help
#
########################################


def joinedList(n):
    # Verity input integrity
    if type(n) == int:
        # Create a list to store the numbers
        NumList = []
        # Check if n is positive or negative
        if n > 0:
            i = 0
            # Loop from 1 to the number provided, appending second to receive the higher number
            while i < n:
                i += 1
                NumList.append(i)
            # Loop from n back to 1, appending first. This create the duplicate of n
            while i >= 1:
                NumList.append(i)
                i -= 1
        elif n < 0:
            i = n - 1
            # Loop from n to -1 using the same logic as above
            while i < -1:
                i += 1
                NumList.append(i)
            while i >= n:
                NumList.append(i)
                i -= 1
        return NumList
    else:
        return 'error'


def removePunctuation(txt):
    # Check validity of input
    if type(txt) == str:
        # Convert the text to a list
        textList = list(txt)
        # Loop through the length of the list
        for i in range(len(textList)):
            # Check each character to see if it is alpha only, otherwise replace it with a space
            if not str.isalpha(textList[i]):
                textList[i] = ' '
        # Join the whole list back into a string and return it
        txt = ''.join(textList)
        return txt
    else:
        return 'error'