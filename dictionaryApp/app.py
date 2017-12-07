#!/usr/bin/env python3
import json
from difflib import get_close_matches
dictList = json.load(open("data.json"))

#gets a word from users imput
def getWord():
      word = input("\nenter a word you would like to know the deff for: ")
      return word

#defines a word baised on the attached json dictionary
def define(w):
  if w in dictList:
    return (w, dictList[w])
  else:
    matches = get_close_matches(w, dictList.keys(), n=3)
    for match in matches:
      answer = input("did you mean {0}? yes or no: ".format(match))
      if answer == "yes":
        return (match, dictList[match])

#prints the word deffinition in a user friendly way
def printWord(d):
  if (d):
    print("\n"+ d[0])
    for index, item in enumerate(d[1]):
      print("{0}: {1}".format(index+1, item))
  else:
    print("\n this word does not exist in the dictionary \n ")

#runs the code in a loop for usability
def run():
  try:
    word = ""
    while(word != "!q"):
      word = getWord()
      deffinitions = define(word)
      printWord(deffinitions)
    print("quiting")
  except Exception as e:
    print(e)


run()
