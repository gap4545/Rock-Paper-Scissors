operation = int(input("""Input Operation.
1. Add
2. Subtract
3. Divide
4. Multiply
5. Exponent
6. Quit
"""))
#Gets Operation from user, bitch
if operation == 6 :
    quit()
    

number1 = int(input("Input first number:")) #Needed int() before input()
number2 = int(input("Input second number:"))
total = 0

if operation == 1 :
    total = number1 + number2
elif operation == 2 :
    total = number1 - number2
elif operation == 3 :
    total = number1 / number2
elif operation == 4 :
    total = number1 * number2
elif operation == 5 :
    total = number1 ** number2

#Does the mathe hoe
print("Your total is", total)
#Print the total bitch    

    
    
                