#---------------------------------------------Lab 15------------------------------------------

# 1. Write a Python program to Get Only unique items from two sets. 
# Input: 
# set1 = {10, 20, 30, 40, 50} 
# set2 = {30, 40, 50, 60, 70} 
# Output: {70, 40, 10, 50, 20, 60, 30}

#----------------------------------------------------------------------------------------------

def unique_items(set1, set2):
    # Use set union operator (|) to combine elements from both sets
    items_unique = set1 | set2
    return items_unique

# Example input sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Print unique items from both sets
print(unique_items(set1, set2))

#*********************************************************************************************************************
#output:
'''{70, 40, 10, 50, 20, 60, 30}'''
#*********************************************************************************************************************

#----------------------------------------------------------------------------------------------

# 2. Write a Python program to Return a set of elements present in Set A or B, but not both.
# Input: 
# set1 = {10, 20, 30, 40, 50} 
# set2 = {30, 40, 50, 60, 70}
# Output: {20, 70, 10, 60}
#----------------------------------------------------------------------------------------------
def return_equal(set1, set2):
    # Use set symmetric difference operator (^) to find elements present in either set, but not both
    items_equal = set1 ^ set2
    return items_equal

# Example input sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Print elements present in either set, but not both
print(return_equal(set1, set2))

#*********************************************************************************************************************
#output:
'''{20, 70, 10, 60}'''
#*********************************************************************************************************************

#----------------------------------------------------------------------------------------------

# 3. Write a Python program to Check if two sets have any elements in common. If yes, display the common elements. 
# Input: 
# set1 = {10, 20, 30, 40, 50} 
# set2 = {60, 70, 80, 90, 10} 
# Output: {10}
#----------------------------------------------------------------------------------------------
def set_common(set1, set2):
    # Use set intersection operator (&) to find common elements between sets
    common_set = set1 & set2
    return common_set

# Example input sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Print common elements between sets
print(set_common(set1, set2))

#*********************************************************************************************************************
#output:
'''{10}'''
#*********************************************************************************************************************

#----------------------------------------------------------------------------------------------

# 4. Write a Python program to Remove items from set1 that are not common to both set1 and set2.
# Input: 
# set1 = {10, 20, 30, 40, 50} 
# set2 = {30, 40, 50, 60, 70} 
# Output: {40, 50, 30}
#----------------------------------------------------------------------------------------------
def remove_set(set1, set2):
    uncommon_set = set()
    # Iterate through elements in set1
    for element in set1:
        # Check if element is present in set2
        if element in set2:
            # If yes, add element to uncommon_set
            uncommon_set |= {element}
    return uncommon_set

# Example input sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Update set1 with common elements
set1 = remove_set(set1, set2)

# Print the updated set1
print("The updated set 1 is:", set1)

#*********************************************************************************************************************
#output:
'''The updated set 1 is: {40, 50, 30}'''
#*********************************************************************************************************************
#----------------------------------------------------------------------------------------------
