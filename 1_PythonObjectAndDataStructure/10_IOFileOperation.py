#if below command does not work in VS code 
# go to settings - > Python - > terminal -Execute in File Dir - Check that option.

## Reading , Writing , appending mode.
# mode = 'r' is ready only
# mode = 'w' is write only(will overwrite files or create new!)
# mode = 'a' is append only (will add on to files)
# mode = 'r+' is reading and writing.
# mode = 'w+' is writing and reading (overwrites existing files or creates a new file!)


'''
a_file = open("myfile.txt")
contents = a_file.read()
print(contents)
a_file.close()

#alternate option -- no need to mention to close the file

print('******************************************************************************')
with open('myfile.txt') as my_new_file:
    mycontents = my_new_file.read()

print(mycontents)



with open('myfile.txt',mode = 'r') as myfile:
    contents=myfile.read()
print(contents)

'''


with open('myfile.txt',mode='a') as f:
    f.write('Four on Fourth')

with open('myfile.txt',mode='r') as f:
    print(f.read())
