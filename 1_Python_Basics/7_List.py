cat_names = []
while True:
    print('Enter the name of cat ' + str(len(cat_names) + 1) +
          '(or Enter nothing to stop)')
    name = input()
    if name == '':
        break
    else:
        cat_names = cat_names + [name]

print('The cat names are:')
for name in cat_names:
    print(' ' + name)
