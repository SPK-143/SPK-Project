#*********************************************************Python Labs*************************************************
#--------------------------------------------------------------------------------------------
#1. Calculate the multiplication and sum of two numbers

num1=22 #declaration of 1st number
num2=25 #declaration of 2nd number
sum_of_nums=num1+num2 #usage of addition operator
multiplication_of_nums=num1*num2 #usage of multiplication operator
print(sum_of_nums)#gives the output of sum of num1 and num2
print(multiplication_of_nums) #gives the output of product of num1 and num2
#---------------------------------------------------------------------------------------------
#2. Declare two variables and print that which variable is largest using ternary operators

p=2                                                                              #decalaration of 1st number
q=5                                                                               #declation of 2nd number
x=True if  p>q else False                                                    #usage of ternary operator
print(x)                                                                         #usage of print statement which gives output
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#3. Python program to convert the temperature in degree centigrade to Fahrenheit

C=75                                                                                                            #takes the input in the form of Celsius
F=(C*9/5)+32                                                                                                #calculation of conversion of centigrade Fahrenheit 
print('The equivalent Fahrenhiet Value for the entered Centigrade value is: ',F,'F')   #usage of print statement for output
#---------------------------------------------------------------------------------------------
#4. Python program to find the area of a triangle whose sides are given

print("don't give a negative value for the length of any side and follow the condition sum of any 2 sides needed to be less than equals to the 3rd side")
a = 5                                                                                                #length of 1st side of the triangle 
b = 2                                                                                                   #length of  2nd side of the triangle
c = 6                                                                                               #length of  3rd side of the triangle
s = (a + b + c) / 2                                                                                  # calculation of  semi-perimeter
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5                                                            # calculation of area
print('the area of the triangle with {a},{b},{c} as its sides is:',area)                 #usage of print statement to show the result
#----------------------------------------------------------------------------------------------
