
'''
The beauty of Dictionary is that it could enable the user to slice the data by index,
which is much more natural than the numbering order of list.
Very basic example about database
'''

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('No info for ' + name + ' in Database')
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

