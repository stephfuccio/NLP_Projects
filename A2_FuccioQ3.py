'''
Stephanie Fuccio
Engl 520
Assignment 2, Question 3
This program converts a last name into soundex representation.
Soundex: http://www.archives.gov/research/census/soundex.html
[1=B,F,P,V; 2=C,G,J,K,Q,S,X,Z; 3=D,T; 4=L; 5=M,N; 6=R]
Test names: Washington=W-252, Lee=L-000, Gutierrez=G-362, Pfister=P-236, Jackson=J-250, Tymczak=T-522, Ashcraft=A-261
'''
import re

def soundexfun():
    name =input("What's your last name? "   ) #requests input
    result = name[0].upper() #capitalizes 1st letter (even if inputted as lowercase)

    inputname = re.sub('[hw]', '', name) #replaces h's + w's with space-part of rule 4, what is "flags=re.I"????

    inputname = re.sub('[bfpv]+', '1', inputname) #next few lines replace the consonants in Soundex code with their Soundex #
    inputname  = re.sub('[cgjkqsxz]+', '2', inputname) #[] means OR for each char inside. Ex c OR g OR k
    inputname  = re.sub('[dt]+', '3', inputname) #+ means any number of times the char appears, Ex: r twice, 2 times, etc
    inputname  = re.sub('l+', '4', inputname)
    inputname  = re.sub('[mn]+', '5', inputname)
    inputname  = re.sub('r+', '6', inputname)

    #print(inputname) #a26a13,still has vowel "A"
    inputname  = inputname [1:] #removes 1st letter from string
    #print(inputname) #26a13 #removes "A" at beg of string but still has non-# "a" in middle of string

    inputname = re.sub('[aeiouy]','',inputname) #removes all vowels, needs to be here (not earlier)-it not, it will ruin spacing of letters with Soundex #.

    result += inputname [0:3] #adds CAP 1st letter (result) +  3 digits of new string

    if len(result) < 5: #Soundex codes should have 4 characters (1 letter + 3 numbers)
        result += '0'*(5-len(result)) #adding 0s if there are less than the 4 letters needed for Soundex code

    result=result[0]+"-"+result[1:4]
    print("\n""Here is your last name's Soundex code:",result,"\n")
    print("Read more about Soundex here:","http://www.archives.gov/research/census/soundex.html")

def main():
    soundexfun()

if __name__ == "__main__":
    main()

