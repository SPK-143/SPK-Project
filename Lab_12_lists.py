#-------------------------------------------Lab 12---------------------------------------------

#---------------------------------------------------------------------------------------------
#1. Write a Python program to sum all the items in a list.
#----------------------------------------------------------------------------------------------

item_list = [5, 6, 6, 666, 3, 54]  # Define the original list containing integer elements.
sum_list = 0  # Initialize a variable to store the sum of the list elements.
for item in item_list:  # Iterate over each item in the list and add it to the sum.
    sum_list += item
print('the sum of list is:', sum_list)  # Print the sum of the list.

#*****************************************************************************************************************
#Output:
'''the sum of list is: 740'''
#*****************************************************************************************************************

#----------------------------------------------------------------------------------------------
#2. Write a Python program to get the largest and smallest number from a list without builtin functions.
#---------------------------------------------------------------------------------------------

def find_largest_and_smallest(numbers):  # Define a function to find the largest and smallest numbers in a list.
    if not numbers:  # Check if the list is empty.
        return None, None
    largest = smallest = numbers[0]  # Initialize variables to store the largest and smallest numbers.    
    for num in numbers:  # Iterate over each number in the list.
        if num > largest:  # Update the largest number if the current number is larger.
            largest = num
        elif num < smallest:  # Update the smallest number if the current number is smaller.
            smallest = num    
    return largest, smallest  # Return the largest and smallest numbers.
example_list = [1, 23, 44, 5, 67, 34]  # Define an example list of numbers.
largest_num, smallest_num = find_largest_and_smallest(example_list)  # Call the function to find the largest and smallest numbers in the list.
print('The largest number is:', largest_num)  # Print the largest number.
print('The smallest number is:', smallest_num)  # Print the smallest number

#*****************************************************************************************************************
#Output:
'''The largest number is: 67
The smallest number is: 1'''
#*****************************************************************************************************************

#----------------------------------------------------------------------------------------------
#3. Write a Python program to find duplicate values from a list and display those. 
# Define a list 'a' with some duplicate and unique elements
#---------------------------------------------------------------------------------------------

original_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]  # Define the original list containing integer elements with duplicates.
duplicate_items = set()  # Create an empty set to store duplicate items.
unique_items = []  # Create an empty list for unique items.
for duplicate in original_list:  # Iterate through each element in the original list.
    if duplicate not in duplicate_items:  # Check if the current element is not a duplicate.
        unique_items.append(duplicate)  # Add the element to the list of unique items.
        duplicate_items.add(duplicate)  # Add the element to the set of duplicate items.
print("Duplicate items:", duplicate_items)  # Print the set of duplicate items.

#*****************************************************************************************************************
#Output:
'''Duplicate items: {40, 10, 80, 50, 20, 60, 30}'''
#*****************************************************************************************************************

#---------------------------------------------------------------------------------------------
#4. Write a Python program to split a given list into two parts where the length of the first part of the list is given
#Original list: [1, 1, 2, 3, 4, 4, 5, 1] 
#Length of the first part of the list: 3 
#Splitted the said list into two parts: 
#([1, 1, 2], [3, 4, 4, 5, 1])
#---------------------------------------------------------------------------------------------
original_list=[1, 1, 2, 3, 4, 4, 5, 1] 
def splitted_list():  # Define a function to split the list into two parts.
    first_sub_list = original_list[:3]  # Define the first sub-list containing the first three elements.
    second_sub_list = original_list[3:]  # Define the second sub-list containing the remaining elements.
    return first_sub_list, second_sub_list  # Return the two sub-lists.
print(splitted_list())  # Call the function to split the list and print the result.

#****************************************************************************************************************
#Output:
'''([1, 1, 2], [3, 4, 4, 5, 1])'''
#****************************************************************************************************************

#-------------------------------------------------------------------------------------------------
#5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
#Original list: ['red', 'green', 'white', 'black'] Traverse the said list in reverse order:
#black 
#white
#green
#red
#-----------------------------------------------------------------------------------------------

original_list = ["red", "green", "white", "black"]  # Define the original list containing string elements.
print("Original list:", original_list)  # Print a message indicating the original list of colors.
print("\nTraverse the said list in reverse order:")  # Print a message indicating the traversal of the list in reverse order.
for element in reversed(original_list):  # Use the 'reversed' function to iterate over the 'original_list' in reverse order.
    print(element)  # Print each color element.
print("\nTraverse the said list in reverse order with original index:")  # Print a message indicating the traversal of the list in reverse order with the original index.
for index, element in enumerate(reversed(original_list)):  # Use 'enumerate' in conjunction with 'reversed' to iterate over the 'original_list' in reverse order.
    print(element, 'at', len(original_list) - 1 - index)  # Print the original index and the corresponding color element


#*****************************************************************************************************************
#Output:
'''Original list: ['red', 'green', 'white', 'black']

Traverse the said list in reverse order:
black
white
green
red

Traverse the said list in reverse order with original index:
black at 3
white at 2
green at 1
red at 0'''
#*****************************************************************************************************************

#-----------------------------------------------------------------------------------------------    


