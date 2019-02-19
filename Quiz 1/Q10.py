def countLetters(letter, text):
    count = 0
    for i in text:
        if letter == i:
            count = count + 1
    return count

print(countLetters('p', 'Penn State - PSU'))
