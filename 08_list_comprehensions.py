# ============================================
# 8. List Comprehensions & Dict Comprehensions
# ============================================
# Topics: list comprehensions, conditionals in comprehensions,
#         nested comprehensions, dict comprehensions
#
# List comprehension: build a list in one line
#   Basic: [output_expression for var in iterable]
#   Three components:
#     1. Output expression (what you create)
#     2. Iterator variable (represents each item)
#     3. Iterable (what you loop over)
#
# Conditionals:
#   Filtering (if at END):
#     [x for x in iterable if condition]
#     Only includes items that match — result can be shorter
#
#   Transforming (if/else at START):
#     [x if condition else y for x in iterable]
#     Every item stays — values change based on condition
#
# Nested loops:
#   [expr for var1 in iter1 for var2 in iter2]
#   First for = outer loop, second for = inner loop
#
# Dict comprehension: same idea but with {} and key: value
#   {key: value for var in iterable}
# ============================================


# --- Examples ---

# Basic list comprehension
nums = [12, 8, 21, 3, 16]
new_nums = [num + 1 for num in nums]
print(new_nums)  # [13, 9, 22, 4, 17]

# With range
squares = [num ** 2 for num in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Filtering (if at the end)
evens = [num ** 2 for num in range(10) if num % 2 == 0]
print(evens)  # [0, 4, 16, 36, 64]

# Transforming (if/else at the start)
labels = [num ** 2 if num % 2 == 0 else 0 for num in range(10)]
print(labels)  # [0, 0, 4, 0, 16, 0, 36, 0, 64, 0]

# Nested loops
pairs = [(num1, num2) for num1 in range(2) for num2 in range(6, 8)]
print(pairs)  # [(0, 6), (0, 7), (1, 6), (1, 7)]

# Dict comprehension
pos_neg = {num: -num for num in range(9)}
print(pos_neg)  # {0: 0, 1: -1, 2: -2, ...}


# ============================================
# EXERCISES
# ============================================

# Exercise 1:
# Given this list:
names = ["yael", "noam", "tamar", "ori", "dana"]
# Use a list comprehension to create a new list with all names capitalized.
# Your code here:


# Exercise 2:
# Use a list comprehension to create a list of all numbers from 1 to 50
# that are divisible by 3. (Hint: num % 3 == 0)
# Your code here:


# Exercise 3:
# Given this list:
temperatures = [22, 35, 18, 40, 28, 15, 33]
# Use a list comprehension with if/else to create a list that labels
# each temperature as "Hot" (above 30) or "OK" (30 or below).
# Your code here:


# Exercise 4:
# Use a list comprehension with nested loops to create all combinations
# of colors and sizes:
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
# Result should be: [("red", "S"), ("red", "M"), ("red", "L"), ("blue", "S"), ...]
# Your code here:


# Exercise 5:
# Given these two lists:
students = ["Yael", "Noam", "Tamar", "Ori"]
scores = [92, 65, 95, 45]
# Use a dict comprehension with zip() to create a dictionary
# where keys are names and values are "Pass" or "Fail" (>= 60 is pass).
# Your code here:


# Exercise 6:
# Given this list:
words = ["hello", "hi", "hey", "howdy", "yo", "hola"]
# Use a list comprehension to keep only words with more than 2 characters.
# Then, from that result, use ANOTHER list comprehension to capitalize them.
# Your code here:


# Exercise 7:
# What is the difference between these two?
#   [x for x in items if condition]        (if at end)
#   [x if condition else y for x in items] (if/else at start)
# Explain in your own words as a comment.
# Answer:
