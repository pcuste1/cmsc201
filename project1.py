# Filename:     project1.py
# Author:       Patrick Custer
# Date:         11/23/2013
# Section:      18
# Email:        pcuste1@umbc.edu
# Desccription:
#

# Fills the board recursively
# Input: position of current spot and the board
# Output: board???
def autoFill(row, col, board):
    if board[row][col] != ".":
        return   
    board[row][col] = "x"
    autoFill(row+1, col, board)
    autoFill(row, col+1, board)
    autoFill(row, col-1, board)
    autoFill(row-1, col, board)

# Greets the user and asks for the file to read.
# Input: None
# Output: None
def greeting():
    print("This is the autofill program!")

# Determins the length of the files
# Input: File name
# Output: the row size and column size
def getRowCol(fileName):
    inData = open(fileName, "r")
    row,col = 0,0
    for line in inData:
        row += 1
        col = len(line)
    inData.close()
    return row, col 

# Creates the board from the file
# Input: the file name
# Output: the created board
def createBoard(fileName):
    inData = open(fileName, "r")
    row,col = getRowCol(fileName)
    board = []
    board.append("0"*(col+2))
    for line in inData:
        board.append(list("0" + line.strip() + "0"))
    board.append("0"*(col+2))
    inData.close()
    return board

# Determines if a file is valid or not
# Input: None
# Output: Valid file name
def fileValidate():
    while(True):
        try:
            fileName = input("Please pick a file to read, or type ‘quit’ to exit: ")
            if fileName.lower() == "quit":
                return fileName
            inData = open(fileName, "r")
            return fileName
        except FileNotFoundError:
            print("No file found.")
        

# Prints the board
# Input: the board
# Output: None
def printBoard(board):
    for line in board:
        for c in line:
            if c != "0":
                print(c, end ='')
        print("")
        
# Creates the board and gets user input as well as call play game
# Input: none
# Output: none
def beginGame():
    while(True):
        fileName = fileValidate()
        if fileName.lower() == "quit":
            return
        board = createBoard(fileName)
        print("The file chosen looks like this before autofill:")
        printBoard(board)
        playGame(board)

# Plays the game. aka calls autofill and gets starting location
# Input: board as well as the size of the board   
# Output: None 
def playGame(board):
    r,c = getRC(board) 
    autoFill(r+1,c+1,board)
    print("After autofill, starting at <",r,",",c,">, the results are:")
    printBoard(board)
  
# Splits the string input of the user in the respective coordinates then converts to integers
# Input: String
# Output: two separate integers representing coordinates  
def getRC(board):
    listLoc,valid = [],False
    while valid == False:
        listLoc,valid = validateCoord(input("Please select x and y coordinate to start autofill: ").split())
        if valid == True:
            valid = coordOnBounds(board,listLoc)
    return int(listLoc[0]), int(listLoc[1])

# Checks if X and Y are valid on the specific board
# Input: board
# Output: Boolean
def coordOnBounds(board,listLoc):
    try:
        board[int(listLoc[0])][0]
    except IndexError:
        print("X is not a valid coordinate.")
        return False
    try:
        board[0][int(listLoc[1])]
    except IndexError:
        print("Y is not a valid coordinate.")
        return False
        
# Checks if X and Y are valid on all boards
# Input: list of coordinates
# Output: Boolean and a list
def validateCoord(listLoc):
    if len(listLoc) != 2:
        print("You need to enter two coordinates")
    elif listLoc[0].isdigit() == False or int(listLoc[0]) < 0:
        print("X is not a valid coordinate.")
    elif listLoc[1].isdigit() == False or int(listLoc[1]) < 0:
        print("Y is not a valid coordinate.")
    else:
        return listLoc,True
    return listLoc,False

def main():
    greeting()
    beginGame()
    print("Thanks for playing")
   
main()

