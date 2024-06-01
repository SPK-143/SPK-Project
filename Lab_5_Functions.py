#---------------------------------------------Lab 5-----------------------------------------------------
#1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

'''this function divides the 2 numbers '''
def div(numerator_input,denominator_input):     
    print(f'The division of {numerator_input} and {denominator_input} is:',numerator_input/denominator_input)
div(54,9)
#--------------------------------------------------------------------------------------------------------
#2. Declare a square() function with one parameter. Then call the function and pass one number and display the square of that number .

'''Usage of square formula and defining the function according to the quesition and this function gives the square of number as output'''
def square(square_input_wanted):
    print(f'The square of {square_input_wanted} is: ',square_input_wanted**2)
square(143)

#--------------------------------------------------------------------------------------------------------

#3. Using max() and min() functions display the maximum and minimum of 5 random numbers.

'''usage of random module we can use randomint() to get the 5 random numbers and can display highest and smallest numbers in the list of 5 numbers'''
import random
# Generate 5 random numbers between 1 and 100
numbers = [random.randint(1, 100) for i in range(5)]
# Find the maximum and minimum values
maximum = max(numbers)
minimum = min(numbers)
# Print the results
print('the random numbers are',numbers,sep=',',end='\n')
print(f"The maximum number is: {maximum}")
print(f"The minimum number is: {minimum}")
#--------------------------------------------------------------------------------------------------------
#4. Accept a name from the user and display that in lower case using lower() function

'''this function accepts the input from the user and converts in to the lower case from upper case'''
def lower(string_input):
    print(f'the lower case of {string_input} is:',string_input.lower())
lower(input('enter a name in upper case:'))
#--------------------------------------------------------------------------------------------------------
