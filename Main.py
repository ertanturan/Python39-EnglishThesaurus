import json
from difflib import get_close_matches

dataPath = "Data/data.json"
data = json.load(open(dataPath))

def printData(wordList):
    if type(wordList)==list:
        for item in wordList:
            print(item)


def translateWord(word):
    if IsDataContainsWord(word.lower()):
        printData(data[word])
    elif IsDataContainsWord(word.title()):
        printData(data[word.title()])
    elif IsDataContainsWord(word.upper()):
        printData(data[word.upper()])
    elif not IsDataContainsWord(word):
        GetClosestMatches(word)



def IsDataContainsWord(word):
    isContains = word in data
    return isContains


def GetClosestMatches(word):
    closestMatches = get_close_matches(word, data.keys(),cutoff=0.8)
    if len(closestMatches) > 0:
        DidYouMean(closestMatches[0])
    else:
        print("The word doesn't exist. Please check it and re-run")


def DidYouMean(word):
    user_input = input(f"The word you entered couldn't be found. Did you mean {word} ? (y/n) : ")
    user_input = user_input.lower()
    if user_input=="y":
        translateWord(word)
    elif user_input=="n":

        exit(0)
    else:
        print("Didn't understand you... PLease retry ")
        DidYouMean(word)



def askUserForWordInput():
    word = input("Enter word: ")


    translateWord(word)


askUserForWordInput()




