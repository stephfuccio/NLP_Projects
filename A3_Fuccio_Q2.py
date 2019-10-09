'''
Stephanie Fuccio
Engl 520
Assignment #3, Question 2:
This program takes input from the user and uses NLTK to add POS tags to the words. It continues to take input until the user types "quit."
'''
import nltk
from nltk import word_tokenize

def tagit():
    text=input("\n""Enter an English sentence to see the parts of speech (POS) for each word. " "\t")
    if len(text)==0:
        print("\n""Stop wasting my time and type something! ")
    else:
        try:
            text=nltk.word_tokenize(text)
            print("\n","Here are this are the words of your sentence with the part of speech (POS) after each word.")
            print("\n",nltk.pos_tag(text),"\n")
            print("Here are some common part of speech tags:(DT=determiner, NN=noun, VB=verb, PRP=personal pronoun) ""\n")
            print("If you need more POS tags, please go here: (https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)""\n")
            print("Or if you'd like a POS musical experience, go here: https://www.youtube.com/watch?v=lmNl7Mt48H8 ""\n" )
            more()
        except:
            print("Whatever you wrote just broke my computer. Thanks a lot! ")
            exit()

def more():
    keepgoing=input("Type another sentence OR type QUIT to stop. ""\t").lower()
    if keepgoing==("quit"):
        print("\n""Thank you for using the Stephized NLTK POS tagging program. ")
    else:
        tagit()

def main():
    tagit()

if __name__ == "__main__":
    main()
