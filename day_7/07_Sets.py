# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.update(["Twitter"])
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(["AMD", "Samsung", "Intel"])
print(it_companies)

Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print(it_companies)

# remove() only removes the element from the set if the element is present in the set, otherwise it will show an error. The discard() function removes the element from the set if present, but produces no error, if the element is not present in the set.

# Join A and B
C = A.union(B)
print(C)
print(A.intersection(B))

# Is A subset of B
if A.issubset(B):
    print("True")
else:
    print("False")  

# Are A and B disjoint sets
if A.isdisjoint(B):
    print("True")
else:
    print("False") 

# Join A with B and B with 
D = A.union(B)          
E = B.union(A)
print(D)          
print(E)    

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))  

# Delete the sets completely
del A
del B

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_age = set(age)
print(len(set_age))
print(len(age))


# Explain the difference between the following data types: string, list, tuple and set
# Lists is Mutable	Set is Mutable	Tuple is Immutable
# It is Ordered collection of items	It is Unordered collection of items	It is Ordered collection of items
# Items in list can be replaced or changed	Items in set cannot be changed or replaced	Items in tuple cannot be changed or replaced

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? You did not learn loops yet you can do it manually.
sentence = {"I", "am", "a", "teacher", "and", "I", "love", "to", "inspire", "and", "teach", "people"}
print(len(sentence))