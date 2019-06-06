from itertools import permutations
import time
from pytesser3 import *
from PIL import Image

def findword(letters, exceptionwords):
    f = open("scrabble.txt", "r")
    filetext = f.read()
    #print(filetext)
    perms = [''.join(p) for p in permutations(letters)]
    #print(perms)

    word = ''
    for possibleword in perms:
        for letteri in range(len(filetext)):
            if len(word) == 4:
                if possibleword == word:
                    if word not in exceptionwords:
                        return word

                lettercont = 0
                word = ''

            word += filetext[letteri]

    print('---no word found---')
    end = time.time()
    print(end - start)
    exit()
    return word


def firesequence(word, letters):
    letters = ''.join(letters)
    sequencelist = []
    i = 0
    while(i<4):
        idw = letters.find(word[i])
        if idw in sequencelist:
            l = list(letters)
            l[idw] = '0'
            letters = "".join(l)
            i -= 1
        else:
            sequencelist.append(idw)
        i += 1

    return [x+1 for x in sequencelist]

start = time.time()

letters = ['a', 'a', 'n', 'o']
print('Letters')
print(letters)


word = findword(letters, [''])
print('word -> ' + str(word))


sequencelist = firesequence(word, letters)
print(sequencelist)


end = time.time()
print(end - start)