#! python3
# 13b_pw.py - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip

if len(sys.argv) < 2: ## this one take the sys.argv, taking when you put the below code on cmd
    print('Hello World')
    print('Usage: python 13b_pw.py [account] - copy account password') ## this contents in cmd (set the cd to the path of your py file)
    exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for {} copied to clipboard.'.format(account))
else:
    print('There is no account named {}'.format(account))

