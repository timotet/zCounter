#
# Count the number of Z's in an .NC program or .gcode file
# 10/19/14 ported to python3.4

from sys import argv
script, importFile = argv

####### variables #########

lineCounter = 0
zCounter = 0
lLine = []
lLineNumber = []  # for keeping track of where the z occurred in the program
lFile = []        # list for a copy of the file that we can manipulate
lCopy = []

####### functions #########


        
########## Main ###########        

with open(importFile) as f:
    for line in f:
        lFile.append(line)
        lineCounter += 1
        if "Z" in line and "F" in line:
            zCounter += 1
            lLineNumber.append(lineCounter)
            lLine.append(line)
            
for number in lLineNumber:
    index = 0
    print(number)
    print(lFile[number])
    lCopy = map(min,list(lFile[number]))  # make a list out of the string
    for letter in lCopy:
        index += 1
        if letter == "E":
            print("found E move to next line")
            lLineNumber.insert(number, number + 1)
            print(lLineNumber)
            print("index is %d" % index)
            break
               
    print(lCopy)      
    print(type(lCopy))
        
        
print("The file contains %d lines" % lineCounter)
print("There are %d Z's in the file" % zCounter)
print(len(lFile))
print(len(lLine))
print(lLineNumber)
 
# to create a new file in the current directory
newFileName = input("Type in a file name ----> ")
newFileName = newFileName + ".nc" # this adds a file extension
print("creating ************************************************************* %s"  % newFileName)
newFile = open(newFileName, "w") # the 'a' does'nt truncate an existing file like a 'w' does
newFile.write("helloWorld\n")
newFile.close()
