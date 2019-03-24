def quickSort(numList):
    '''
    >>> quickSort([3, 5, 4, 1, 2])
    [1, 2, 3, 4, 5]
    >>> quickSort([7,2,1])
    [1, 2, 7]
    >>> quickSort([1,1,1,1,1])
    [1, 1, 1, 1, 1]
    >>> quickSort([4,6,5,2,3])
    [2, 3, 4, 5, 6]
    >>> quickSort([4,6,5,2,3,3])
    [2, 3, 3, 4, 5, 6]

    >>> quickSort([10, 7, 8, 9, 1, 5])
    [1, 5, 7, 8, 9, 10]
    >>> quickSort([89,15,73,40,99,56,22,7,81,50])
    [7, 15, 22, 40, 50, 56, 73, 81, 89, 99]
    >>> quickSort([2,5,9,8,5])
    [2, 5, 5, 8, 9]
    >>> quickSort([3,4,1,6,9,10,12,23])
    [1, 3, 4, 6, 9, 10, 12, 23]
    >>> quickSort([1,2,3,4,5])
    [1, 2, 3, 4, 5]
    >>> quickSort([])
    []
    >>> quickSort([1,0,-1,-3,2])
    [-3, -1, 0, 1, 2]
    '''
    n=len(numList)
    if n<=1:
        return numList
    # Set pivot to end of list and reassign right to before the pivot
    x, left, right = numList[n-1], 0, n-2
    # Loop until left is greater than pivot
    while left<=right:
        if numList[left]<=x:
            left+=1
        else:
            # Check if left is greater than pivot, then if right is less than pivot
            if numList[right]<=x:
                numList[left], numList[right] = numList[right], numList[left]
            right -=1
    numList[left], numList[n-1] = numList[n-1], numList[left]
    # Recursively reassign the list values
    numList[:left] = quickSort(numList[:left])
    numList[left+1:] = quickSort(numList[left+1:])
    return numList

    '''
    Question 1:
    No, the quicksort is not properly implemented. The program does not decrement the right
    until a value less than pivot is found. Along with this, the values from the recursive call 
    are not modifying the list, changing nothing for each sort. The search also doesn't run
    until the value of left is greater than right

    Question 2:
    When given the unsorted list [10, 7, 8, 9, 1, 5], the code fails.
    The code is corrected above along with new, more complex tests

    Question 3:
    The responsibility of the testing team is to test the code in all cases. Anything the user can do, they will do.
    The testing team works to assure complete functionality in the code before passing it on to completion.
    '''
