# Input values
lname = input("Enter your last name: ")
fname = input("Enter your first name: ")
age = input("Enter your age: ")
number = input("Enter your contact number: ")
course = input("Enter your course: ")

# File handling
with open("test.txt", "a") as file:
    file.write("Last name: " + lname + "\n")
    file.write("First name: " + fname + "\n")
    file.write("Age: " + age + "\n")
    file.write("Contact number: " + number + "\n")
    file.write("Course: " + course + "\n")
    file.write("\n")

# Output
print("Last name: ", lname)
print("First name: ", fname)
print("Age: ", age)
print("Contact number: ", number)
print("Course: ", course)
print("Student information has been saved to 'students.txt'.")
