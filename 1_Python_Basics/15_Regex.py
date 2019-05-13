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
hahaPattern = re.compile(r'(ha){1,2}?') ## non-greedy add ? (return the shortest version)
mo4 = hahaPattern.search('And, I: hahaha'); print(mo4.group())


## (3) .findall()
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex_group = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups

phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
phoneNumRegex_group.findall('Cell: 415-555-9999 Work: 212-555-0000') # with group (return tuples)


## (4) Character Classes
xmasRegex = re.compile(r'\d+\s\w+') ## \d+: 1+ digits; \s: space; \w+: 1+ letters/words 
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 \\
swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')


## (4b) Your own character classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('Robocop eats baby food. BABY FOOD.')

consonantRegex = re.compile(r'[^aeiouAEIOU]') ## ^ after the bracket, search anything but ones in []
consonantRegex.findall('Robocop eats baby food. BABY FOOD.')


## (5) Caret and $
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890').group())
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('123 4567890') == None)


## (6) Wildcard
atRegex = re.compile(r'.at') ## . match any character except for a newline
atRegex.findall('The cat in the hat sat on the flat mat.')

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') ## .* match everything
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

greedyRegex = re.compile(r'<.*>') ## .* is greedy, it takes as long as possible
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

nongreedyRegex = re.compile(r'<.*?>') ## add ? for non-grredy
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

noNewlineRegex = re.compile('.*') ## anything except new line
noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \\
\nUphold the law.').group() ## everything up to the first \n

newlineRegex = re.compile('.*', re.DOTALL) ## add re.DOTALL, to also include new line
newlineRegex.search('Serve the public trust.\nProtect the innocent. \\


## (7) Case Insensitive
robocop = re.compile(r'robocop', re.I) ## IGNORECASE
robocop.search('Robocop is part man, part machine, all cop.').group()
robocop.search('ROBOCOP protects the innocent.').group()


## (8) substitue
namesRegex = re.compile(r'Agent \w+') ## Start with Agent then followed by Words (till space)
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

## (9) Complex Regexes
agentNamesRegex = re.compile(r'Agent (\w{2})\w*') ## n letters in group 1
## \1, \2, \3 to indicate the group in ( )
agentNamesRegex.sub(r'\1*****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', 
    re.VERBOSE) ## for complicated regex pattern, add re.VERBOSE to ignore new lines and comments inside the pattern


## (10) re.IGNORECASE, re.DOTALL, re.VERBOSE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)


