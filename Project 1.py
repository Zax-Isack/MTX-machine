#_______Calculator for  simple calculation_______

number1 = int(input())
number2 = int(input())
operations = 0

while operations < 4:
    operations += 1
    operation = input("OP =  ")

    if operation == " +Addition ": 
        sum = number1 + number2
        print(sum)

    elif operation == " Subtraction ": 
        subtraction = number1 - number2
        print(subtraction)

    elif operation == " MUltiplication ":
        product = number1 * number2
        print(product)

    elif operation == " /Division
        
    else:

        print("Please enter the numerical value or a selected operation in the calculator.")
