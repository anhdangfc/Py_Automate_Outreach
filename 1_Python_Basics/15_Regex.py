'''
PATTERN MatchedING WITH REGULAR EXPRESSIONS
'''

import re

## (1) Basic structure of RegEx from re module
dateUnderScore = re.compile(r'\d\d_\d\d_\d\d\d\d') ## \ is for exit, so put r outside
mo = dateUnderScore.search('I name a file as today_file_12_05_2019')

print('Matched pattern: '+ mo.group())


## (1.1) Grouping by parentheses
dateUnderScore = re.compile(r'(\d\d)_(\d\d)_(\d\d\d\d)') ## \ is for exit, so put r outside
mo = dateUnderScore.search('I name a file as today_file_12_05_2019')

print('Matched pattern (Group 1 - Date): '+ mo.group(1))
print('Matched pattern (Group 2 - Month): '+ mo.group(2))
print('Matched pattern (Group 3 - Year): '+ mo.group(3))
print('Matched pattern (Group 0 - All): '+ mo.group(0))
print('Matched pattern (All): '+ mo.group())

date, month, year = mo.groups() ## using .groups() method
print(date)
print(month)
print(year)


## (1.2) When you mean () as a character (rather than special meaning)
## add backslash \( <str> \), as well as | ? * + and other special characters
dateUnderScore = re.compile(r'(\d\d)_(\(\d\d\))_(\d\d\d\d)') ## \ is for exit, so put r outside
mo = dateUnderScore.search('I name a file as today_file_12_(05)_2019')
print('Matched pattern: '+ mo.group())


## (1.3) Multiple groups with Pipe
heroPattern = re.compile(r'Batman|Iron Man|Spider Man') ## pipe
mo1 = heroPattern.search('My friend and me go to see Pikachu, Batman, Iron Man. It\'s fun')
mo2 = heroPattern.search('My friend and me go to see Pikachu, Iron Man, Batman. It\'s fun')
mo3 = heroPattern.findall('My friend and me go to see Pikachu, Iron Man, Batman. It\'s fun')

print('Matched Hero pattern: '+ mo1.group()) ## return the first occurence
print('Matched Hero pattern: '+ mo2.group()) 
print('Matched Hero pattern: '+ str(mo3)) ## return all

## use with () with same prefix
facebookProduct = re.compile(r'Face(book|time)')
mo = facebookProduct.search('Youtube, Google, Facebook, Medium, Netflix, Facetime')

print(mo.group())


## (1.4) Optional Matching with ?
businessPersonPattern = re.compile(r'business(wo)?man')
mo1 = businessPersonPattern.search('doctor, businessman, lawyer, businesswoman')
mo2 = businessPersonPattern.search('doctor, businesswoman, lawyer, businessman')
mo2 = businessPersonPattern.search('doctor, businesswowoman, lawyer'); mo3 == None

print(mo1.group())
print(mo2.group())


## (1.5) Matching 0+ with *
businessPersonPattern = re.compile(r'business(wo)*man')
mo0 = businessPersonPattern.search('doctor, businessman'); mo0 == None
mo1 = businessPersonPattern.search('doctor, businessman, lawyer, businesswoman')
mo2 = businessPersonPattern.search('doctor, businesswoman, lawyer, businessman')
mo3 = businessPersonPattern.search('doctor, businesswowowoman, lawyer, businessman')

print(mo1.group())
print(mo2.group())
print(mo3.group())


## (1.6) Matching 1+ with +
businessPersonPattern = re.compile(r'business(wo)+man')
mo1 = businessPersonPattern.search('doctor, businessman, lawyer')
mo2 = businessPersonPattern.search('doctor, businesswoman, lawyer, businessman')
mo3 = businessPersonPattern.search('doctor, businesswowowoman, lawyer, businessman')

print(mo1 == None)
print(mo2.group())
print(mo3.group())


## (1.7) Repetition with {}
hahaPattern = re.compile(r'(ha){2}')
laughBoundPattern = re.compile(r'(ha){3,5}')
laughUnboundPattern = re.compile(r'(ha){,5}')

mo1 = hahaPattern.search('And, I: ha'); print(mo1 == None)
mo2 = hahaPattern.search('And, I: haha'); print(mo2 == None)
mo3 = laughBoundPattern.search('And, I: haha'); print(mo3 == None)
mo4 = laughBoundPattern.search('And, I: hahaha'); print(mo4 == None)
mo5 = laughUnboundPattern.search('And, I: haha'); print(mo5 == None)


## (2) Greedy and Nongreedy Matching

## (3) .findall()
## (4) Character Classes
## (4b) Your own character classes
## (5) Caret and $
## (6) Wildcard
## (7) Case Insensitive
## (8) substitue
## (9) Complex Regexes
## (10) re.IGNORECASE, re.DOTALL, re.VERBOSE


