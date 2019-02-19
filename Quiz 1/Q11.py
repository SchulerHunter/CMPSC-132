def myFunction(aList):
    for position in range(len(aList)):
        aList[position] = 2 * aList[position]
    return aList

num_list = [2, 5, 9]
print(myFunction(num_list))
