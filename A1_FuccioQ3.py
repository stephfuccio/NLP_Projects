'''
Stephanie Fuccio
Engl 520
Assignment #1, Question 3: The Trigram Challenge
This code takes a .txt file as input, divides the text into trigrams (incl spaces as characters, as the instructions examples showed),
counts the frequency of said trigrams AND displays them in order of most frequent first, with their count.
'''
import re

def trigramfiesta():
    #takes input, reads it, removes punc, changes letters to lowercase
    text =input("To see a list of trigrams in a text in order of most frequent (with their counts) enter a file path here: ")
    try:
        text=open(text).read()
        text = re.sub(r'[^\w\s]','',text) #removes punc
        text = re.sub("\n","",text) #replaces line break with no space (nothing)
        text=text.lower()

        #makes trigram list (incl spaces)
        trigramlist=[]
        for i in range(len(text)-1):
            trigramlist.append(text[i:i+3])
            tris=trigramlist

        #creates dict of trigrams and their count (making sure NOT to duplicate counts)
        tridict = {}
        for char in tris:
            if char not in tridict.keys():
                tridict[char] = 1
            else:
                tridict[char] += 1

        #reverses dict order so that the highest count trigrams are first
        for k, v in sorted(tridict.items(), key=lambda kv: kv[1], reverse=True):
            print("%s => %s" % (k,v))
    except:
        print("You have not entered a viable file path. Please go get some coffee, come back and try again. Gracias.")

def main():
    trigramfiesta()

if __name__ == "__main__":
    main()


#/home/onyx/Desktop/Engl520/Code/A1_pastehere.txt
