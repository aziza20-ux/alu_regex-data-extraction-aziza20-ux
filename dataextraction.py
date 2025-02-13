#!/usr/bin/python3
import re

# patterns to extract the desired datatypes
REGEX_RULES = {
    "Emails": re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"),
    "URLs": re.compile(r"https?:\/\/[\w.-]+\.[a-zA-Z]{2,6}(\/[\w.-]*)*\/?"),
    "Phone Numbers": re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"),
    "Credit Card Numbers": re.compile(r"\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}"),
}
# a function which uses patterns to find match and extract the datatypes
def filter_data(text):
    filter_data = {}
    for key, pattern in REGEX_RULES.items():
        filter_data[key] = pattern.findall(text)  
    return filter_data
# the main to run the function
if __name__ == "__main__":
    # a sampletext to test against our function
    sample_text = """
    user@example.com
    firstname.lastname@company.co.uk
    https://www.example.comLinks 
    http://subdomain.example.org/pageLinks 
    (123) 456-7890
    123-456-7890
    123.456.7890
    1234 5678 9012 3456
    1234-5678-9012-3456
    """
    # calls filter_data function to extract our patterns

    results = filter_data(sample_text)
    # loops through sampletext to extract the matches
    for category, matches in results.items():
        print(f"{category}: {matches}")
