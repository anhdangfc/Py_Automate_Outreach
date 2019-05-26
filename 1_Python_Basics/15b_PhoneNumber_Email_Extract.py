#! python3
# 15b_PhoneNumber_Email_Extract.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re


## Phone number Regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    (\d{3})                       # first 3 digits
    (\s|-|\.)                     # separator
    (\d{4})                       # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', 
    re.VERBOSE) ## for complicated regex pattern, add re.VERBOSE to ignore new lines and comments inside the pattern


## Email Address Regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-0._%+-]+  # username
    @                  # at
    [a-zA-Z0-9.-]+     # domain 
    (\.[a-zA-Z]{2,4})  # dot-something (top-level domain)
)''', re.VERBOSE)


## Find match in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


## Copy the results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


# ## test
# print(emailRegex.search('This is the test: ma@fc.com').group())
# print(emailRegex.search('This is the test: ma@fc.com').group(2))
# t = phoneRegex.findall('This is the test: 800-420-7240 ext 56')