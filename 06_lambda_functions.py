# ============================================
# 6. Lambda Functions
# ============================================
# Topics: lambda, map()
#
# Lambda = anonymous function (one-liner, no name needed)
#
# Syntax: lambda arguments: expression
#   - No def keyword needed
#   - No return keyword needed
#   - Can be stored as a variable for reuse
#   - Can have multiple arguments
#
# map(): applies a function to every item in an iterable
#   - map(function, iterable)
#   - Returns a map object (use list() to see results)
#
# Lambda with if/else:
#   lambda x: value_if_true if condition else value_if_false
#   NOTE: no colon after else (unlike regular if/else blocks)
# ============================================


# --- Examples ---

# Basic lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple arguments
power = lambda x, y: x ** y
print(power(2, 3))  # 8

# Lambda with if/else
pass_fail = lambda score: "Pass" if score >= 60 else "Fail"
print(pass_fail(85))   # Pass
print(pass_fail(45))   # Fail

# Using lambda directly (anonymous)
print((lambda x: x * 2)(10))  # 20

# map() with lambda
names = ["yael", "noam", "tamar"]
capitalized = list(map(lambda x: x.capitalize(), names))
print(capitalized)  # ['Yael', 'Noam', 'Tamar']


# ============================================
# EXERCISES
# ============================================

# Exercise 1:
# Write a lambda called "double" that takes a number and returns it doubled.
# Test it with double(7)
# Your code here:
double = lambda x: x * 2
print(double(7))

# Exercise 2:
# Write a lambda called "add" that takes two numbers and returns their sum.
# Test it with add(3, 5)
# Your code here:
add = lambda x , y : x + y
print(add(3, 5))

# Exercise 3:
# Write a lambda called "classify_temp" that takes a temperature and returns:
#   "Hot" if above 30
#   "Cold" if below 15
#   "Nice" for everything else
# Hint: you can nest if/else like: a if cond1 else b if cond2 else c
# Test with: classify_temp(35), classify_temp(10), classify_temp(22)
# Your code here:
classify_temp = lambda temp : "hot" if temp > 30 else "cold" if temp < 15 else "nice"
print(classify_temp(35))
print(classify_temp(10))
print(classify_temp(22))

# Exercise 4:
# Given this list:
prices = [10.5, 23.0, 7.99, 45.0, 12.75]
# Use map() with a lambda to add 20% tax to each price.
# Print the result as a list.
# Your code here:
print(list(map(lambda x: round(x * 1.2,2), prices)))

# Exercise 5:
# Given this list:
words = ["hello", "WORLD", "Python", "CODE"]
# Use map() with a lambda to convert each word to lowercase.
# Print the result as a list.
# Your code here:
print(list(map(lambda word : word.lower(), words)))

# Exercise 6:
# What is the difference between a lambda function and a regular function?
# When would you use one over the other?
# Write your answer as a comment.
# Answer: a lambda function is an anonymous function and used on a simple function,
# a regular function is used when the function is more complicated and used multiple times.