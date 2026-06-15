student ={
    "name":"Maruf",
    "age":22,
    "department":"CSE",
    "cgpa":3.78
}

print(student)
print(type(student))
print("\n")


#keys
print(student.keys())
print("\n")


#Different
for key in student:
    print(key, student[key])
print("\n")


for val in student.values():
    print(val)
print("\n")

for key,val in student.items():
    print(key,val)
print("\n")

