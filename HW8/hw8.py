# Filename: hw8.py
# Author: Patrick Custer
# Section: 16
# Date: 11/11/2013
# Email: pcuste1@umbc.edu
# Description:

# This function opens the “cipher.txt” file and determines if the file had 26 
# entries. Remember, you ARE guaranteed that the file will not have an issue 
# of duplicate alphabetical letters. (But it may have duplicate cipher letters!!)
# returns False if the file is NOT 26 lines long, returns a LIST IF the file
# was 26 lines. Ex: List   [‘A C’, ‘B F’, etc…]
def validateFileLength():
    inFile = open("cipher.txt", 'r')
    listOfCiphers = []
    counter = 0
    for c in inFile:
        listOfCiphers.append(c.strip())
        counter += 1
    inFile.close()
    if counter != 26:
        return False
    return listOfCiphers

# This function determines if the file had 26 DISTINCT cipher entries.
# Input: list of ciphers
# returns True/False
def validateCipher(listOfCiphers):
    for i in range(len(listOfCiphers)):
        for j in range(i+1,len(listOfCiphers)):
            if listOfCiphers[j][2] == listOfCiphers[i][2]:
                return False
    return True

# This function opens results.txt and displays the file to the screen.
def printResults():
    inFile = open("results.txt", 'r')
    print (inFile.read())
    inFile.close()
    return

# This function simple prints the list of ciphers with both 
# <ALPHABET, CIPHER>. List of ciphers MUST be loaded for it to 
# print ANYTHING
def printCipher(listOfCiphers):
    for c in listOfCiphers:
        print (c)
    return

# This function opens A USER SELECTED FILE and displays the file 
# to the screen.
def printRegularTextFile():
    while True:
        try:
            fileName = input("Please enter the name of the file you wish to open: ")
            inFile = open(fileName,'r')
            for line in inFile:
                print(line.strip())
            inFile.close()
            return
        except IOError:
            print("Invalid file name. Please enter another.")
            
# This function does the most work. It must verify the loaded cipher using 
# validateCipher() function. The list of ciphers MUST be loaded before this 
# function is called!! Terminate the conversion (not the program) if the cipher # is bad, and DELETE the cipher if present. Otherwise it will ask for a file to # convert, and write the results to “results.txt”
def convertToCipher(listOfCiphers):
    while True:
        try:
            fileName = input("Please enter the name of the file you wish to open FOR CONVERSION: ")
            inFile = open(fileName,"r")
            outFile = open("results.txt","w")
            for line in inFile:
                for c in line:
                    for j in listOfCiphers:
                        if c == j[0]:
                            outFile.write(j[2])
                        elif c.lower() == j[0].lower():
                            outFile.write(j[2].lower())
                    if (c.lower() in list("abcdefghijklmnopqrstuvwxyz")) == False:
                        outFile.write(c)
            return ("file converted, please check results.txt for your encrypted file")
        except IOError:
            print("Invalid file name. Please enter another.")

def printMenu():
    print("a.) load cipher input (to be used later)")
    print("b.) convert regular text to ciphered (cipher MUST be loaded)")
    print("c.) display cipher to screen")
    print("d.) display regular text to screen")
    print("e.) display current results.txt to screen")
    print("f.) Quit")

def main():
    print("This is the Cipher program")
    cipherList = False
    while True:
        printMenu()
        userOption = input("Enter a menu option: ")
        if userOption == "a":
            cipherList = validateFileLength()
            print("cipher loaded, thank you")
        elif userOption == "b":
            if (cipherList != False and validateCipher(cipherList) == True):
                print(convertToCipher(cipherList))
            else:
                print("No cipher loaded OR cipher is invalid. Please load a cipher.")
        elif userOption == "c":
            if (cipherList != False):
                printCipher(cipherList)
            else:
                print("No cipher loaded OR cipher is invalid. Please load a cipher.")
        elif userOption == "d":
            printRegularTextFile()
        elif userOption == "e":
            printResults()
        elif userOption == "f":
            return
        else:
            print("Invalid option.")

main()
