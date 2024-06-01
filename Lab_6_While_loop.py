#----------------------------------Lab 5------------------------------------------------------
#---------------------------------------------------------------------------------------------

#1. Write a python program to reverse a number using a while loop.

''''Defined a function and called get_reverse_number() and using while loop I reversed the number''''
def get_reverse_number(number_input):
    reverse_number=0
    while number_input!=0:
        last_digit=number_input%10
        reverse_number=reverse_number*10+last_digit
        number_input=number_input//10
    print('The reversed number is:',reverse_number)   
get_reverse_number(int(input('enter a 2 digit or more digit integer number to reverse it:')))

#*******************************************************************************************************************
#output:
''''enter a 2 digit or more digit integer number to reverse it:143
The reversed number is: 341''''
#*******************************************************************************************************************
#---------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------
#2. Write a python program to check whether a number is palindrome or not?

'''defined a function and called palindrome_or_not() and using while loop i checked whether the word is palindrome or not'''
def palindrome_or_not(enter_palindrome):
    while True:
        if enter_palindrome==enter_palindrome[::-1]:
            print(f'{enter_palindrome} is a Palindrome')
            break
        else:
            print(f'{enter_palindrome} is not a Palindrome')
            break
palindrome_or_not(input('enter a word:'))

#*******************************************************************************************************************
#output:
'''enter a word:Amor
Amor is not a Palindrome'''
#*******************************************************************************************************************

#---------------------------------------------------------------------------------------------

#3. Write a python program finding the factorial of a given number using a while loop.

''''defined a funcion and called find_factorial() and using while loop i calculated the factorial of the given number''''
def find_factorial(number_enter):   
    factorial=1
    while number_enter>0:
        factorial*=number_enter
        number_enter-=1
    print('the factorial of the number is :',factorial)
find_factorial(int(input('enter a number to find factorial:')))

#*******************************************************************************************************************
#output
''''enter a number to find factorial:8
the factorial of the number is : 40320''''
#*******************************************************************************************************************
        
#---------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------
#4. Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.

''''I defined a function and called continue_to_zero() and using infinite while loop I calcualed the sum of entered numbers''''
def continue_to_zero():
    first_number=0
    sum=0
    while True:
        first_number=int(input('enter a number (if you want to get sum of your entered numbers then give 0 as your input):'))
        if first_number==0:
            break
        sum+=first_number
    print('the sum of entered numbers is;',sum)
continue_to_zero()

#*******************************************************************************************************************
#output
''''enter a number (if you want to get sum of your entered numbers then give 0 as your input):123
enter a number (if you want to get sum of your entered numbers then give 0 as your input):321
enter a number (if you want to get sum of your entered numbers then give 0 as your input):1234
enter a number (if you want to get sum of your entered numbers then give 0 as your input):852
enter a number (if you want to get sum of your entered numbers then give 0 as your input):0
the sum of entered numbers is; 2530''''

#---------------------------------------------------------------------------------------------        

