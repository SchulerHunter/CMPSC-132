#LAB 15
#Due Date: 04/05/2019, 11:59PM
########################################
#
# Name: Hunter Schuler
# Collaboration Statement: Neither sought nor gave assistance
#
########################################


def merge(list1, list2):
    result = []
    i = 0
    j = 0
    # Compare each element in the lists until a max in one list is reached
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    # After a max is reached, add the rest of the elements from the other list
    if i < len(list1):
        for k in range(len(list1[i:])):
            result.append(list1[k+i])
    else:
        for k in range(len(list2[j:])):
            result.append(list2[k+j])
    return result

def mergeSort(numList):
    # If the list has a length of 0 or 1, return the array
    if len(numList) < 2:
        return numList
    # Calculate the middle
    middle = len(numList) // 2
    # Recursively reassign the left half, with each redefinition being sorted
    leftHalf = mergeSort(numList[:middle])
    rightHalf = mergeSort(numList[middle:])
    # Return the final merge of two sorted halfs of the original list
    return merge(leftHalf, rightHalf)
