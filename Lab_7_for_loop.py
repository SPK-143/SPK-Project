#-------------------------------------------Lab 7----------------------------------------------------------------------------------------------------------------------------------------------
#    1. Print the first 10 natural numbers using for loop 

def first_ten_natural_numbers():                                                    # Define a function named first_ten_natural_numbers
    for i in range(1, 11):                                                               # Loop from 1 to 10 (inclusive)
        print(i)                                                                             # Print the current value of i
first_ten_natural_numbers()                                                          # Call the function to print the first ten natural numbers

#*********************************************************************************************************************************************************************************************************************
#Output:
'''
1
2
3
4
5
6
7
8
9
10 '''

#*********************************************************************************************************************************************************************************************************************

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#   2. Python program to check if the given string is a palindrome 

def palindrome_or_not(word_input):                                                              # Defined a function named palindrome_or_not which takes a single parameter word_input
    for charcter in range(len(word_input)//2):                                                  # Loop over half of the characters in the input word
        if word_input[charcter].lower() != word_input[-(charcter+1)].lower():          # Check if the character at the current position from the start is not equal to the character at the current position from the end
            return f'{word_input} is not a palindrome'                                          # If the characters don't match, return a message indicating it's not a palindrome
    return f'{word_input} is a palindrome'                                                        # If the loop completes without finding any mismatch, return a message indicating it's a palindrome

print(palindrome_or_not(input('Enter a word: ')))                                             # Prompt the user to input a word and pass it to the palindrome_or_not function, then print the result

    
#*********************************************************************************************************************************************************************************************************************
#Output:
'''Enter a word: Tenet
Tenet is a palindrome'''

#*********************************************************************************************************************************************************************************************************************


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  3. Python program to check if a given number is an Armstrong number


def is_armstrong(number):
    number_string = str(number)                                                    # Convert number to string to count digits 
    number_of_digits = len(number_string)                                        # Calculate the number of digits
    total = 0                                                                                # Initialize total to 0    
    for digit in number_string:
        total += int(digit) ** number_of_digits                                    # Calculation of sum of each digit raised to the power of the number of digits
    return total == number                                                           # Check if the total is equal to the original number 
number = int(input("Enter a number: "))                                        # Input a number from the user
if is_armstrong(number):                                                             # Check if the number is an Armstrong number and print the result
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")


#*********************************************************************************************************************************************************************************************************************
#Output:
'''Enter a number: 1634
1634 is an Armstrong number'''

#*********************************************************************************************************************************************************************************************************************


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#4. Python program to get the Fibonacci series between 0 to 50 


def fibonacci_numbers():                                                                                         # Initialize the first two Fibonacci numbers  
    first_number = 0
    second_number = 1  
    fibonacci_numbers = []                                                                                       # Initialize an empty list to store Fibonacci numbers
    for i in range(0, 50):                                                                                         # Loop to generate Fibonacci numbers up to 50        
        sum_number = second_number + first_number                                                   # Calculate the next Fibonacci number
        first_number, second_number = second_number, sum_number                              # Update the first and second numbers for the next iteration    
        fibonacci_numbers += [sum_number]                                                               # Concatenate the new Fibonacci number to the list
    print('the fibonaci series are :')
    return fibonacci_numbers                                                                                  # Return the list of Fibonacci numbers
result = fibonacci_numbers()                                                                                 # Call the function and store the result
print(result)                                                                                                      # Print the list of Fibonacci numbers

#*********************************************************************************************************************************************************************************************************************
#Output:
'''the fibonaci series are :
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309,
3524578, 5702887, 9227465, 14930352,24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903,
2971215073, 4807526976, 7778742049, 12586269025, 20365011074]'''

#*********************************************************************************************************************************************************************************************************************


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#5. Python program to check the validity of password input by users

def check_validity(enter_password):                                                                            # Define a function named check_validity which takes a single parameter enter_password
    password = 'GambitMaster@143'                                                                           # Define the correct password  
    for single_charcter in range(len(password)):                                                              # Loop through each character in the correct password        
        if password[single_charcter] != enter_password[single_charcter]:                             # Check if the characters of the entered password match the characters of the correct password
            return 'Your password is not valid'      
    return 'Your password is valid'                                                                             # If the loop completes without finding any mismatch, return a message indicating the password is valid
print(check_validity(input('Enter your password: ')))                                                    # Prompt the user to enter a password and check its validity using the function


#*********************************************************************************************************************************************************************************************************************
#Output:
'''Enter your password: GambitMaster@142
Your password is not valid'''

#*********************************************************************************************************************************************************************************************************************


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
