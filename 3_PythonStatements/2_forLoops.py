#   Many objects in Python are 'iterable' meaning we can iterate over every element in the object.
#   Such as every element in a list or every charecter in a string.
#   We can use for loops to execute a block of code for every iteration. 

#   The term iterable means you can 'iterate' over the object.
#   For example you can iterate over every charecter in a string , iterate over every item in a list , iterate over every 
#   key in a dictionary

mylist = [1,2,3,4,5,6,7,8,9,10]

'''
for a in mylist:
    print(a)


for num in mylist:
    if num % 2 ==0:
        print(num)
    else:
        print(f'odd numbers : {num}')

list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print(list_sum)



mystring = 'Hello World'
for letter in mystring:
    print(letter)


tup = (1,2,3)
for item in tup:
    print(item)



mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))

for item in mylist:
    print(item)

for a,b in mylist:
    print(a)

'''

d = {'k1':1,'k2':2,'k3':3}
for item in d.items():
    print(item)

for key,value in d.items():
    print(key)
    print(value)

