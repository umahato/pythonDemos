#1. Lesser of two evens : Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

'''
#method : 1
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 ==0:
        #Both numbers are even
        if a< b:
            result = a
        else:
            result = b
    else:
        #one or both numbers are odd
        if a>b:
            result = a
        else:
            result = b
    return result

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))



#method 02.
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 ==0:
       result = min(a,b)
    else:
       result = max(a,b)
    return result

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

#method 03.
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 ==0:
       return min(a,b)
    else:
        return max(a,b)
   

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

'''
#2. Animal Crakers: Write a function takes a two-word string and return true if both words begin with same letter
# animal_crakers('Levelheaded Llama') --> True
# animal_crakers('Crazy Kangaroo') --> False

#Method 01 

'''
def animal_crakers(text):
    wordlist = text.split()
    print(wordlist)

    first = wordlist[0]
    second =wordlist[1]

    return first[0] == second[0]


print(animal_crakers('Levelheaded Llama'))
print(animal_crakers('Crazy Kangaroo'))

#method 2.

def animal_crakers(text):
    wordlist = text.lower().split()
    print(wordlist)
    return wordlist[0][0] == wordlist[1][0]


print(animal_crakers('Levelheaded Llama'))
print(animal_crakers('Crazy kangaroo'))


# 3. Makes twenty: Given two integers, return true if the sum of the integers is 20 on if one of the integer
# is 20. If not, return false.

# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> True

#Method 01

def makes_twenty(n1, n2):
    if n1+ n2 ==20:
        return True
    elif n1 == 20:
        return True
    elif n2 ==20:
        return True
    else:
        return False

print(makes_twenty(20,10))
print(makes_twenty(2,3))


'''


def makes_twenty(n1, n2):
    return (n1+n2) == 20 or n1 ==20 or n2 ==20

print(makes_twenty(20,10))
print(makes_twenty(2,3))



























