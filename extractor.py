#!/usr/bin/python3

#the regex library
import re
#the dictionary to hold regex rules
patterns = {
    "email": r'[a-zA-Z0-9.%_+]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    "url": r'https?://[^\s/$.?#].[^\s]*',
    "phonenumber": r'\(?\d{3}\)?[\s\-.]?\d{3}[\s\-.]?\d{4}',
    "creditcard":r'\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}'

 }
 #the function to apply regex rules on the text and extract the desired datatypes
def data_validator(text):
   for key, value in patterns.items():
     extracted =  re.findall(value, text, re.MULTILINE)
     print(f"Your {key} is {extracted} you did it!!!!")
# sample text
if __name__ == "__main__":
   sampletext = """
   user@example.com
   firstname.lastname@company.co.uk
   https://www.example.comLinks to an external site.
   http://subdomain.example.org/pageLinks to an external site.
   (123) 456-7890
   123-456-7890
   123.456.7890
   1234 5678 9012 3456
   1234-5678-9012-3456
   """
   #the call of function data_validator
   data_validator(sampletext)
