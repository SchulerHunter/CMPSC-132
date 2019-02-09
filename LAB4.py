#Lab #4
#Due Date: 02/01/2019, 11:59PM
########################################
#
# Name: Hunter Schuler
# Collaboration Statement: Neither sought nor gave any help
#
########################################


def encrypt(message, key):
    # Verify the inputs
    if type(message) == str:
        if type(key) == int:
            # Create a dictionary containing a numerical value for all upper and lower case letters
            values = dict()
            for i in range(ord('A') - 64, ord('Z') - 63):
                values[i] = chr(i + 64)
            for i in range(ord('a') - 70, ord('z') - 69):
                values[i] = chr(i + 70)
            text = list(message)
            # Convert text to number
            for i in range(len(text)):
                if text[i].isupper():
                    text[i] = ord(text[i]) - 64
                elif text[i].islower():
                    text[i] = ord(text[i]) - 70
                else:
                    pass
            # Encrypt the text
            for i in range(len(text)):
                if type(text[i]) == int:
                    if text[i] < 27:
                        text[i] = (text[i] - 1 + key) % 26 + 1
                    else:
                        text[i] = (text[i] - 1 + key) % 26 + 27
                else:
                    pass
            # Convert numbers to text
            for i in range(len(text)):
                if type(text[i]) == int:
                    text[i] = values[text[i]]
                else:
                    pass
            # Convert the encrypted list back into a string and return it
            message = ''.join(text)
            return message
        else:
            return "error"
    else:
        return "error"


def decrypt(message, key):
    if type(message) == str:
        if type(key) == int:
            # Create a dictionary containing a numerical value for all upper and lower case letters
            values = dict()
            for i in range(ord('A') - 64, ord('Z') - 63):
                values[i] = chr(i + 64)
            for i in range(ord('a') - 70, ord('z') - 69):
                values[i] = chr(i + 70)
            text = list(message)
            # Convert text to number
            for i in range(len(text)):
                if text[i].isupper():
                    text[i] = ord(text[i]) - 64
                elif text[i].islower():
                    text[i] = ord(text[i]) - 70
                else:
                    pass
            # Decrypt the text
            for i in range(len(text)):
                if type(text[i]) == int:
                    if text[i] < 27:
                        text[i] = (text[i] - 1 - key) % 26 + 1
                    else:
                        text[i] = (text[i] - 1 - key) % 26 + 27
                else:
                    pass
            # Convert numbers to text
            for i in range(len(text)):
                if type(text[i]) == int:
                    text[i] = values[text[i]]
                else:
                    pass
            # Convert the encrypted list back into a string and return it
            message = ''.join(text)
            return message
        else:
            return "error"
    else:
        return "error"