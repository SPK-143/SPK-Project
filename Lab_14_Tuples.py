#-----------------------------------------------Lab 13----------------------------------------

#---------------------------------------------------------------------------------------------

#1. Write a Python program to find the number of times 4 appears in the tuple.
#Input: tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 ) 
#Output: 3
#---------------------------------------------------------------------------------------------
def count_tuple(tuplex):
    # Initialize count to keep track of the number of times 4 appears
    count = 0
    # Number to count occurrences of
    number_counted = 4
    # Loop through each element in the tuple
    for counted_number in tuplex:
        # Check if the current number is equal to the number we are counting
        if counted_number == number_counted:
            # Increment count if the condition is met
            count += 1
    return count
# Print the result of the count_tuple function
print(count_tuple( (2, 4, 5, 6, 2, 3, 4, 4, 7) ))

#********************************************************************************************************************
#output:
3
#*********************************************************************************************************************

#---------------------------------------------------------------------------------------------

#2.Write a Python program to convert a list to a tuple.
#Input: listx = [5, 10, 7, 4, 15, 3] 
#Output: (5, 10, 7, 4, 15, 3)

def convert_list(listx):
    # Convert the list to a tuple
    tuplex = tuple(listx)
    return tuplex
# Print the result of the convert_list function
print(convert_list([5, 10, 7, 4, 15, 3]))

#********************************************************************************************************************
#output:
(5, 10, 7, 4, 15, 3)
#*********************************************************************************************************************

#---------------------------------------------------------------------------------------------
#3. Write a Python program to calculate the sum of the numbers in a given tuple.
#Input: tuples_list = [(1, 2), (3, 4), (5, 6)]
#---------------------------------------------------------------------------------------------
def tuplex_sum(tuples_list):
    # Initialize sum_tuples to keep track of the sum
    sum_tuples = 0
    # Loop through each tuple in the list
    for tuple_value in tuples_list:
        # Loop through each number in the tuple
        for number_value in tuple_value:
            # Add the number to the sum
            sum_tuples += number_value
    return sum_tuples
# Print the result of the tuplex_sum function
print(tuplex_sum([(1, 2), (3, 4), (5, 6)]))

#********************************************************************************************************************
#output:
21
#*********************************************************************************************************************

#---------------------------------------------------------------------------------------------

#4.Write a python program and iterate the given tuples
#Input:
#employee1 = ("John Doe", 101, "Human Resources", 60000) 
#employee2 = ("Alice Smith", 102, "Marketing", 55000) 
#employee3 = ("Bob Johnson", 103, "Engineering", 75000)

def iterate_tuple():
    # Iterate over the given tuples
    for name, id, department, salary in employee1, employee2, employee3:
        # Print name and salary of each employee
        print(name)
# Define the employee tuples
employee1 = ("John Doe", 101, "Human Resources", 60000) 
employee2 = ("Alice Smith", 102, "Marketing", 55000) 
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# Call the iterate_tuple function
iterate_tuple()

#********************************************************************************************************************
#output:
John Doe
Alice Smith
Bob Johnson
#*********************************************************************************************************************
#---------------------------------------------------------------------------------------------
