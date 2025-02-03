# Input values
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")
fullname = fname + " " + lname

# Output
print("Full name: ", fullname)
print("Sliced name: ", fname[:])
print("Greeting message: Hello, {}! Welcome. You are {} years old.".format(fname[:4], age))