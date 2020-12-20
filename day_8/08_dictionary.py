# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'Captain','color':'Beige','breed':'labrador','Legs':4,'Age':'1 Year'}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'Priyanshu','last_name':'Chatterjee','gender':'Male','age':19,'maritial status':'single','skills':['CPP','Python','Javascript'],'country':'India','city':'Chandannagar','address':'Nimtala Road, Bhakunda'}

# Get the length of the student dictionary
# print(len(student))

# Get the value of skills and check the data type, it should be a list
lst = [student['skills'],type(student['skills'])]

# Modify the skills values by adding one or two skills
student['skills'].append('Blogger')

print(student.keys())

print(student.values())

items_student = student.items()
print(items_student)

student_dict.popitem()
print(student)

del dog
