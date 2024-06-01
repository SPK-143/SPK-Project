#-----------------------------------------Lab 11-----------------------------------------------

#----------------------------------------------------------------------------------------------

#1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

def division_two_numbers(num1, num2):
    try:
        result = num1 / num2                      # Division operation
        print("Result of division:", result)      # Print the result if successful
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")    # Handle ZeroDivisionError exception

# Examples:
division_two_numbers(10, 2)                      # Output: Result of division: 5.0
division_two_numbers(5, 0)                       # Output: Error: Cannot divide by zero.

#----------------------------------------------------------------------------------------------

#2. Write a Python program that prompts the user to input an integer
#and raises a ValueError exception if the input is not a valid integer.    

def input_integer():
    try:
        num1 = int(input('Enter an integer number: '))          # Prompt user to input an integer
        return num1                                             # Return the input integer
    except ValueError:
        raise ValueError('Input is not a valid integer. Please enter a valid integer.')  # Raise ValueError if input is not an integer

# Example:
try:
    integer_value = input_integer()                            # Call function to input integer
    print('you have entered a valid input integer:', integer_value)  # Print the input integer if successful
except ValueError:
    print('Error: Invalid input. Please try again.')            # Handle ValueError exception

#----------------------------------------------------------------------------------------------

#3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

def open_file(file_name):
    try:
        with open(file_name, 'r') as file:                      # Open file in read mode
            print("File content:")                              # Print message
            for line in file:                                   # Loop through each line in the file
                print(line.strip())                             # Print each line (remove leading/trailing whitespace)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")          # Handle FileNotFoundError exception

# Example :
file_name = input("Enter the file name: ")                      # Prompt user to input file name
open_file(file_name)                                            # Call function to open file

#----------------------------------------------------------------------------------------------

#4. Write a Python program that prompts the user to input two numbers
#and raises a TypeError exception if the inputs are not numerical

def input_numbers():
    try:
        num1 = float(input('Enter the first number: '))         # Prompt user to input first number
        num2 = float(input('Enter the second number: '))        # Prompt user to input second number
        return num1, num2                                       # Return the input numbers
    except ValueError:
        raise TypeError('Inputs are not numerical. Please enter numerical values.')  # Raise TypeError if inputs are not numerical

# Example :
try:
    num1, num2 = input_numbers()                               # Call function to input two numbers
    print('You have entered two numerical values:', num1, 'and', num2)  # Print the input numbers if successful
except TypeError as e:
    print('Error:', e)                                         # Handle TypeError exception
