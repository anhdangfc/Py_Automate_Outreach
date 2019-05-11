print('Hello world!')
print('What is your name?')    # ask for their name
myName = input()

if myName == 'Anh':
    print('Welcome Back Master, ' + myName)
else:
    print('Hi stranger, it is good to meet you, ' + myName)

print('The length of your name is:')
print(len(myName))
print('What is your age?')    # ask for their age
myAge = input()


# Flow-Control: Condition
if int(myAge) < 20:
    print('Hi kid!')
elif int(myAge) < 30:
    print('Hi young-age!')
elif int(myAge) < 60:
    print('Hi middle-age!')
else:
    print('Hi old!')

print('You will be ' + str(int(myAge) + 1) + ' in a year.')

