'''
Y = 20
X = 10
print (type(X))

num = 10>9
print(type(num))

name = "Umesh"
print(len(name))

print(name[2])
print(name[2:6])
print(name.upper())
print(name.lower())


mylist = [10,20,30,"Umesh","shilu"]
print(mylist)
mylist.append(10)
print(mylist)
mylist.insert(5,100) # insert a value in specific position in a list

print(mylist)
mylist.reverse()
print(mylist)



### Dictionary mutable
courses = {
    1:'Python',
    2:'Java',
    3:'Data Science'
}

print(courses)

print(courses[2])
courses[2] = 'aws'
print(courses)


# Tuple -- immutable
animals = (10,20,30,'tiger','lion','giraffe','tiger')
print(animals[2])
print(animals.count('tiger'))



# set -- immutable

myset = {10,20,30,40,50,40,'Umesh','Bangalore'}
print(myset)




#range

print(range(10))
print(list(range(11)))




a = [1,2,3,4,5]
b = {4,5,6,7,8}
c = [a,b]
print(c)



# Type conversion.

x = 10
name = "umesh"

print(str(x) + name )

'''
