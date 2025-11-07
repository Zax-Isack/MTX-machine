#_______Calculator for  simple calculation_______

def calculator():
    number1 = int(input())
    number2 = int(input())
    operations = 0

    while True:
        
        operation = input("Mathematical Operation =  ")
        if operation == "Addition":
            sum = number1 + number2
            return(sum)

        elif operation == "Subtraction":
            subtraction = number1 - number2
            return(subtraction)

        elif operation == "Multiplication":
            product = number1 * number2
            return(product)

        elif operation == "Division":
            division = number1 / number2
            return(division)

        else:
            return("Please enter the numerical value or a selected operation in the calculator.")


calculations = calculator()
print(calculations)


