"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# def make_int(num1, num2):
    #make the second and third token into ints
# def tokens_used(sym, int(num1), int(num2 = None)):
#     user_input = input()

#     token_2 = user_input.split(" ")

#     #token3 is optional (make it have a default value)
#     #function always needs at least two arguments
#     sym = tokenized[0]

#     #returns the tokens needed for the situation calling the function
#     return [sym, num1, num2]


def mathstufffornow():
    """Read user input and evaluate the numbers based on math thing done"""
    while True:
        #read input
        str = input() 

        #tokenize input
        tokenized = str.split(" ")

        #if the first token is "q":
        if tokenized[0].lower() == "q":
            return "Thanks for using the Calculator!"
            # break

        #else
        else:
        #make them all ints
        #new variables for tokenized values
            # sym = tokenized[0]
            # num1 = int(tokenized[1])
            # if the list has 3 items the last num2 is the last item 
            # if input has 3 items, 3 variables will be made
            if len(tokenized) == 3:
                num2 = int(tokenized[2])
                sym = tokenized[0]
                num1 = int(tokenized[1])
                if sym == "+":
                    result = add(num1, num2)

                elif sym == "-":
                    result = subtract(num1, num2)
                
                elif sym == "*":
                    result = multiply(num1, num2)
                
                elif sym == "/":
                    result = divide(num1, num2)

                elif sym == "pow":
                    result = power(num1, num2)

                elif sym == "mod":
                    result = mod(num1, num2)

                print(float(result))

            #if input is only 2 items, only 2 variables will be made
            if len(tokenized) == 2:
                sym = tokenized[0]
                num1 = int(tokenized[1])
                if sym == "square":
                    result = square(num1)

                elif sym == "cube":
                    result = cube(num1)
                print(float(result))

print(mathstufffornow())