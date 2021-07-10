# This program demonstrates flow control statements.

# while loops for input validation
name = ""
while name != "your name":
    print("To continue, please type your name.")
    name = input()
print("Thank you.")

# break statement
capital = ""
while True:
    print("What is the capital of Georgia?")
    capital = input()
    if capital == "Tbilisi":
        break
print("You are correct.")

# if else statement
print("Please enter your password:")
password = input()
if password == "swordfish":
    print("Access granted.")
if password == "":
    print("You did not enter a password.")
else:
    print("Access denied.")

