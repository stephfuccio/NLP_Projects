'''
Engl 520
Stephanie Fuccio
Assignment 2-Question 2
Question 2
This program identifies date expressions from a user .txt file and lists them together in the output statements.
'''
import re

def whatdate():
    datefile =input("Enter a .txt filepath here:  " )
    try:
        dates=open(datefile).read()
        dates1=re.findall(r'\d{1,2}.\d{1,2}.\d{4}',dates) #finds ['15-3-2016', '10-15-2016', '15/8/2016', '6/15/2016', '15 2016']
        #without the {1,2} delimiter, it was showing partial dates in wrong format, Ex: '15 2016', '20,2015'
        dates2=re.findall(r'\d+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\d+',dates) #26Jan2016
        dates3=re.findall(r'[0-9]+(?:st|nd|rd|th)\D[a-z]+\D(?:January|February|March|April|May|June|July|August|September|October|November|December)',dates)
        dates4=re.findall(r'[0-9]+(?:st|nd|rd|th)\D[a-z]+\D(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+[0-9]+',dates)
        dates5=re.findall(r'[?:January|February|March|April|May|June|July|August|September|October|November|December]+\s+[0-9]+\,\s+[0-9]+',dates)

        print("\n""Here are some numeric dates in your text:",dates1,"\n")
        print("And some abbreviated month dates: ",dates2,"\n")
        print("How about European date order with full month names: ",dates3,"\n")
        print("Oh, let's not forget the year! ",dates4,"\n")
        print("And last but not least, full form American style:",dates5,"\n")

    except:
        print("There has been an error. Did you type in a date OR some other form of text? ""\n")
        print("To see some examples of date formats globally, click on this link >>>: https://en.wikipedia.org/wiki/Date_format_by_country")
        exit()

def main():
    whatdate()

if __name__ == "__main__":
    main()
