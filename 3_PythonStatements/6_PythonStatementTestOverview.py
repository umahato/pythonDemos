# 1.    Use for .split() and if to create a statement that will print out the words that will start with 's'
st = 'Sam Print only the word that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':
        print(word)

print('********************************************************************************************')
#2 . Use range() to print all the even numbers from 0 to 10.

#1.
for x in range(0,10):
    if x % 2 ==0:
        print(x)

#2.
print(list(range(0,11,2)))

#3.
for num in range(0,11,2):
    print(num)
print('********************************************************************************************')

# 3. Use a list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3

print([x for x in range(1,51) if x%3 ==0])

print('********************************************************************************************')
#4. Go through the string below and if the lenth of a word is even print "even!"

for word in st.split():
    if len(word) % 2 == 0:
        print(word + ' is Even.')

print('********************************************************************************************')
#5. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz"
# instead of the numbers, and for the multiples of five print "Buzz". For numbers which are multiples of both three
# and five print "FizzBuzz"

for num in range(1,101):
    if num %3 == 0 and num %5 ==0:
        print('FizzBuzz')
    elif num%3 ==0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)
print('********************************************************************************************')
print([word[0] for word in st.split()])

print('********************************************************************************************')