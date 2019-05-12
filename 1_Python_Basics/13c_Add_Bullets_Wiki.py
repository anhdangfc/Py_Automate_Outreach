#! python3
# 13c_Add_Bullets_Wiki.py - Adds Wikiperdia bullet points to the start
# of each line of text on the clipboards

'''
Create a bulleted list by putting each list item on its own line and placing a star in front.
Copy any list from Wikipedia
'''

import pyperclip

text = pyperclip.paste() ## take this from the clipboard

textSplit = text.split('\n')
output = '* ' + '\n* '.join(textSplit) ## add * for the first, and join by \n* following items

pyperclip.copy(output) ## copy the output after adjustments
print('Done! The added bullets Wiki is on your clipboard')