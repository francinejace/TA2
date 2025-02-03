#Task: Write a Python program that does the following:
# Opens the "students.txt" file in read mode.
# Reads the contents of the file.
# Displays the student information to the user.

print("\nReading Student Information: \n")
with open("students.txt", "r") as file:
    print(file.read())
