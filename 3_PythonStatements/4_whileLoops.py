# While loops will continue to execute a block of code while some condition remain true.
# For example , while my pool is not full , keep filling my pool with water.
# Or While my dogs are still hungry, keep feeding my dogs.

'''
x = 0
while x < 5:
    print(f'The current value of x is {x}')
    #x = x +1
    x += 1
else:
    print('X is not less than 5')

'''

# Break , Continue and Pass
#   We can use break, continue and pass statements in our loops to add additional functionality for various cases. 
#   The three statements are defined by:

# break:    Breaks out of the current closest enclosing loop.
# continue: Goes to the top of the closest enclosing loop.
# pass:     Does nothing at all.

'''
x = [1,2,3]

for item in x:
    pass
print('end of my script')

'''

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        break    # can be use break or continue
    print(letter)
