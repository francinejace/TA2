# Input values
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
fullname = fname + " " + lname
uppername = fullname.upper()
lowername = fullname.lower()
countname = len(fullname.replace(" ", ""))

# Output
print("Full name: ", fullname)
print("Full name in upper case: ", uppername)
print("Full name in lower case: ", lowername)
print("Length of full name: ", countname)