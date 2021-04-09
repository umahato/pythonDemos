
example = [1,2,3,4,5,6,7]

print(example)
from random import shuffle
shuffle(example)

print(example)


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(result)




def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number : 0,1 or 2 : ")
    
    return int(guess)

print(player_guess())

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong Guess!")
        print(mylist)


## Intial List
mylist = ['','0','']
# Suffle List
mixedup_list =  shuffle_list(mylist)
# User Guess
guess = player_guess()
# Check Guess
check_guess(mixedup_list,guess)
