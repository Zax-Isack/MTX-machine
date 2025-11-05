#_______Calculator for  simple calculation_______

number1 = int(input())
number2 = int(input())
operations = 0

while operations < 4:
    operations += 1
    operation = input("OP =  ")

    if operation == " + ": # sign for addition
        sum = number1 + number2
        print(sum)

    elif operation == " - ": # sign for subtraction
        subtraction = number1 - number2
        print(subtraction)

    elif operation == " * ": # sign for Multiplications
        product = number1 * number2
        print(product)

    elif operation == " / ": # sign for division
        division = number1 / number2
        print(division)
        
    else:
        print("Please enter the numerical value or a selected operation in the calculator.")