# python-concepts
This repository contains Python files demonstrating basic Python concepts.

## Notes
Notes on basic Python concepts taken during Al Sweigart's course: Automate the Boring Stuff with Python Programming.

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
