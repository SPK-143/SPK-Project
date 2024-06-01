#--------------------------------------------------Lab 3---------------------------------------

#----------------------------------------------------------------------------------------------
#1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd
a=int(input('enter a number:'))
b='Even' if a%2==0 else 'Odd'
print(b)
#-----------------------------------------------------------------------------------------------
#2. Using input function take two number and then swap the number
p=int(input('enter 1st number:'))
q=int(input('enter 2nd number:'))                       
print('U entered this numbers:',p,q)                                
p,q=q,p
print("swapped numebers:",p,q)
#-----------------------------------------------------------------------------------------------
#3. Write a Program to Convert Kilometers to Miles
km=float(input('enter the distance in  kilometer(s):'))
miles=km*0.621
print(f'{km} kilometeres equal to the {miles:.2f} miles.')
#-----------------------------------------------------------------------------------------------
#4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.
def simple_interest():
    principal_amount=int(input('enter a intial amount:'))
    rate_of_interest=int(input('enter the percentage value:'))
    time_period=int(input('enter the time period in years:'))
    interest= principal_amount*rate_of_interest*time_period
    print(f"Simple Interest for Rs.{principal_amount:} at {rate_of_interest:}% for {time_period} years is : Rs.{interest:.2f}  ")
    return interest
simple_interest()
#-----------------------------------------------------------------------------------------------

