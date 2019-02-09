#Lab #3
#Due Date: 01/25/2019, 11:59PM
########################################
#
# Name: Hunter Schuler
# Collaboration Statement: Neither sought nor gave any help
#
########################################


def countWords(document):
    # First test to make sure the input is a string, otherwise return an error
    if type(document) == str:
        # Remove all new line characters from the provided string and separate all words into a list
        docWords = document.replace('\n',' ').split(' ')
        # Iterate through every word on the list
        for i in range(len(docWords)):
            # If the word contains a hyphen, it is most likely a contraction so do nothing
            # Otherwise, remove all symbols and anything non-alpha
            if "'" in docWords[i]:
                pass
            else:
                docWords[i] = ''.join(filter(str.isalpha, docWords[i]))
            # Convert every word to lower case to avoid confusion
            docWords[i] = docWords[i].lower()
        # Remove all empty strings left over from filtering symbol only strings
        docWords = filter(None, docWords)
        # Prepare a dictionary to store the return value
        words = {}
        # If the word exists in the dictionary, increase it, otherwise create an value for it in the dicitonary
        for word in docWords:
            if word in words.keys():
                words[word] += 1
            else:
                words[word] = 1
        return words
    else:
        return 'error'

def studentGrades(gradeList):
    # Check that the type is a list
    if type(gradeList) == list:
        # Initialize all of the variables to calculate the averages
        sum = 0
        count = 0
        averages = []
        # Iterate through the first dimension of the array, starting at element 1
        # since element 0 is a descriptive array
        for student in range(1, len(gradeList)):
            # Iterate through the second dimension, again skipping the 0th element
            for grade in range(1, len(gradeList[student])):
                # Calculate the sum and count to calculate avarage
                sum += gradeList[student][grade]
                count += 1
            # Add each average to the list of averages
            averages.append(int(sum / count))
            # Reset average calculating variables for each student
            sum = 0
            count = 0
        return averages
    else:
        return 'error'