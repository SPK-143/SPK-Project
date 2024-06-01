#--------------------------------------------------Lab 4-----------------------------------------


#------------------------------------------------------------------------------------------------------
#1.     Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

num_input = int(input('Enter a number: '))                                            #usage of input funciton
if num_input==0:
    print('zero is neither even nor odd')
elif num_input % 2 == 0:
    print(f'You entered {num_input} and it is a even number.')                   #usage of print statement to display the number is even
else:
    print(f'You entered {num_input} and it is an odd number.')                  #usage of print statement to display the number is odd

#output
#********************************************************************************************************************************
#********************************************************************************************************************************
#------------------------------------------------------------------------------------------------------
#2.      Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
    
person_input_age=int(input('Hello! Please enter your age to check if you are eligible to vote:'))           #usage of input function to get the age of a person
'''usage of if and conditional statement to decide weather he/she is eligible or not'''
if person_input_age<=0:
    print('enter a valid year')
elif person_input_age>=18:
    print(f'your age is {person_input_age} and you are eligible to vote')
else:
     print(f'your age is {person_input_age} and you are not eligible to vote')                                  #usage of print statement to display the appropriate message according to the age  

#output
#********************************************************************************************************************************
#********************************************************************************************************************************
#------------------------------------------------------------------------------------------------------
#3.      Write a Python program that determines if a given year is a leap year or not
     
'''here I took year as input and checked it using  if and elif condition statments to decide wheather it is a leap year or not'''
given_input_year=int(input('enter a year number:'))
if given_input_year<=0:
    print('enter a valid year')
elif given_input_year %4 ==0 and given_input_year % 100 != 0 or given_input_year % 400 == 0:                                                #using conditon we can check the year is leap year or not
    print(f'{given_input_year} is a leap year')
else:
     print(f'{given_input_year} is not a leap year')
     
#output
#********************************************************************************************************************************
#********************************************************************************************************************************
#------------------------------------------------------------------------------------------------------
#4    Create a Python program that checks if a user-given number is positive, negative, or zero.

user_given_number=int(input('enter a number:'))
if user_given_number==0:                                                    #here i took input from the user and checked it either positive or negaitve or zero usnig if and elif conditonal statements
    print('You entered input as number zero({user_given_input}) and zero is neither positive nor negative number')
elif user_given_number>0:
    print(f'{user_given_number} is a positive number')
else:
    print(f'{user_given_number} is a negative number')
    
#output
#********************************************************************************************************************************
#********************************************************************************************************************************
#------------------------------------------------------------------------------------------------------
#5     Write a Python program that determines the largest of three numbers entered by the user.

#taking 3 inputs from the user using input statements
user_input_number_one=int(input('enter the 1st number:'))
user_input_number_two=int(input('enter the 2nd number:'))
user_input_number_three=int(input('enter the 3rd number:'))
# Finding the largest number using conditional statements
largest = user_input_number_one

if user_input_number_two > largest:
    largeslt = user_input_number_two
if user_input_number_three > largest:
    largest = user_input_number_three
print(f"The largest number is: {largest}")                                            #usage of output statement to display the largest number

#output
#********************************************************************************************************************************
#********************************************************************************************************************************
    
#------------------------------------------------------------------------------------------------------

#4. A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.
#The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.
#On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.
#Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.
#Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''I used dictionary datatype to declare the codes of each product in different category'''
shop_items = {1: 'Battery Based Toys', 2: 'Key-based Toys', 3: 'Electrical Charging based Toys'}
min_order = {1: 1000, 2: 100, 3: 500}
discount_rate = {1: 0.1, 2: 0.05, 3: 0.1}

product_code = int(input('Enter a valid product code (1, 2, or 3): '))
order_amount = float(input('Enter order amount: '))

discount = 0.0
net_amount = order_amount

# Validate product code
if product_code not in shop_items:
    print('Invalid product code. Please enter 1, 2, or 3.')
else:
    # Calculate discount (if applicable)
    if order_amount > min_order[product_code]:
        discount = order_amount * discount_rate[product_code]
    net_amount = order_amount - discount

# Display results
print(f"Product Name: {shop_items.get(product_code, 'Invalid Code')}")  # Handle missing code gracefully
print(f"Discount amount: Rs.{discount:.2f}")
print(f"Net amount payable: Rs.{net_amount:.2f}")
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#A transport company charges the fare according to following table: Distance Charges 1-50 8 Rs./Km 51-100 10 Rs./Km > 100 12 Rs/Km

'''here i defined a function to calculate the distance charges(km) and using elif functions I have included the prices based on distacnce that gets inputed'''

def transport_company_charges():
    distance_desire_travel=float(input('enter the desired distance to travel by you(km):'))
    if distance_desire_travel<=0:
        print('enter a valid distance')
    elif distance_desire_travel>=1 and distance_desire_travel<=50:
        print('Your total distance charge is {distance_desire_travel} * 8 =',distance_desire_travel*8)
    elif distance_desire_travel>=51 and distance_desire_travel<=100:
        print('Your total distance charge is {distance_desire_travel} * 10 =',distance_desire_travel*10)
    elif distance_desire_travel>=100 :
        print('Your total distance charge is {distance_desire_travel} * 12 =',distance_desire_travel*12)
transport_company_charges()
        
