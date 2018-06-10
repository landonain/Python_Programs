# Program is removing 0-9 from a string using ord()
# as the marker to pull the from 0 = ord(48) and 9 = ord (57)
# Found way to remove int chars from str with ord

# Found way to replace characters in the string with
# a blank space using a loop to iterate over the string

# Found a way to get the directories with os module
# and created a method to pass the files (string objects)
# and then renaming the objects with my method
# it works!
import pdb
import os


# Method for removing the char ints from the title
def removingInts(newFile):
    for x in newFile:
        if ord(x) in range(48, 58, 1):
            newFile = newFile.replace(x, '')
    os.rename(act_file, newFile)


# Method for removing the files
def removingFile(newFile):
    os.remove(newFile)
    print newFile

# Getting the file path and passing it as a string           
#def filePath(filePath):
file_path = raw_input("Please enter the file path for the dir.")
for fileName in os.listdir(file_path):
    act_file = (file_path + "\\" + fileName)
    #removingFile(act_file)
    #pdb.set_trace()
    if fileName[-4:] == ".jpg":
        removingInts(act_file)

    
 
    
     
 
 


# Range of ord values for numbers
# x = '9'
# print ord(x)
# x = '0'
# print ord(x)
# value = "000011122ABC123"

# original method to loop over values and replace them
# for x in value:
#    if ord(x) in range(48, 58, 1):
#       value = value.replace(x, '')

