
### (1) isX string methods are useful to validate user input
while True:
    print('Enter your Age:')
    age = input()
    if age.isdecimal():
        break
    print('Age should be a number')

while True:
    print('Enter your password (only numbers and letters):')
    pwd = input()
    if pwd.isalnum():
        break
    print('Password should contain only letters and numbers')

### Other methods: .start_with(), .end_with()


### (2) .join() and .split()
print('-'.join(['123','456','789']))

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob''' 
print(spam.split('\n'))


### (3) justifying 
def printPinic(pinicItems, leftWidth, rightWidth):
    print('PINIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in pinicItems.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth, '.'))

pinicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPinic(pinicItems, 10, 10)


### (4) Remove Whitespace
'   hello '.strip()
'----- today'.strip('-')


### (5) pyperclip
import pyperclip
# Copy something outside
pyperclip.paste()
pyperclip.copy('This is from pyperclip')
# Paste it some where else

