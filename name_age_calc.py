# This program says hello and asks for name and age.
# Makes simple calculations of age and name (length of name, age in five years).

print("Hello!")

print("What is your name?")
name = input()
print("It is nice to meet you, " + name)
name_char_count = len(name)
print("Your name is",  name_char_count, "characters long")

print("How old are you?")
age = input()
print("You will be " +str(int(age) + 5) + " in five years")
