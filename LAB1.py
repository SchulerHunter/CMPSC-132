# Lab #1
# Due Date: 01/11/2019, 11:59PM
########################################
#
# Name: Hunter Schuler
# Collaboration Statement: No collaboration
#
########################################


def sumSquares(aList):
    sum = 0.0  # Initialize a sum variable to hold total
    if type(aList) == list:  # Verify the supplied parameter is a list
        for i in range(len(aList)):  # iterate through the list
            # Use a try block for when a string is supplied with the list
            try:
                sum += float(aList[i]) ** 2  # Convert all items to floating point to include items like strings
            except ValueError:
                pass
        return sum
    else:
        return 'error'
