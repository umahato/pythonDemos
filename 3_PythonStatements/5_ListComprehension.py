#   List Comprehensions are unique way of quickly creating a list with Python.
#   If you find yourself usig a a for loop along with .append() to create a list,
#   List Comprehensions are good alternative

'''
mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)
'''

# alternate way.
mystring = 'hello'
mylist = [letter for letter in mystring]
print(mylist)

mylist = [x for x in 'abcde']
print(mylist)

mylist2 = [num for num in range(0,11)]
print(mylist2)

mylist3 = [num**2 for num in range(0,11)]
print(mylist3)

mylist4 = [x for x in range(0,11) if x%2 ==0]
print(mylist4)

celcius = [0,10,20,30.4]
fahrenheit = [((9/5)* temp + 32) for temp in celcius]
print(fahrenheit)

# alternate
fahrenheit2 = []
for temp in celcius:
    fahrenheit2.append(((9/5)*temp + 32))
print(fahrenheit2)