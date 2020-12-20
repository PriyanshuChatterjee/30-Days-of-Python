import math

# Declare your age as integer variable
myAge = 19

# Declare your height as a float variable
myHeight = 182

# Declare a complex number variable
complexNum = 3+4j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle
base = float(input("Enter the base of the triangle"))
height = float(input("Enter the height of the triangle"))
area = 0.5*base*height

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle
firstSide = float(input("Enter the first side of the triangle"))
secondSide = float(input("Enter the second side of the triangle"))
thirdSide = float(input("Enter the third side of the triangle"))
perimeter = firstSide+secondSide+thirdSide

# # Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter
length = float(input("Enter the length of the rectangle"))
breadth = float(input("Enter the breadth of the rectangle"))
rectanglePerimeter = 2*(length+breadth)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter the radius of the circle"))
cicleArea = math.pi*radius*radius

# Calculate the slope, x-intercept and y-intercept of y = 2x -2


# Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point (6,10)
x1, x2, y1, y2 = 2, 6, 2, 10

slope = (y2 - y1)/(x2 - x1)
print("The slope is: ",slope)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.
x = int(input("Enter the value of x: "))
y = x * x + 6 * x + 9
print("The value of y is: ", y)

# Find the length of 'python' and 'jargon' and make a falsy comparison statement.
str1 = "python"
str2 = "jargon"

if str1 == str2:
    print("True")
else:
    print("False")

# Hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
str3 = "I hope this course is not full of jargon"
if 'jargon' in str3:
    print("The string is present")
else:
    print("The string is not present")    

# There is no 'on' in both dragon and python
str4 = "dragon"
str5 = "python"


if 'on' not in str4 and str5:
    print('There is no on in dragon and python')

else:
    print("On is present in dragon and python") 

# Find the length of the text python and convert the value to float and convert it to string
str6 = "python"
len_str6 = float(len(str6))
len_str6_tostring = str(len(str6))
print(len_str6)       
print(len_str6_tostring)       

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input("Enter the number: "))

if num % 2 == 0:
    print("The number is even")

else:
    print("The number is odd")    

# The floor division of 7 by 3 is equal to the int converted value of 2.7.
print(int(7//3))

# Check if type of '10' is equal to 10
if type('10') == type(10):
    print("True")

else:
    print("False") 
   
# Check if int('9.8') is equal to 10
a = '9.8'
int_a = int(a)

if int_a == 10:
    print("True")

else:
    print("False")   

# Output is an error     


# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person
hours = int(input("Enter hours: "))
rate_per_hours = int(input("Enter rate per hour: "))
earnimg = hours * rate_per_hours

print("Your weekly earning is", earnimg)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume someone lives up to hundred years
years = int(input("Enter number of years you have lived: "))

seconds_lived = years * 365 * 24 * 60 * 60
print("You have lived for ",seconds_lived, "seconds")

# Write a python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)
