#!/usr/bin/env python3
import json
from difflib import get_close_matches
dictList = json.load(open("data.json"))


def define(w):
  if w in dictList:
    return dictList[w]
  else:
    matches = get_close_matches(w, dictList.keys(), n=3)
    for match in matches:
      answer = input("did you mean {0}? yes or no: ".format(match))
      if answer == "yes":
        return dictList[match]


def getWord():
      word = input("\nenter a word you would like to know the deff for: ")
      return word.lower()


def run():
  try:
    word = ""
    while(word != "!q"):
      word = getWord()
      deffinitions = define(word)
      if (deffinitions):
        print("\n"+word)
        for index, item in enumerate(deffinitions):
          print("{0}: {1}".format(index+1, item))
      else:
        print("\n this word does not exist in the dictionary \n ")
    print("quiting")
  except Exception as e:
    print(e)


run()
