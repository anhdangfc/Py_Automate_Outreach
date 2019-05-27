'''
READING AND WRITING FILES

1. Open and return a File object
2. Read / Write on the File object
3. Close a file

'''

import os
cwd_path = os.getcwd()
output_path = os.path.join(cwd_path, 'Outputs')


## 1. Open a file
helloFile = open(os.path.join(output_path, 'hello.txt')) ## File object

os.chdir(output_path)
poemFile = open('poem.txt')

## 2. Read the contents of the file
helloContent = helloFile.read()
poemLines = poemFile.readlines() ## return a list with each lines

## 3. Write a file
helloFile2 = open('hello2.txt', 'w') ## 'w': Write mode
helloFile2.write('How are you?\n') ## over-write
helloFile2.close()

helloFile2 = open('hello2.txt', 'a') ## 'a': append
helloFile2.write('I am fine!')
helloFile2.close()

### Check
helloFile2 = open('hello2.txt')
content = helloFile2.read()
helloFile2.close()
print(content)


## 4. Saving Variables with the shelve Module
'''The idea is to take the variables and outsource into other Py program'''
cwdPathOutsouce = os.getcwd() ## for example, the cwd

### Use module shelve to save things/data
import shelve
shelfFile = shelve.open('shelfFile')
shelfFile['cwdPathOutsource'] = cwdPathOutsouce
shelfFile.close()

### To open it
shelfFile = shelve.open('shelfFile')
type(shelfFile)
shelfFile['cwdPathOutsource'] ## recall it
list(shelfFile.keys()) ## organize as dictionary
list(shelfFile.values())
shelfFile.close()

### pprint.pformat()
'''There is another way to save variables by creating a .py file
rather than using shelve module. As a text file, anyone can modify it, 
but only for basic data types: integers, floats, strings, lists, dict.'''

import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
fileObj = open('writecode_pprint.py','w')
fileObj.write('cats = {}\n'.format(pprint.pformat(cats)))
fileObj.close()

### Call
import writecode_pprint
writecode_pprint.cats
writecode_pprint.cats[0]
writecode_pprint.cats[0]['name']