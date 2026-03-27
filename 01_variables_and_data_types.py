# ============================================
# 1. Variables & Data Types
# ============================================
# Topics: str, int, float, bool, type()
#
# Variables store and reuse information.
# Python assigns data types automatically.
# Use type() to check what data type a variable is.
#
# Data Types:
#   - str: text values in quotes ("hello", 'world')
#   - int: whole numbers (5, -3, 100)
#   - float: decimal numbers (3.14, -0.5)
#   - bool: True or False (capitalized, no quotes)
# ============================================


# --- Examples ---

# String
recipe_name = "20-minute pasta"
print(type(recipe_name))  # <class 'str'>

# Integer
servings = 4
print(type(servings))  # <class 'int'>

# Float
prep_time = 20.5
print(type(prep_time))  # <class 'float'>

# Boolean
is_vegetarian = True
print(type(is_vegetarian))  # <class 'bool'>

# Strings with apostrophes — use double quotes
chef_special = "Chef's secret seasoning"


# ============================================
# EXERCISES
# ============================================

# Exercise 1:
# Create a variable called "city" and assign it the string "Haifa"
# Print its type.
# Your code here:
city = "Haifa"
print(type(city))

# Exercise 2:
# Create a variable called "temperature" and assign it the float 28.5
# Create a variable called "is_hot" and assign it True
# Print both variables and their types.
# Your code here:
temperature = 28.5
is_hot = True
print(type(temperature))
print(type(is_hot))

# Exercise 3:
# What is the output of the following code? Write your answer as a comment, then run it to check.
x = "42"
print(type(x))
# Answer: string

# Exercise 4:
# Create variables for a product in a store:
#   - product_name (str)
#   - price (float)
#   - quantity_in_stock (int)
#   - is_available (bool)
# Print each variable with its type.
# Your code here:
product_name = "Pasta"
price = 10.5
quantity_in_stock = 20
is_available = True
print(type(product_name))
print(type(price))
print(type(quantity_in_stock))
print(type(is_available))

# Exercise 5:
# What is the difference between 42, 42.0, and "42"?
# Write your answer as a comment.
# Answer: 42 = int, 42.0 = float, "42" = str
