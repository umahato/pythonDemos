# def name_of_function():
# def -> it tells us that it's a function in python.
# name_of_functions() - > name of the function is in snake casing case. Snake casing is all 
# lowercase with underscores between words.
# parenthesis at the end. 
# a colon indicates 

#def name_of_function():
#    '''
#    Docstring explains function.
#    '''
#    print("Hello")
#
# >> name_of_function
# >> Hello

'''
def add_function(num1, num2):
    return num1 + num2

result =add_function(4,7)
print(result)


def say_hello():
    print("Hello")

say_hello()


def say_hello(name):
    print(f'Hello {name}')

say_hello('umesh')

'''

def say_hello(name = 'Default'):
    print(f'Hello {name}')

say_hello()

def add_num(num1, num2):
    return num1 + num2

sum = add_num(20,30)
print(sum)


def print_result(a,b):
    print(a+b)


def return_result(a,b):
    return a+b

print_result(10,30)

result = return_result(10,30)
print(result)

def myfunc(a,b):
    print(a+b)
    return (a+b)

myfunc(55,89)