emptyTuple = ()

brothers = ('Arijit','Debrath')
sisters = ('Apurba',)

siblings = brothers+sisters

noofSiblings = len(siblings)

parents = ('Ma','Papa')
family_members = siblings+parents


(firstSibling, secondSibling, thirdSibling, firstparent, secondParent) = family_members 

fruits  = ('apples','mangoes','bananas')
vegetables = ('potatoes','cauliflower')
animal_products = ('egg','milk')
food_stuff_tp = fruits+vegetables+animal_products

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# Unpack siblings and parents from family_members
# print(family_members)
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# How many siblings do you have?
# Join brothers and sisters tuples and assign it to siblings
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# Create an empty tuple
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
midNumber = int((len(food_stuff_lt))/2)

# Slice out the first three items and the last three items from food_staff_lt list
sList = food_stuff_lt[:3]+food_stuff_lt[4:]

# Delete the food_staff_tp tuple completely
del(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
N = 'Estonia'
res = False 
for ele in nordic_countries : 
    if N == ele : 
        res = True
        break

# Check if 'Iceland' is a nordic country
N = 'Iceland'
res = False 
for ele in nordic_countries : 
    if N == ele : 
        res = True
        break

print("Does tuple contain required value ? : " + str(res))