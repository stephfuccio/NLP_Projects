'''
Stephanie Fuccio
Engl 520
Assignment #1, Question 2: Where are the Citations?
This code takes a .txt file as input & replaces all citations in the file with the word CITATION using regular expressions.It writes this to a new file.
There are 5 citation formats replaced with this code:
     1.(LastName, Year; LastName, Year) #line207,
     2.LastName and LastName (Year)
     3.LastName (Year)
     4.(LastName, Year)
     5.(LastName et al., Year) #there is ., between et al and Year in the sample text I took the in-text citations from. The . was missing from the output BUT was picking up on that pattern in texts with the ., citation (such as the Kessler article used as an example)

#Citations source:Kessler, etal 1998,"Automatic Detection of Text Genre", although the code should work on any .txt file with the above type of citations.
'''
import re,os

def citationfun():
    text=input("Would you like your in-text citations tagged for format checking purposes? Great! Enter your file path here: ")
    try:
        text=open(text).read()
        text=re.sub(r'\([A-Z][a-z]+,\s+[0-9]+;\s[A-Z][a-z]+\s[a-z]+\s[A-Z][a-z]+,\s[0-9]+\)', "CITATION1",text )
        #(Biber, 1995; Karlgren and Cutting, 1994)
        text=re.sub(r'[A-Z][a-z]+ and [A-Z][a-z]+,?\s\(\d{0,4}\S' ,"CITATION2",text) #Karlgren and Cutting (1994)
        text=re.sub(r'[A-Z][a-z]+,?\s\(\d{0,4}\S' ,"CITATION3",text) #Butcher (1932)
        text=re.sub(r'\([A-Z][a-z]+,\s+[0-9]+\)',"CITATION4",text) #(Nunberg, 1990)
        text=re.sub(r'\([A-Z][a-z]+ et al\.,\s+[0-9]+\)', "CITATION5", text)
        filepath2 = open("NewFilealaSteph.txt", "w")
        print("A new file has been created with your citation replacements.")
        print("The name of the file is NewFilealaSteph.")
        print("The five citations replaced were as follows:")
        print("CITATAION1 = (LastName, Year; LastName, Year)")
        print("CITATION2 = LastName and LastName (Year)")
        print("CITATION3 = LastName (Year)")
        print("CITATION4 = (LastName, Year)")
        print("CITATION5 = (LastName et al., Year)")
        print("I hope this information is useful for you.")
        filepath2.write(text)
        filepath2.close()

    except:
        print("That is not a good file path. Did your fingers slip on the keyboard? Please try again")
        exit()

def main():
    citationfun()

if __name__ == "__main__":
    main()
