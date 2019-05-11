spam = {'color': 'red', 'age': 42}

print('This is by values')
for v in spam.values():
    print(v)

print()
print('This is for keys extracting')
for v in spam.keys():
    print(v)
    print(spam[v])

print()
print('This is to extract items')
for i in spam.items():
    print(i)

print()
print('The trick of multiple assignment')
for i, v in spam.items():
    print('The key is {0} and the value is {1}'.format(i, v))
