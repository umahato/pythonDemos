'''
def even_check(number):
    return  (number %2 == 0)
     
resultu = even_check(20)
print(resultu)
# Return true if any number is even inside a list.
def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False
num_list = [1,3,5] 
result = check_even_list(num_list)
print(result)
'''



def check_even_list(num_list):
    # Return all the even numbers in a list

    # placeholder variable
    even_number = []

    for number in num_list:
        if number % 2 == 0:
            even_number.append(number)
        else:
            pass
    return even_number


num_list = [1,3,5,20,44,33] 
result = check_even_list(num_list)
print(result)