#! python3
# 15c_StrongPassword.py - Detect a Strong Password

## 1. Contains at least 8 characters
## 2. Both uppercase + lowercase
## 3. At least 1 digit

import re, getpass
from prompt_toolkit import prompt

while True:
    # 1 - Input the password
    pwd = prompt('Enter your password to check how strong it is? \n', is_password=True)

    # 2 - Testing the condition of strong password
    eightCountRegex = re.compile(r'[A-Za-z0-9>_%+-]{8,}') # 1. Contains at least 8 characters
    upperCaseRegex = re.compile(r'[A-Z]{1,}') # 2a. At least 1 uppercase
    lowerCaseRegex = re.compile(r'[a-z]{1,}') # 2b. At least 1 lowercase
    digitRegex = re.compile(r'[0-9]{1,}') # 3. At least 1 digit

    if eightCountRegex.search(pwd) == None:
        print('- Not good Password: Should contain at least 8 characters')
  
    if (upperCaseRegex.search(pwd) == None) or (lowerCaseRegex.search(pwd) == None):
        print('- Not good Password: Should have both uppercase and lowercase')
 
    if digitRegex.search(pwd) == None:
        print('- Not good Password: Should have at least 1 digit')

    if eightCountRegex.search(pwd) != None and upperCaseRegex.search(pwd) != None and \
        lowerCaseRegex.search(pwd) != None and digitRegex.search(pwd) != None:
        print('The password is OK!')
        break




