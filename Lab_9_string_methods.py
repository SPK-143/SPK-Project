#---------------------------------------------Lab 9--------------------------------------------

#1. Write a Python program to Count all letters, digits, and special symbols from the given 
#string Input = “P@#yn26at^&i5ve”

def count_characters(input_string):  # Function to count characters in the input string
    letters = 0  # Count for letters
    digits = 0   # Count for digits
    special_symbols = 0  # Count for special symbols
    for char in input_string:  # Loop through each character in the input string
        if char.isalpha():  # Check if the character is a letter
            letters += 1  # Increment the letter counter
        elif char.isdigit():  # Check if the character is a digit
            digits += 1  # Increment the digit counter
        else:  # If the character is neither a letter nor a digit, it's a special symbol
            special_symbols += 1  # Increment the special symbol counter
    return letters, digits, special_symbols  # Return the counts of letters, digits, and special symbols
input_string = "P@#yn26at^&i5ve"  # Input string
letter_count, digit_count, special_count = count_characters(input_string)  # Call the function to count characters
print("Number of letters:", letter_count)  # Print the count of letters
print("Number of digits:", digit_count)    # Print the count of digits
print("Number of special symbols:", special_count)  # Print the count of special symbols

#*******************************************************************************************************************
#output:
'''Number of letters: 8
Number of digits: 3
Number of special symbols: 4'''
#*******************************************************************************************************************

#--------------------------------------------------------------------------------------------

#2. Write a Python program to remove duplicate characters of a given string. 
#Input = “String and String Function”

def remove_duplicate(Input):
    no_duplicate_text = " "  # Initialize an empty string to store the result without duplicates
    for text_duplicate in Input:  # Iterate through each character in the input string
        if text_duplicate not in no_duplicate_text:  # Check if the character is not already in the result string
            no_duplicate_text += text_duplicate  # If not, add the character to the result string
    return no_duplicate_text  # Return the modified string without duplicates
print(remove_duplicate("String and String Function"))   # Call the function and print the result

#*******************************************************************************************************************
#output:
'''StringadFuco'''
#*******************************************************************************************************************
#--------------------------------------------------------------------------------------------

#3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
 #Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”

def count_characters(input_string):
    uppercase_count = 0  # Initialize counter for uppercase characters
    lowercase_count = 0  # Initialize counter for lowercase characters
    special_count = 0    # Initialize counter for special characters
    numeric_count = 0    # Initialize counter for numeric characters

    for char in input_string:  # Iterate through each character in the input string
        if char.isupper():  # Check if the character is uppercase
            uppercase_count += 1  # Increment the uppercase counter
        elif char.islower():  # Check if the character is lowercase
            lowercase_count += 1  # Increment the lowercase counter
        elif char.isdigit():  # Check if the character is a digit
            numeric_count += 1  # Increment the numeric counter
        else:  # If the character is not uppercase, lowercase, or a digit, it's a special character
            special_count += 1  # Increment the special character counter
    return uppercase_count, lowercase_count, special_count, numeric_count  # Return the counts
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"    # Input string
uppercase_count, lowercase_count, special_count, numeric_count = count_characters(input_string)    # Call the function to count characters
print("Number of uppercase characters:", uppercase_count)               # Print the counts
print("Number of lowercase characters:", lowercase_count)
print("Number of special characters:", special_count)
print("Number of numeric characters:", numeric_count)

#*******************************************************************************************************************
#output:
'''Number of uppercase characters: 5
Number of lowercase characters: 18
Number of special characters: 11
Number of numeric characters: 5'''
#*******************************************************************************************************************

#--------------------------------------------------------------------------------------------

#4. Write a Python Count vowels in a string 
#input= “Welcome to Python Assignment” 
#Output: Total vowels are: 8

def count_vowels(input_string):
    vowels = "aeiouAEIOU"  # Define a string containing all vowels
    vowel_count = 0  # Initialize a counter for vowels    
    for char in input_string:  # Iterate through each character in the input string
        if char in vowels:  # Check if the character is a vowel
            vowel_count += 1  # Increment the vowel counter    
    return vowel_count  # Return the total count of vowels
input_string = "Welcome to Python Assignment"  # Input string
print("Total vowels are:", count_vowels(input_string))           # Call the function to count vowels and print the result

#*******************************************************************************************************************
#output:
'''Total vowels are: 8'''

#*******************************************************************************************************************

#--------------------------------------------------------------------------------------------
