import pprint as pretty

message = 'This is a silly way to do word count but it will help you to understand well the concept'
# First create a empty dict
count = {}
for char in message:
    count.setdefault(char, 0)  # setdefault() to prevent the error, if that key has not existed, add one with zero value
    count[char] += 1

#pretty.pprint(count)
print(pretty.pformat(count))