'''
Stephanie Fuccio
Engl 520
Assignment 5, Question 2
This program takes user input, uses POS tagging AND a set of pattern matching grammar rules to identify noun and preposition phrases. The output displays these two types of phrases one per line.
'''
import nltk, re
from nltk import word_tokenize
import string

def tag_me(): #change to input before submitting
    text=input("Enter a sentence to see the noun and prepositional phrases there are: ")
    print("")
    if len(text)>2: #checks that the input is long enough to use, 2 words
        text=nltk.word_tokenize(text) #tokenized input
        text=nltk.pos_tag(text) #POS tags input
        print("Here is your input split into words WITH each word's part of speech: ")
        print(text)
        print("")
        print("And here is each noun phrase AND prepositional phrase-one phrase per line:")
        return text
    else:
        print("\n""Stop wasting my time and type something we can work with! ")
def par():
    text=tag_me()
    if text==0:#here is the set of grammar rules for the task
        print("Tisk, tisk, this is too short to do anything with. Perhaps this video will inspire you: https://www.youtube.com/watch?v=PKIpCPS-oZc")
    else:
        grammar = r"""
          NP:
            {<DT><WP><VBP>*<RB>*<VBN><IN><NN>}
            {<NN|NNS|NNP|NNPS><IN>*<NN|NNS|NNP|NNPS>+}
            {<JJ>*<NNS|NNP|NNPS><CC>*<NN|NNS|NNP|NNPS>+}
            {<JJ>*<NN|NNS|NNP|NNPS>+}
            {<NN><CC><NN|PRP>}
            {<DT|PP\$>?<JJ>*<NN>}
            {<NNP>+}
            {<NN>+|<PRP>+}
            {<PRP>}
            {<NN>|<PRP><NN>}
            {<NN><ADJ><NN>}
            {<NNP>*<CONJ>*<NN|PRP|NNP>}
            {<DT><N>}
            {<NNP><CC><PRP>}
          PP:
            {<IN><NP>}
            {<IN><DT><NP>}
            {<IN>*<NN>}
          """
        cp = nltk.RegexpParser(grammar) #breaks down rules
        result = cp.parse(text) #parses the text using the above grammar
        noun_phrase = list(result.subtrees(filter=lambda x: x.label()=='NP')) #identifies noun phrases
        prepositional_phrase = list(result.subtrees(filter=lambda x: x.label()=='PP')) #identifies prep phrases
        for i in noun_phrase:#loops through text, looking for noun phrases-prints them
            print(i)
        for i in prepositional_phrase:#loops through text, looking for prep phrases-prints them
            print (i)
def main():
    par()
if __name__ == "__main__":
    main()
