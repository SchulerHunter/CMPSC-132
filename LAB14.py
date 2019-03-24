#LAB 14
#Due Date: 04/05/2019, 11:59PM
########################################
#
# Name: Hunter Schuler
# Collaboration Statement: Neither sought nor gave assistance
#
########################################

def bubbleSort(numList):
    # Initialize a count variable, a dictionary, and a bool to confirm if the list is sorted
    steps = {}
    sorted = False
    step = 0
    # While the array is't sorted, loop through the list and compare the current value to the next
    # If the current value is greater, swap the two and flag as swapped
    # If the swap flag isn't raised, the list is sorted and everything can be returned
    while not sorted:
        step += 1
        for i in range(len(numList) - 1):
            if numList[i] > numList[i + 1]:
                numList[i], numList[i+1] = numList[i+1], numList[i]
                swap = True
        steps[step] = numList.copy()
        if swap == False:
            sorted = True
        swap = False
    return (steps, numList)
