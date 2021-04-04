#Sets are unordered collections of unique elements.
#there can be one representative of the same object

myset = set()
print(myset)

myset.add(1)
print(myset)

myset.add(2)
print(myset)


myset.add(2)
print(myset)

mylist = [1,1,1,2,2,2,1,1,3,3,3,3]
print(set(mylist))