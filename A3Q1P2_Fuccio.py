'''
Stephanie Fuccio
Engl 520
Assignment 3,Question 1, Program 2
This program uses the POS probability/frequency data from program 1 to provide POS predictions for user input.
'''
import re
import nltk, re, pprint
from nltk import word_tokenize
from nltk.util import ngrams
from nltk import *
import string
import itertools
from collections import OrderedDict
from operator import itemgetter
from A3Q1P1_Fuccio import tris #from A3Q1P1_Fuccio file- import tris (used in function below)

##################  I originally had the dictionary (below, variable "a") going to a text file. And it did successfully. However, when I opened the text file in program 2, all of the dictionary features were gone and it was very difficuult to use the string that it had become. I am painfully aware that calling this dictionary in program 2 missed the point of having this in 2 programs, but it is as close as I can get without going crazy. ###############################

def allinone(): #requests input, preprocesses input (append and tokenize), add input to list
    try:
        inputlist=[] #opens input list
        a=tris()#dictionary
        bigramlist=[] #create new list to store bigram TAG-WORD pairs
        valuelist=[] #creates value list -will merge bigramlist + this later into bigram_valuedict
        bigram_valuedict={}
        outputlist=[] #stores POS results as iteration goes on

    ############################################### Input handling #############################################

        inputhere=input("Enter something extraordinary: ")
        for c in string.punctuation:
            inputhere= inputhere.replace(c,"")
        token=nltk.word_tokenize(inputhere)
        inputlist.append("sBEGIN")
        for i in range(len(token)):
            inputlist.append(token[i])
        inputlist.append("sEND")
        print("\n","Here is your input tokenized: ", inputlist,"\n""\n")

    ############################################### Starts POS predicting ########################################

        for i in range(len(inputlist)): #print(inputlist[i]) #=sBEGIN Air for release tomorrow sEND

            #----------------- 1st round: <sBEGIN> <word1> ------------------#

            if inputlist[i] == "sBEGIN": #searches training data dictionary for TAG-WORD bigram from input
                for trigram in a.keys():#a is the dictionary
                    if (trigram[0])==inputlist[i] and (trigram[1])==inputlist[i+1]:
                        #trigram[0]=index 0 in training data dict trigram KEYS, trigram[1]=index 1 in training data dict KEYS
                        #print("trigram, freq",trigram,a[trigram]) #prints trigram,frequency

                        #adds these bits of info (temporarily) to these lists
                        bigramlist.append(trigram)#add bigram/trigram to list
                        valuelist.append(a[trigram]) #add value to list

                        #combines these lists into a dictionary
                        keys=bigramlist
                        values=valuelist
                        bigram_valuedict = {k: v for k, v in zip(keys, values)}

                        #orders dictionary by values (highest 1st)
                        sorted_dict = OrderedDict(sorted(bigram_valuedict.items(), key=itemgetter(1)))

                        #selects highest value AND picks TAG from the last part of this trigram
                        for trigram in sorted_dict.keys():#a is the dictionary
                            tv=trigram[2] #trigram[2] is the most freq POS for the TAG-WORD input pair-this is the SAME INDEX for all iterations of this task

                        #adds sBEGIN and 1st OUTPUT POS to outputlist
                        outputlist.append("sBEGIN")
                        outputlist.append(tv)#add 1st POS TAG to output list
                        #print("outputlist",outputlist)
                        break
            #----------------- all other rounds <previous TAG> <next word> -------------------------#
            else:
                #searches training data dictionary for next TAG-WORD bigram
                for trigram in a.keys():#a is the dictionary
                    if (trigram[0])==outputlist[1] and (trigram[1])==inputlist[i]:
                        #print(trigram,a[trigram]) #prints trigram, frequency

                        #clears old lists and dictionary so new info can be stored for this BIGRAM pair
                        bigramlist[:] = [] #clears old bigram list (make room for new bigram list)
                        valuelist[:] = [] #clears old value list
                        bigram_valuedict.clear() #clear dictionary

                        #adds new info to lists and dictionary
                        bigramlist.append(trigram)#add to list
                        valuelist.append(a[trigram]) #add to list
                        bigram_valuedict = {k: v for k, v in zip(keys, values)}
                        #print(bigram_valuedict)

                        #combines these lists into a dictionary
                        keys=bigramlist
                        values=valuelist
                        bigram_valuedict = {k: v for k, v in zip(keys, values)}

                        #orders dictionary by values (highest 1st)
                        sorted_dict = OrderedDict(sorted(bigram_valuedict.items(), key=itemgetter(1)))

                        #selects highest value AND picks TAG from the last part of this trigram
                        for trigram in sorted_dict.keys():#a is the dictionary
                            tv=trigram[2] #trigram[2] is the most freq POS for the TAG-WORD input pair

                        #adds OUTPUT POS to list
                        outputlist.append(tv) #add 1st POS TAG to output list
                        break

        print("And here are the POS tags:",outputlist)

    except:
        print("There has been an error. Go find coffee and try again in a few minutes.")

def main():

    allinone()

if __name__ == "__main__":

    main()

