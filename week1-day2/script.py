# Dictionary Operations

student = {}
print(student)

# Insert
student["name"] = "Ahmed"
student["age"] = 25
student["cgpa"] = 3.6
print(student)

# Access
print(student["age"])
print(student.get("age"))

# Update
student["cgpa"] = 3.8
print(student)

# Delete
del student["cgpa"]
print(student)

# Search
print("cgpa" in student)
print("age" in student)

# Traverse
for key, value in student.items():
  print(key, value)
  
# Size
print(len(student))






# Comparing Lists and Dictionaries

names = ['Ahmed', 'Ali', 'Fahad']
ages = [25, 26, 27]
cgpa = [3.4, 3.5, 3.6]

print(names[0])
print(ages[0])
print(cgpa[0])

student1 = {
  'name': 'Ahmed',
  'age': 25,
  'cgpa': 3.4
}
student2 = {
  'name': 'Ali',
  'age': 25,
  'cgpa': 3.4
}
student3 = {
  'name': 'Fahad',
  'age': 25,
  'cgpa': 3.4
}

print(student2)

