#ordered sequences
#can be nested

my_list = [1,2,3,4,5]
my_list1 = ['STRING',100,12.34]
print(len(my_list))
print(len(my_list1))

print(my_list1[2])

print(my_list + my_list1)

my_list1[0] = 'one all lower'
print(my_list1)
my_list1.append(233)
print(my_list1)

my_list1.pop()
print(my_list1)

num_list = [1,2,223,3,121,5,63]
print(num_list)
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)