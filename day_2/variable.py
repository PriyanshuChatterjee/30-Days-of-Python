import math

#Day 2: 30 Days of python programming
firstName = "Priyanshu"
lastName = "Chatterjee"
fullName = "Priyanshu Chatterjee"
country = "India"
city = "Chandannagar"
age = 19
year = 2001
is_married = False
is_true = True
is_light_on = True

# Check the data type of all your variables using type() built-in function
print(type(firstName))
print(type(lastName))
print(type(fullName))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Using the len() built-in function find the length of your first name
print(len(firstName)) 

# Declare 5 as num_one and 4 as num_two
num_one = 4
num_two = 5
# Add num_one and num_two and assign the value to a variable _total
variable_total = (4+5)
# Subtract num_two from num_one and assign the value to a variable _diff
variable_diff = (4-5)
# Multiply num_two and num_one and assign the value to a variable _product
variable_product = (4*5)
# Divide num_one by num_two and assign the value to a variable _division
variable_division = (4/5)
# Use modulus division to find num_two divided by num_one and assign the value to a variable _remainder
variable_remainder = (5%4)
# Calculate num_one to the power of num_two and assign the value to a variable _exp
variable_exp = (5**4)
# Find floor division of num_one by num_two and assign the value to a variable _floor_division
variable_floor_division = (4//5)

# The radius of a circle is 30 meters
radius = 30

# Calculate the area of a circle and assign the value to a variable area_of_circle
area_of_circle = math.pi*radius*radius
# Calculate the circumference of a circle and assign the value to a variable circum_of_circle
circum_of_circle = 2*(math.pi)*radius
print(circum_of_circle)
# Take radius as user input and calculate the area.
radius = float(input("Enter the radius of the circle"))