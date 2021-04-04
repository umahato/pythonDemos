#Tuples : Tuples are very similar to Lists. However the  have one key difference  - immutability
# Once an element is inside a tuple, it can not be reassigned

# Tuples use parenthesis : (1,2,3)

t = (1,2,3)
mylist = [1,2,3]
print(type(t))
print(type(mylist))

t2 = ('one',2)
print(t2)

print(t2[1])

t3 = ('a','a','b')
print(t3.count('a'))
print(t3.index('a'))