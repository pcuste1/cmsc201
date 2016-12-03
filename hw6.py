# File name: hw6.py
# Author: Patrick Custer
# Date: 10/27/2013
# Section: 18
# Email: pcuste1@umbc.edu
# Description: Simple game

global board

# Set the global variable board
# Inuput: Initial positions of the key and player
# Output: None
def setBoard(rowk,colk,rowp,colp):
    global board
    board = []
    for i in range(9):
        board.append([])
        for j in range(9):
            board[i].append(" *")
    board[rowk][colk] = " K"
    board[rowp][colp] = " P"

# Prints out the board
# Input: none
# Output: none
def showBoard():
    print("---------------------")
    for i in range(9):
        for j in range(9):
            if j == 0:
                print("|", end = "")
            print(board[i][j], end = "")
            if j == 8:
                print(" |", end = "")
        print()
    print("---------------------")

# Updates the position of the board
# Input: New position and old player position
# Output: The new player position
def updatePosition(newRowp, newColp, rowp, colp):
    if offBoard(rowp + newRowp, colp + newColp):
        print("Cannot move that way.")
        return rowp, colp
    else:
        board[rowp][colp] = " *"
        board[rowp + newRowp][colp + newColp] = " P"
        return rowp + newRowp, colp + newColp

# Determines if the move would go off the board
# Input: attempted position
# output: boolean
def offBoard(newRow, newCol):
    if newRow == -1 or newRow == 9 or newCol == -1 or newCol == 9:
        return True
    return False

# Determines if the player has reached the key or not
# Input:
# Output: boolean
def reachedKey(rowk, colk, rowp, colp):
    if board[rowk][colk] == board[rowp][colp]:
            return True
    return False
    
def main():
    print("Welcome to loops HW! Get to the key!!\n")
    rowk, colk, rowp, colp = 6,3,4,2
    direction = {'north':(-1,0), 'south':(1,0), 'east':(0,1), 'west':(0,-1)}
    setBoard(rowk,colk,rowp,colp)
    showBoard()
    while reachedKey(rowk,colk,rowp,colp) == False:
        flag = True
        while flag == True:
            userChoice = input("North, South, East or West? ").lower()
            if userChoice in ["north", "south", "east", "west"]:
                rowp, colp = updatePosition(direction[userChoice][0],direction[userChoice][1], rowp, colp)
                flag = False
            else:
                print("Invalid input.")
        showBoard()
    print("Good job! You've won!")

main()






