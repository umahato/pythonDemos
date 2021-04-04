#Undordered and can not be sorted.
# Objects retrieve by Key Names
my_dict = {'key1': 'value1','key2':'value2'}
print(my_dict)
print(my_dict['key1'])

prices_lookup = {'apple':2.99,'oranges':1.99,'milk':5.80}

print(prices_lookup['apple'])

d = {'k1':123 , 'k2':[0,1,2,3],'k3':{'insidekey':100}}

print(d['k2'])

print(d['k3']['insidekey'])

d1 = {'key1' : ['a','b','c']}
print(d1)

mylist = d1['key1']
print(mylist)

letter = mylist[1]
print(letter)

print(letter.upper())

print(d1['key1'][2].upper())