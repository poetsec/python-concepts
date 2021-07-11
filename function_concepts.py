def hello(name):
    print("Hello" + name)
    print("Hello!!")
    print("Hello there.")

hello("alice")

def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)

# keyword arguments
print("hello", end="")
print("world")

# the sep= keyword argument allows us to change the value of the spaces
print("cat", "dog", "mouse" sep="ABC")

# there are two local scopes here refering to two different egg variables
# one exists in bacon()'s local scope, and one exists in spam()'s local scope
# local scopes can't use variables in other local scopes
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()
# eggs in spam can only refer to eggs in spam. Never to eggs in bacon
