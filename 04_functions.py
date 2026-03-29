# ============================================
# 4. Functions
# ============================================
# Topics: def, return, arguments, default arguments,
#         keyword arguments, *args, **kwargs, docstrings
#
# Functions let you write reusable blocks of code.
#
# def function_name(arguments):
#     """Docstring — describes what the function does."""
#     # function body
#     return result
#
# Positional arguments: provided in order
# Keyword arguments: provided by name (keyword=value)
# Default arguments: have a fallback value if not provided
# *args: accepts any number of positional arguments (becomes a tuple)
# **kwargs: accepts any number of keyword arguments (becomes a dict)
#
# Docstrings: text inside triple quotes describing the function
#   - Access with help(function_name) or function_name.__doc__
# ============================================


# --- Examples ---

# Basic function
def average(values):
    """Calculate the average of a list of numbers."""
    avg = sum(values) / len(values)
    return avg

print(average([10, 20, 30]))  # 20.0

# Default argument
def average_rounded(values, rounded=False):
    """Calculate the average, optionally rounded to 2 decimals."""
    avg = sum(values) / len(values)
    if rounded:
        return round(avg, 2)
    else:
        return avg

print(average_rounded([10, 23, 37]))        # Not rounded
print(average_rounded([10, 23, 37], rounded=True))  # Rounded

# Arbitrary positional arguments (*args)
def average_args(*args):
    """Calculate the average of any number of arguments."""
    avg = sum(args) / len(args)
    return round(avg, 2)

print(average_args(15, 29, 4, 13, 11, 8))  # 13.33

# Arbitrary keyword arguments (**kwargs)
def average_kwargs(**kwargs):
    """Calculate the average of keyword argument values."""
    avg = sum(kwargs.values()) / len(kwargs.values())
    return round(avg, 2)

print(average_kwargs(math=90, english=80, science=85))  # 85.0

# Accessing docstring
print(average.__doc__)


# ============================================
# EXERCISES
# ============================================

# Exercise 1:
# Write a function called "greet" that takes a name
# and returns "Hello, [name]!"
# Include a docstring.
# Test it with your name.
# Your code here:
def greet(name):
     """Return a greeting message for the given name.

    Args:
        name (str): The person's name.

    Returns:
        str: A greeting in the format 'Hello, name!'"""
     return "Hello, " + name
print(greet("Omri"))

# Exercise 2:
# Write a function called "is_passing" that takes a score
# and a passing_threshold with a default value of 60.
# Return True if the score >= threshold, else False.
# Test it with: is_passing(55), is_passing(55, 50), is_passing(75)
# Your code here:
def is_passing(score,passing_threshold=60):
    if score >= passing_threshold:
        return True
    else:
        return False
print(is_passing(55))
print(is_passing(55,50))
print(is_passing(75))


# Exercise 3:
# Write a function called "total" that uses *args
# to accept any number of numbers and returns their sum.
# Test it with total(1, 2, 3) and total(10, 20, 30, 40, 50)
# Your code here:
def total(*args):
    sum_args = sum(args)
    return sum_args
print(total(1,2,3))
print(total(10, 20, 30, 40, 50))

# Exercise 4:
# Write a function called "student_info" that uses **kwargs
# and prints each key-value pair on a new line like:
# "name: Yael"
# "age: 22"
# Test it with student_info(name="Yael", age=22, grade="A")
# Your code here:
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
student_info(name="Omri", age=30, grade="A")

# Exercise 5:
# Write a function called "describe_number" with a multi-line docstring.
# The function takes a number and returns:
#   - "positive" if > 0
#   - "negative" if < 0
#   - "zero" if == 0
# The docstring should include: summary, Args, Returns
# Your code here:
def describe_number(num):
    """Return if the number is positive, negative or zero.
    Args:
        num (int): The number
    Returns:
        str: 'positive', 'negative', or 'zero'"""
    if num > 0:
        return "positive"
    elif num == 0:
        return "zero"
    else:
        return "negative"

# Exercise 6:
# What is the difference between return and print in a function?
# Write your answer as a comment.
# Answer: return gives the value silently, print displays it on the screen.
