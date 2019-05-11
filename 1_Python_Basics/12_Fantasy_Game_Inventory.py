
## Nested Dictionaries and Lists

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
            'Bob': {'ham sandwiches': 3, 'apples': 2},
            'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(guests, item):
    numBrought = 0
    for k, v in guests.items(): ## g: key, i: items
        numBrought = numBrought + v.get(item, 0) ## get the value in i with key as string in item, if not return 
    return numBrought

### Test the function
print('Number of things being bought:')
print(' - Apples: {}'.format(str(total_brought(allGuests, 'apples'))))
print(' - Cups: {}'.format(str(total_brought(allGuests, 'cups'))))
print(' - Pretzels: {}'.format(str(total_brought(allGuests, 'pretzels'))))


## Practice: Fantasy Game 
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(in_list):
    print('Inventory:')
    total = 0
    for k, v in in_list.items():
        print('{} {}'.format(v, k))
        total += v
    print('Total number of items: {}'.format(total))

### Test:
displayInventory(inventory)


def addToInventory(in_list, add_list):
    for i in add_list:
        in_list[i] = in_list.setdefault(i, 0) + 1 ## setdefault would return the existing value in dict, if not exist, add one with the v of 0
    return(in_list)

### Test:
addedItems = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addedInventory = addToInventory(inventory, addedItems)
displayInventory(addedInventory)





