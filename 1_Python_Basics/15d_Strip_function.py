#! python3
# 15d_Strip_function.py - Remove whitespace/specific character from the beginning and ending of string

import re

# '  Hello '.strip() ## the method to mimic
def strip(string, char = ' '):
    regex1 = f'^[{char}]+' ## at the begin
    regex2 = f'[{char}]+$' ## at the end
    stripPattern1 = re.compile(regex1)
    stripPattern2 = re.compile(regex2)
    string = stripPattern1.sub('',string)
    string = stripPattern2.sub('',string)
    return string

# test
strip('   Hello     ')
strip('----MAD----','-')