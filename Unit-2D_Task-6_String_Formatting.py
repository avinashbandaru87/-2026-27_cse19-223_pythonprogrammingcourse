# Unit-2D_Task-6_String_Formatting.py

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

# String Formatting
print("Name: {}".format(name))
print("Age: {}".format(age))
print("Marks: {:.2f}".format(marks))

# Using f-strings
print(f"\nStudent Name: {name}")
print(f"Student Age: {age}")
print(f"Student Marks: {marks:.2f}")