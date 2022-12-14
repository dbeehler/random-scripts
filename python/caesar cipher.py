from base64 import decode
from operator import index, indexOf
from nltk.corpus import words 
import string

#Dusty Beehler September 2022
#Caesar cipher encode and decoder
#Encodes using a defined shift
#Decodes by decoding all possible strings incrementing by -1
#Assigns a score to each string for each English word found
#Prints highest score, or if there are multiple found it would print that as well, but most times it would just be one

alpha = list(string.ascii_lowercase)
alpha += " "
inputEnDe = int(input("Enter 1 for encode. 2 for decode: "))
wordList = words.words()

def encodeWord(word, shift):
    finalString = ""
    for char in word:
        indexOfChar = alpha.index(char)
        if indexOfChar == 26:
            finalString+=" "
        elif indexOfChar+shift>25:
            remainder = abs(len(alpha)-shift-indexOfChar-1)
            finalString+=alpha[remainder]
        else:
            finalString+=alpha[indexOfChar+shift]
    return finalString

def decodeWord(word):
    decodedStrings = []
    englishScore = []
    shift = -1
    for let in alpha:
        decodedWord = ""
        for char in word:
            indexOfChar = alpha.index(char)
            if indexOfChar == 26:
                decodedWord+=" "
            elif indexOfChar+shift < 0:
                remainder = len(alpha)-abs(indexOfChar+shift-1)
                decodedWord+=alpha[remainder]
            else:
                decodedWord+=alpha[indexOfChar+shift]
        shift=shift-1
        decodedStrings.append(decodedWord)

    for strings in decodedStrings:
        score = 0
        stringToCheck = strings.split()
        for word in stringToCheck:
            if word in wordList:
                score+=1
        englishScore.append(score)

    highest = 0
    wordToDisplay = ""
    for scores in englishScore:
        if scores > highest:
            highest = scores
            wordToDisplay = decodedStrings[englishScore.index(scores)]
        if scores > 3:
            print("this phrase may match: " + wordToDisplay)

if inputEnDe == 1:  
    inputString = input("Enter a string to encode: ")
    shiftNum = int(input("Enter a number to shift: "))
    print(encodeWord(inputString,shiftNum))
else:
    inputString = input("Enter encoded text to decipher: ")
    print(decodeWord(inputString))