#-----------------------------------------------Lab 8--------------------------------------

#1. Write a Python program to count the occurrences of each word in a given sentence 
#string = “To change the overall look of your document. To change the look available in the gallery”

def count_occurrences(string):                        # Define a function that takes a string as input
    words = string.split()                                # Split the input string into a list of words
    words_count = {}                                     # Initialize an empty dictionary to store word counts
    for word in words:                                  # Iterate through each word in the list
        if word in words_count:                      # Check if the word is already a key in the dictionary
            words_count[word] += 1                # If yes, increment the count for that word
        else:                                                # If the word is not in the dictionary
            words_count[word] = 1                 # Add the word to the dictionary with a count of 1
    return words_count                              # Return the dictionary containing word counts

print(count_occurrences('To change the overall look of your document. To change the look available in the gallery'))  # Print the result of calling the function with a sample string

#************************************************************************************************************************************************
#output:
'''{'To': 2, 'change': 2, 'the': 3, 'overall': 1, 'look': 2, 'of': 1, 'your': 1, 'document.': 1, 'available': 1, 'in': 1, 'gallery': 1}'''
#************************************************************************************************************************************************

#-------------------------------------------------------------------------------------------------------------------

#2. Write a Python program to remove a newline in Python 
#String = "\nBest \nDeeptech \nPython \nTraining\n"

def remove_newline(string):                                                                                                                                    # Define a function called remove_newline which takes a string as input
    new_string = ""                                                                                                                                                  # Initialize an empty string to store the modified string    
    for character in string:                                                                                                                                        # Iterate over each character in the input string
        if character != '\n':                                                                                                                                        # Check if the current character is not a newline character
            new_string += character                                                                                                                            # If it's not a newline character, append it to the new string            
    return new_string                                                                                                                                           # Return the modified string with newline characters removed
print(remove_newline("\nBest \nDeeptech \nPython \nTraining\n"))                                                                        # Test the function by passing a string with newline characters


#************************************************************************************************************************************************
#output:
'''Best Deeptech Python Training'''
#************************************************************************************************************************************************
#-------------------------------------------------------------------------------------------------------------------

#3. Write a Python program to reverse words in a string 
#String = “Deeptech Python Training” 


def reverse_words(string):                                                                      # Define the function to reverse words in a string                                                                                                         
    words = string.split()                                                                         # Split the string into individual words    
    reversed_words = words[::-1]                                                             # Reverse the list of words
    reversed_string = ""  
    for word in reversed_words:                                                                 # Concatenate the words back into a string
        reversed_string += word + " "                                                           # Append each word with a space
    if reversed_string:
        reversed_string = reversed_string[:-1]                                               # Remove the last space
    return reversed_string
input_string = "Deeptech Python Training"                                               # Define the input string
print("Original string:", input_string)                                                      # Call the function and print the result
print("Reversed string:", reverse_words(input_string))                                # Print the reversed string

#************************************************************************************************************************************************
#output:
Original string: Deeptech Python Training
Reversed string: Training Python Deeptech
#************************************************************************************************************************************************
#-------------------------------------------------------------------------------------------------------------------

#4. Write a Python program to count and display the vowels of a given text String=”Welcome to python Training

def display_vowels(string):
    vowels = 'aeiouAEIOU'
    vowel_count = 0  # Initialize a counter for vowels
    vowel_list = []  # Initialize an empty list to store vowels  
    for character in string:  # Iterate over each character in the string       
        if character in vowels: # Check if the character is a vowel
            vowel_count += 1  # Increment the vowel counter
            vowel_list+=[character]  # Add the vowel to the list
    return "Total vowels: " + str(vowel_count) + "\n" + "Vowels: " + str(vowel_list)  # Return the count and list of vowels as a string

print(display_vowels('Welcome to Python Training')) # printing the result

#************************************************************************************************************************************************
#output:
'''Total vowels: 8
Vowels: ['e', 'o', 'e', 'o', 'o', 'a', 'i', 'i']'''
#************************************************************************************************************************************************

#-------------------------------------------------------------------------------------------------------------------




            
            


