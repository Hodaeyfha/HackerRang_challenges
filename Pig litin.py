'''
Pig Latin is a game of alterations played on the English language game.
To create the Pig Latin form of an English word
the initial consonant sound is transposed to the end of the word and an ay is affixed
(Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.

'''

def pig_letin():
    input_word = str(input("Input sentenc : ")).split()

    for word in input_word:
        print(word[1:] + word[:1] +'ay' , end='')

    print()
pig_letin()

