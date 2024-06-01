#------------------------------------------Lab 10-----------------------------------------------
#1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

def display_file_content(file_name):
    try:
        with open(file_name, 'r') as file:                              # Open the file in read mode
            for line in file:                                           # Iterate over each line in the file
                print(line.strip())                                     # Print each line after stripping whitespace
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")                  # Handle FileNotFoundError

# Call the function with the file name
display_file_content("C:/Users/Phani/AppData/Local/Programs/Python/Python37/Anudip Foundation/ABC.txt")

#**********************************************************************************************************************
#output:

'''In a garden green, a frog did croak,
With a leap so high, the tadpoles awoke.
In splashes of laughter, the pond did soak.'''
#**********************************************************************************************************************


#----------------------------------------------------------------------------------------------

#2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”

def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:                              # Open the file in read mode
            content = file.read()                                      # Read the content of the file
            word_count = len(content.split())                           # Split the content into words and count them
            print(f"Total number of words in '{file_name}' are : {word_count}")  # Print the word count
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")                  # Handle FileNotFoundError

# Call the function with the file name
count_words_in_file("C:/Users/Phani/AppData/Local/Programs/Python/Python37/Anudip Foundation/ABC.txt")

#**********************************************************************************************************************
#output:
''' Total number of words in 'C:/Users/Phani/AppData/Local/Programs/Python/Python37/Anudip Foundation/ABC.txt' are : 24'''
#**********************************************************************************************************************

#----------------------------------------------------------------------------------------------

#3. Write a function in Python to count uppercase character in a text file “ABC.txt”

def count_uppercase_in_file(file_name):
    try:
        with open(file_name, 'r') as file:                              # Open the file in read mode
            content = file.read()                                      # Read the content of the file
            uppercase_count = sum(1 for char in content if char.isupper())  # Count uppercase characters
            print(f"Total number of uppercase characters in '{file_name}': {uppercase_count}")  # Print the count
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")                  # Handle FileNotFoundError

# Call the function with the file name
count_uppercase_in_file("C:/Users/Phani/AppData/Local/Programs/Python/Python37/Anudip Foundation/ABC.txt")

#**********************************************************************************************************************
#output:
'''Total number of uppercase characters in 'C:/Users/Phani/AppData/Local/Programs/Python/Python37/Anudip Foundation/ABC.txt': 3 '''
#**********************************************************************************************************************

#----------------------------------------------------------------------------------------------

#4. Write a function display_words() in python to read lines
#from a text file "story.txt", and display those words, which are less than 4 characters.

def display_words():
    try:
        words_less_than_4 = []                                          # Initialize an empty list to store words
        with open("C:/Users/Phani/AppData/Local/Programs/Python/Python37/Anudip Foundation/Story.txt", 'r') as file:  # Open the file in read mode
            for line in file:                                           # Iterate over each line in the file
                words = line.split()                                    # Split the line into words
                for word in words:                                      # Iterate over each word
                    if len(word) < 4:                                   # Check if the length of the word is less than 4
                        words_less_than_4.append(word)                   # Append the word to the list
        return words_less_than_4                                        # Return the list of words
    except FileNotFoundError:
        print("Error: File 'story.txt' not found.")                     # Handle FileNotFoundError

# Call the function
words_less_than_4_characters = display_words()                          # Get the list of words
print(words_less_than_4_characters)                                     # Print the list of words

#**********************************************************************************************************************
#output:
'''['a', 'in', 'a', 'and', 'a', 'had', 'a', 'of', 'and', 'an', 'the', 'One', 'to', 'the', 'the', 'As', 'she', 'the', 'she', 'a', 'by', 'and',
'she', 'the', 'her', 'of', 'a', 'in', 'In', 'the', 'of', 'the', 'an', 'to', 'in', 'the', 'As', 'the', 'she', 'a', 'its', 'she', 'and', 'up', 'a',
'a', 'in', 'her', 'you', 'the', 'to', 'the', 'of', 'the', 'and', 'our', 'her', 'to', 'her','and', 'on', 'an', 'to', 'her', 'and', 'the', 'the',
'And', 'so,', 'the', 'her', 'set', 'off', 'on', 'her', 'to', 'lay', 'and', 'an', 'of']'''
#**********************************************************************************************************************

#----------------------------------------------------------------------------------------------
