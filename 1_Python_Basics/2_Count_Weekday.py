# While Loop Statement
count = 0
days_in_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
while count < 7:  # keep looping when the condition is still True
    print(days_in_week[count])
    count += 1
print()

# For loop
for d in days_in_week:
    print('Today is ' + d)
    if d == 'Friday':
        print('TGIF')
        break



