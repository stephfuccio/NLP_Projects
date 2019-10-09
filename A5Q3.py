'''
Stephanie Fuccio
Engl 520
Assignment 5, Question 3
This program takes a sentence input from the user and shows the following information:
1. Syntactic parse tree, 2. Number of NPs, 3. Average length of the NP, 4. Number of Verbs and 5. Number of Preposition Phrases in the sentence
'''
import nltk
from nltk.parse.stanford import StanfordParser
from nltk.tree import Tree
import pprint

def allinone():
    parser_folder=input("Input the Stanford Parser folder filepath: ")
    parser_jar = parser_folder + 'stanford-parser.jar'
    models_jar = parser_folder + 'stanford-parser-3.6.0-models.jar'
    const_parser = StanfordParser(parser_jar, models_jar)
    print("")
    text=input("Type a sentence of your choosing here: ")
    const_output = const_parser.raw_parse(text)
    print("")
    print("-------------------------------------SYNTACTIC PARSE of your sentence--------------------------------------")
    print("")
    for item in const_output:#accepts raw sentences (dont have to tokenize)
        print(item)
    print("")
    print("-----------------------------------------------------NOUN PHRASE INFO--------------------------------------")
    print("")
    noun_phrase = list(item.subtrees(filter=lambda x: x.label()=='NP')) #identifies noun phrases
    i=0
    NPLen=[]
    while i <len(noun_phrase):
        print("")
        print(noun_phrase[i])
        NPLen.append(len(noun_phrase[i]))
        i+=1
    print("")
    print("Number of noun phrases: ", i)
    #AVERAGE LENGTH OF NOUN PHRASES:
    avg=sum(NPLen)/i
    avg=round(avg, 2)
    print("")
    print("Average length of noun phrases: " ,avg)
    #VERB COUNTING
    verblist=[] #open a list to add diff very types to
    verb1 = list(item.subtrees(filter=lambda x: x.label()=='VB')) #identifies verb type 1
    i=0
    while i <len(verb1):
        verblist.append(i)
        i+=1
    verb2= list(item.subtrees(filter=lambda x: x.label()=='VBD')) #identifies verb type 2
    i=0
    while i <len(verb2):
        verblist.append(i)
        i+=1
    verb3 = list(item.subtrees(filter=lambda x: x.label()=='VBP')) #identifies verb type 3
    i=0
    while i <len(verb3):
        verblist.append(i)
        i+=1
    verb4 = list(item.subtrees(filter=lambda x: x.label()=='VBG')) #identifies verb type 4
    i=0
    while i <len(verb4):
        verblist.append(i)
        i+=1
    verb5 = list(item.subtrees(filter=lambda x: x.label()=='VBN')) #identifies verb type 5
    i=0
    while i <len(verb5):
        verblist.append(i)
        i+=1
    verb6 = list(item.subtrees(filter=lambda x: x.label()=='VBZ')) #identifies verb type 6
    i=0
    while i <len(verb6):
        verblist.append(i)
        i+=1
    print("")
    print("-----------------------------------------------VERB INFO---------------------------------------------------")
    print("")
    print("Number of verbs: ", len(verblist))
    print("-----------------------------------------PREPOSITIONAL PHRASE INFO-----------------------------------------")
    print("")
    prep_phrases = list(item.subtrees(filter=lambda x: x.label()=='PP'))
    i=0
    PPLen=[]
    while i <len(prep_phrases):
        print("")
        PPLen.append(len(prep_phrases[i]))
        i+=1
    print("")
    print("Number of prepositional phrases: ", i)
    print("-----------------------------------------------------------------------------------------------------------")
    print("")
    print("Thank you for using this Stephized Stanford Parsing Program.")

def main():
    allinone()
if __name__ == "__main__":
    main()


