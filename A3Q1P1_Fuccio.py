'''
Stephanie Fuccio
Engl 520
Assignment 3, Question 1, Program 1
This program uses a training data file to creates trigram probability estimates (in this case, frequencies) for POS tags.
This information will be used in program 2 to take input data from a user and show them POS tags for the words in input.
'''
import re
import nltk, re, pprint
from nltk import word_tokenize
from nltk.util import ngrams
from nltk import *
import string

def preprocessing():
    try:
        text =("A3_trainingdata.txt")
        text=open(text).read()
        text=re.sub(r'\n\s*\n',"sEND\nsBEGIN\n",text) #replaces blank line with "S_END > new line > S_BEGIN"
        text=re.sub(r'\s+'," ",text) #removed breaks so tokens appear in sentence form
        text=re.sub(r'sEND',"sEND\r\n\n",text)#puts breaks between sentences (easier to read)
        for c in string.punctuation:#most beautiful punc stripper known to man! (took care of 1.contractions, possessives, etc)
            text= text.replace(c,"")
        text2=open("A3_sentences.txt","w") #write training data to new file
        text2.write("sBEGIN")
        text2.write(text)
        text2.close()
    except:
        print("This file is unreadable. Please check the file name and try again. ""\n")
    #intentionally only want it to use this function right now (def tris() is called in program 2). See below for more info.


def tris():
    text2=("A3_sentences.txt")
    text2=open(text2).read()
    token=nltk.word_tokenize(text2)
    new_trigrams = []
    c = 0 #c is the index
    while c < len(token) - 2:
        new_trigrams.append((token[c], token[c+1], token[c+2]))
        c += 1 #this is how many token it skips (every one, every two, etc)-trying 1 now and will if loop for tag-word-tag combos only
    #FREQUENCY & DICTIONARY
    fdist = nltk.FreqDist(new_trigrams)
    freqdict={} #creates an empty dictionary
    for k,v in fdist.items():#frequency(value) for each trigram (key)
        freqdict[k]=v #adding keys, values to dictionary
        #print(freqdict)
    return freqdict
    #intentionally not using this function in this program. It is called in program 2.

##################  I originally had this dictionary going to a text file. And it did successfully. However, when I opened the text file in program 2, all of the dictionary features were gone and it was very difficuult to use the string that it had become. I am painfully aware that calling this dictionary in program 2 missed the point of having this in 2 programs, but it is as close as I can get without going crazy. ###############################

def main():

    preprocessing()

if __name__ == "__main__":

    main()
