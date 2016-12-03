# FileName:         project2.py
# Author:           Patrick Custer
# Section:          16
# Date:             12/10/2013
# Email:            pcuste1@umbc.edu
# Description:      
#                   Solves simple mathematical equations using stacks
#                   and the order of operations.

from stack import *

inputPriority = {"+" : 1 , "-" : 1 , "*" : 2, "/" : 2, "%" : 2, "^" : 5, "(" : 6, ")": "-" , "$" : "-"}
stackPriority = {"+" : 1 , "-" : 1 , "*" : 2, "/" : 2, "%" : 2, "^" : 4, "(" : 0, ")": "-" , "$" : -1}

# Simply Greets the user
# Input: None
# Output: None
def greeting():
    print("Author: Patrick Custer\t Section: 16\t File: projct2.py")

# Creates the stacks that will be used throughout the program. Does this using stack.py's stack() function
# Input: None
# Output: opStack , inputStack , valueStack
def initializeStacks():
    opStack , inputStack , valueStack = stack() , stack() , stack()
    push(opStack , "$") , push(inputStack , -1) , push(valueStack, "$")
    # print(opStack , "\t" , inputStack , "\t" , valueStack)
    return opStack , inputStack , valueStack

# Gets the equation from the user
# Input: None
# Output: List of the users equation. Ie. 2 + 2 * 3 => ['2', '+', '2', '*', '3']
def getInput():
    userEqu = input("please enter an equation (-1 to quit): ")
    if userEqu == "-1":
        return "-1"
    return list(userEqu.split())

# Adds a value to the valueStack
# Input: Value to add and the valueStack
# Output: None
def addValue(char, valueStack):
    push(valueStack,char)
    
# Validate the equation. Mine does both valid characters an d valid equation formathing. Ie. 1 + + 2 will return as false.
# Input: the users equation
# Output: Boolean
def equationValidation(userEqu):
    validCharNum = ["1","2","3","4","5","6","7","8","9"]
    validCharOp =["+","-","*","/","%","^","(",")"]
    oldChar = ""
    for char in userEqu:
        # print(char , "\t" , oldChar)
        
        # So as to avoid ( ( 2 * 1 ) + 3) being flagged with an error, I used to conditional that the code will only run if it does not equal one of those.
        if char != "(" and char != ")":
            
            # I check for whether the char is a valid operator/value and if the char that was previously added is also an operator/value
            if ((char in validCharNum) == False and (char in validCharOp) == False) or (char in validCharNum) == (oldChar in validCharNum):
                print("ERROR: invalid equation")
                return False
            oldChar = char
    
    # If no errors are found, I return true.
    return True

# adds an operator to the op stack and its input value to the the input stack
# Input: Operator to add , opStack , inputStack , valueStack
# Output: None
def addOperator(char, opStack, inputStack , valueStack):
    
    # First, the method checks if the new operator is a ")"
    if char == ")":
        print("pop and process, found a )")
        popAndProcess(opStack , inputStack , valueStack)
        
        # Removes the "("
        pop(opStack)
        pop(inputStack)
    else:
        # The program then checks if the operator has a high enough value to be added. popAndProcess until it is
        while inputPriority[char] <= top(inputStack):
            print("STACK VALUE >= the new INPUT PRIORITY. So pop and process, and recheck.")
            popAndProcess(opStack , inputStack , valueStack)
            
        # Finally, push the new operator into both the opStack and the inputStack
        push(opStack,char)
        print(char , "was just added to opStack")
            
        push(inputStack,stackPriority[char])
        print(stackPriority[char] , "was just added to inputStack")
    # print(opStack , "\t" , inputStack , "\t" , valueStack)

# pops and processes the stacks
# Input: opStack , inputStack , valueStack
# Output: None
def popAndProcess(opStack , inputStack , valueStack):
    
    # First, the method gets the values for A, B, and Z in the equation A z B = X
    valueA , valueB , operator = float(pop(valueStack)) , float(pop(valueStack)) , pop(opStack)
    # print(valueA , " " , operator , " " , valueB)
    
    # I used a dictionary for all the math to avoid a crap load of if statements.
    # Each key corresponds to a value using the key as the operator in an equation.
    mathDictionary = {"+": valueA + valueB, "-": valueB - valueA, "*": valueA * valueB,
                      "/": valueB / valueA, "%": valueB % valueA, "^": valueB ** valueA}
    
    # Push the new value onto the value stack
    push(valueStack,mathDictionary[operator])
    print("new answer being placed into the VALUE stack is:" , valueStack[-1])
    
    # remove the leftover value in the inputStack
    pop(inputStack)
    
    # print(opStack , "\t" , inputStack , "\t" , valueStack)
    # print(valueStack , "\t" , opStack)

def main():
    greeting()
    while True:
        error = False
        opStack , inputStack , valueStack = initializeStacks()
        # print(opStack , "\t" , inputStack , "\t" , valueStack)
        userEqu = getInput()
        if userEqu == "-1":
            print("Goodbye.")
            return
        while equationValidation(userEqu) == False:
            userEqu = getInput()
            if userEqu == "-1":
                print("Goodbye.")
                return
        print("the equation(list) we are looking at is: " , userEqu)
    
        for char in userEqu:
            print(" looking at " , char , " in the equation")
            
            # Check if char is a value. If it is add to value stack
            if ord(char) >= 48 and ord(char) <= 57:
                print("adding a value to ValueStack")
                addValue(char, valueStack)
                
            # Check if the program attempts to add ")" onto a "(". If so, produce an error. 
            # Ie. ( ( 1 + 2 ) ) will produce an error.
            elif top(opStack) == "(" and char == ")":
                print("ERROR: unable to solve equation")
                error = True
                break
            
            # Otherwise add the operator to the opStack and inputStack
            else:
                addOperator(char, opStack, inputStack , valueStack)
            # print(opStack , "\t" , inputStack , "\t" , valueStack)
        
        # Once all of the equation has been added, pop and process until the opStack is emppty.
        while top(opStack) != "$" and error != True:
            print("END OF EQUATION, so pop and process until op Stack is only a $")
            
            # Checks for if there is a hanging "(" in opStack or if opStack is empty. Both will produce an error.
            # opStack will be empty if the equation looks like 1 + 2 ). That will produce an error.
            if top(opStack) == "(" or isEmpty(opStack): 
                print("ERROR: unable to solve equation")
                error = True
                break
            
            # Otherwise popAndProcess.
            else:
                popAndProcess(opStack , inputStack , valueStack)    
        
        # print(opStack , "\t" , inputStack , "\t" , valueStack)
        if error == False:
            print(top(valueStack))
    
# print(inputPriority["+"] , "\t" ,stackPriority["$"] , "\t" , inputPriority["+"] >= stackPriority["$"])  

# popAndProcess(["$","^"] , ["$", 2 , 3])

main()