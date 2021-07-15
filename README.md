# python-concepts
This repository contains Python files demonstrating basic Python concepts.

## Notes
These are my notes on basic Python concepts taken during beginner Python courses such as Al Sweigart's course: Automate the Boring Stuff with Python Programming.

## Flow Control

### Booleans
- Boolean data types are true or false. 
- Comparison operators are `==`, `!=`, `<`, `>`, `<=`, and `>=`.
- `==` is comparison, `=` is assignment.
- Boolean operators: `and`, `or`, `not`.

### If, Else, and Elif Statements
- An if statement can be used to conditionally execute code, depending on whether or not the if statement's condition is `True` or `False`.
- An `elif` (as in, "else if") statement can follow an if statement. Its block executes if its condition is true and all of the previous conditions have been false.
- The values 0, 0.0, and an empty string are considered to be "falsey" values. They are considered false when used in conditions. 

### While Loops
- When the execution reaches the end of a while statement's block, it jumps back to the start to re-check the condition. 
- You can press `ctrl + C` to get out of an infinite loop.
- A break statement causes the program execution to immediately leave the loop without re-checking the condition.
- A continue statement causes the executuion to immediately jump back to the start of the loop and re-check the condition.

### For Loops
- For loops will loop a specific number of times.
- The `range()` function with a certain number will loop that number of times. 
- With a `range()` function with two arguments, you can set a starting integer and an ending integer.
- The `range()` function called with three arguments includes a starting integer, an ending integer, and a step argument which is how much the for loops's variable increases each time. 

## Functions
Python has built-in functions that all Python programs can call. These include `input()`, `len()`, and `print()`. Python also comes with a set of modules called the standard library. Each module is a Python program that includes related functions that can be used in Python programs. You must import a module with an import statement before you can use its functions.

### Modules
- to call a function from a certain module, you must first import the module. For example, `import random`. Then, you must type the module name followed by a period to call the function, telling Python to look inside that module for the function. For example `random.randint`. Randint isn't a built-in function and only exists in the random module, which is why you have to have the `random.` before the function name itself.
- You can import multiple modules in a line of code by seperating the module names with commas in the import statement. For example `import random, sys, os, math`.
- Another way to import a module would be `from module_name import *`. The star tells Python to import everything. You would import a module this way so you don't have to type the `module_name.` before the function every time. However, using the full name makes for more readable code because you can see which module the function comes from.

### Third-Party Modules
- Python can also install third-party using the `pip` command.
- `pip` must be run from the terminal/commandline.
- The third-party module pyperclip has `copy()` and `paste()` functions for reading and writing large amounts of text to and from the clipboard.

### Writing Functions
- Functions are like mini programs inside of the program.
- The `def()` statement only defines a function. It does not execute the code inside of it, and will skip its block when the function is first defined. The code inside the function will only run when the function is called.
- The main purpose of functions is to define code that needs to be run multiple times into a group that can be easily called when needed. 
- Using functions prevents the need to rewrite the same code over and over.
- Avoiding duplicating code is also useful when debugging and updating. Using a function makes it so only that function needs to be edited, and we don't have to search through the entire program to find each time we used that same block of code that needs to be changed.
- An argument is the value passed when calling a function. A parameter is the variable inside the function.
- Keyword arguments are often used for optional arguments to pass to a function call. The `print()` function has the keyword arguments `end=` and `sep=`.
- Functions that return without a return statement return the `None` value.

### Global and Local Scopes
- A variable in a function can have the same name as a variable outside of the function, but they are considered two seperate variables.
- Local variables are variables inside of a function i.e. in the local scope of the function. Global variables are variables in any area of the source code i.e. the global scope of the code. 
- Global and local scopes can be thought of global and local containers. A variable can't be in both the global and local scope. 
- Local variables, or variables in the local scope, are forgotten when that function ends. So in a sense, local variables are temporary. They won't exist after the function returns.
- Code in a global scope can't use variables in the local scope, but code in a local scope can use global variables. Code in one function's local scope cannot use functions in another function's local scope.
- If there is an assignment statement i.e. `count = 40` in the function, the variable is considered a local variable. If there is no assignment statement, it is considered a global variable. 

## Handling Errors with Try and Except Statements
- `try` and `except` statements can be used to keep a program running to completeion instead of crashing entirely when an error is encountered.
- You can also have a simple `except` statement without specifying the error it catches, and it will catch all types of errors.

## Lists
- A list is a value that contains values in an ordered sequence. The values inside of a list are called items.
- An integer index for an item's position inside of the list is used to access that item i.e. `list[4]` would call the item at index 4. The first item is at index 0.
- Lists start at 0 and go up, but you can also use negative integers. Negative integers start from the end of the list and go forward. `[-1]` refers to the last item in the list. 
- An index calls a single item from a list while a slice calls multiple items from a list. The slice `[1:3]` would start at item 1 and go up to, but not including, item 3. 
- You can leave out the values on either side of the semicolon when creating a slice. Leaving out the value before the semicolon will begin the slice at item 0. Leaving out the value after the semicolon will end the slice with the last item in the list. Leaving out both values will run the slice the entire length of the list.
- There is a list function `list()` that takes a value and splits it up into a list.
