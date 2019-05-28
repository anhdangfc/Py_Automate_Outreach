'''
READING AND WRITING FILES

- How to create, read, and save files to the hard drive
- filename and path
- Win: C:\., in Linux and OS: /
'''

## 1. Path in Win/Linux and OS
'''
The idea is to write the paht that would work in both Win, and OS/Linux
'''
import os
os.path.join('usr','bin','spam') ## in Win, would return the appropriate path for Win

## 2. Multiple file
myFiles = ['accounts.txt','details.csv','invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\anh.dang\\Documents\\Self_Learning\\Py_Automate\\Outputs', filename))

## 3. Current Working Directory
os.getcwd() ## current working directory
os.chdir(os.path.join(os.getcwd(), 'Outputs'))
os.getcwd()

## 4. Absolute and Relative Path
## . cwd
## .. parent of cwd
os.path.abspath('c:\\Users\\anh.dang\\Documents\\Self_Learning\\Py_Automate\\Outputs\\makedirs')
os.path.relpath('c:\\Users\\anh.dang\\Documents\\Self_Learning\\Py_Automate\\Outputs\\makedirs') ## use cwd as start
os.path.relpath('c:\\Users\\anh.dang\\Documents\\Self_Learning\\Py_Automate\\Outputs\\makedirs', \
    start='c:\\Users\\anh.dang\\Documents\\Self_Learning\\Py_Automate') ## give the start path

## 5. Create New Folders
os.makedirs('c:\\Users\\anh.dang\\Documents\\Self_Learning\\Py_Automate\\Outputs\\makedirs')


## 6. Contents
path = os.getcwd()

os.path.dirname(path) ## return string of everything that comes before the last slash
os.chdir(os.path.dirname(path))

os.path.basename(path) ## everything after the last slash in the path (cwd)
os.path.split(path) ## split to path and basename

path.split(os.path.sep) ## combine method split, with os.path.sep, for list of all folders in path


## 7. File size and Folder contents
path = os.getcwd() 
os.path.getsize(path) ## 4,096 bytes
os.listdir(path)

totalSize = 0
for file in os.listdir(os.getcwd()):
    size = os.path.getsize(os.path.join(os.getcwd(), file))
    totalSize += size
    print('Filename:{} - Size:{}'.format(file, size))

print('Total Size: {}'.format(totalSize))


## 8. Path Validity