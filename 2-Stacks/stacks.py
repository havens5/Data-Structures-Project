def main(string):

    #create a empty stack
    letterStack = []

    #take each letter of the string and add it to the stack
    for letter in string:
        letterStack.append(letter)
    
    finalStack = []
    #make it so the first item that you want printed is at the end of the stack to be printed first
    while len(letterStack) > 0:
        finalStack.append(letterStack.pop())
    
    #take each letter off the stack until it is empty
    while len(finalStack) > 0:
        print(finalStack.pop())

main("Live on time, emit no evil")
print("")
main("Hello")
