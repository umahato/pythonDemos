'''
def myfunc(a,b):
    #Return 5% of the sum of a and b
    return sum((a,b)) * 0.05

print(myfunc(40,60))



def myfunc(*args):
    return sum(args) * 0.05

print(myfunc(34,53,53))



def myfunc (**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choise is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
    
print(myfunc(fruit='apple'))


# Define a function called myfunc that takes in an arbitrary number of arguments, and return a list containing
# only those arguments that are even

def myfunc(*args):
    return [x for x in args if x %2 ==0]

print(myfunc(23,33,24,35,66))


'''

# Define a function called myfunc that takes in a string and returns a matching string where every even letter
# is uppercase and every odd letter is lowercase. Assume that the incoming string only contains letters
# and don't worry about numbers , spaces or punctuations. The output string can start with either an 
# uppercase letter , so long as letter alternate throughout the string.

def myfunc(val):
    st = ''
    count = 1
    for i in val:
        if count%2 ==0:
            st = st + i.upper()
        else:
            st = st + i.lower()
        count =  count + 1
    return st

print(myfunc('hello'))

