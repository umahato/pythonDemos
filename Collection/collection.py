'''

# There are four collection data types in python which are used to store collections of data. 
# a. Lists , b. Tuples , c. Sets , d. Dictionary
# a. Tuple - Ordered and immutable,  can have duplicate values
# Set - Unordered and declared in {} curly brackets, does not have duplicate entries.
# Dictionary - key value pairs , mutable in nature.

# Collections - Specialised collection data structure.
# Specialised Collections Data Types
a. namedtuple()
b. Chainmap
c. Counter
d. OrderedDict
e. defaultdict
f. UserDict
g. UserList
h. UserString

a. namedtuple() -  returns a tuple with a named value for each element in the tuple. 
Details = (name = 'edureka',course = 'python',course2 = 'data science')



from collections import namedtuple
a = namedtuple('courses','name , technology')
s =a('data science','python')
print(s)

p = a._make(['artificial intelligence','python'])
print(p)



b. deque - deque pronounced as 'deck' is an optimised list to perform inserstion and deletion easily.

Deque(['e','d','u','r','e','k','a'])


from collections import deque
a = ['e','d','u','r','e','k','a']
d = deque(a)
print(d)

d.append('python')
print(d)

d.appendleft('python2')
print(d)

d.popleft()
print(d)

'''

c. Chainmap - is a Dictionary like class for creating a single view of multiple mappings

A = {1:'edureka',2:'python'}
B = {3:'data science',4: 'AI'}

[{1:'edureka',2:'python'},{3:'data science',4:'AI'}]