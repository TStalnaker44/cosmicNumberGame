"""
Author: Trevor Stalnaker
File: magicNumber

A program that runs calculations for the classic Cosmic Number game.
"""

import inflect

engine = inflect.engine()

def getValue(num):
    words = engine.number_to_words(num)
    formatted = words.replace("minus","negative")
    formatted = formatted.replace(" ","")
    print("%s is %s" % (num,len(formatted)))
    if len(formatted) == 4:
        print("4 is the cosmic number!")
    else:
        return getValue(len(formatted))

while True:
    num = float(input("Number: "))
    getValue(num)
    again = input("Again? (Y/N)")
    if again.lower() == "n":
        break
