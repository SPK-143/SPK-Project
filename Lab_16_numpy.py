#------------------------------------------Lab 16--------------------------------------------
#1. Convert the below list into numpy array then display the array
#Input: my_list = [1, 2, 3, 4, 5]

def array2list(my_list):
    # Import the NumPy library
    import numpy as np
    
    # Convert the input list to a NumPy array
    array_list = np.array(my_list)
    
    # Return the resulting array
    return array_list

# Call the array2list function with the provided list and print the result
print(array2list([1, 2, 3, 4, 5]))

#2. Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.
#Input: my_list = [1, 2, 3, 4, 5]

def array_product(my_list):
    # Call the array2list function to convert the input list to a NumPy array
    product_array = array2list(my_list)
    
    # Print the NumPy array
    print(product_array)
    
    # Print the first element of the array
    print("\nFirst Element:", product_array[0])
    
    # Print the last element of the array
    print("Last Element:", product_array[-1])
    
    # Multiply each element of the array by 2
    multiplied_array = product_array * 2
    
    # Return the resulting array
    return multiplied_array

# Call the array_product function with the provided list and print the result
print(array_product([1, 2, 3, 4, 5]))

