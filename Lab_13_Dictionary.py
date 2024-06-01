#---------------------------------------------------Lab 13------------------------------------------------------------------------------------------------------------
#1. Write a Python program and calculate the mean of the below dictionary. 
#test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 
#Output: 6.2
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def calculate_dictionary_mean(test_dict):
    test_values = []   # Initialize an empty list to store dictionary values
    test_length = 0    # Initialize a variable to store the length of values
    test_sum = 0       # Initialize a variable to store the sum of values   

    for value in test_dict.values():    # Iterate over values of the dictionary
        test_values+=str(value)       # Append each value to test_values
        test_length += 1                # Increment test_length for each value
        test_sum += value               # Sum up all values of the dictionary    

    return (f"The values are: {test_values}\n"      # Return a formatted string with calculated values
            f"the number of values is: {test_length}\n"
            f"the sum of values is: {test_sum}\n"
            f"the average of dictionary values is: {test_sum / test_length}")

# Test the function with a sample dictionary
print(calculate_dictionary_mean({"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}))


#*************************************************************************************************************************************************************************************************************************
#output:
'''The values are: ['6', '9', '5', '7', '4']
the number of values is: 5
the sum of values is: 31
the average of dictionary values is: 6.2'''
#*************************************************************************************************************************************************************************************************************************

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#2.Write a Python script to concatenate the following dictionaries to create a new one. Sample Dictionary : 
#dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60}

def concatenate_dictionaries(dic1, dic2, dic3):                                     #"""""Here we can use update() also to concatenate dictionaries''''''''''''''
    return f'the new dictionary is : { {**dic1, **dic2, **dic3} }'               # Return a tuple containing a string message and a new dictionary created by merging dic1, dic2, and dic3
print(concatenate_dictionaries({1:10, 2:20}, {3:30, 4:40}, {5:50, 6:60}))       # Call the concatenate_dictionaries function with three dictionaries as arguments


#*************************************************************************************************************************************************************************************************************************
#output:
'''the new dictionary is : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''
#*************************************************************************************************************************************************************************************************************************
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#3.Write a Python program to get the key, value and item in a dictionary. 
#input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def get_dict(dict_num):
    return (f"the keys in the dictonaries are: {dict_num.keys()}\n"
            f"the values in the dictinaries are: {dict_num.values()}\n"
            f"the key value pairs in the dictionaries are: {dict_num.items()}\n")
print(get_dict({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}))                     # Call the get_dict function with a dictionary as an argument and print the result
                
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#*************************************************************************************************************************************************************************************************************************
#output:
'''the keys in the dictonaries are: dict_keys([1, 2, 3, 4, 5, 6])
the values in the dictinaries are: dict_values([10, 20, 30, 40, 50, 60])
the key value pairs in the dictionaries are: dict_items([(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60)])'''
#***********************************************************************************************************************************************************************************************************************

    
