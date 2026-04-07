# ============================================================
# 12 — Lists and Tuples
# Course: Data Types in Python (DataCamp)
# Chapter 1: Fundamental Sequence Data Types
# ============================================================

# ------------------------------------------------------------
# PART 1: LISTS
# ------------------------------------------------------------
# A list is an ordered, mutable sequence.
# Ordered means items have a fixed position (index starts at 0).
# Mutable means you can change, add, or remove items after creation.

# Creating a list
fruits = ["apple", "banana", "cherry"]

# Indexing — access by position
print(fruits[0])   # "apple"
print(fruits[-1])  # "cherry" (negative index = count from end)

# .append() — adds ONE item to the end
fruits.append("mango")
print(fruits)  # ["apple", "banana", "cherry", "mango"]

# .extend() — adds ALL items from another list to the end
more_fruits = ["grape", "melon"]
fruits.extend(more_fruits)
print(fruits)

# + operator — combines two lists into a NEW list (does not modify originals)
list_a = [1, 2, 3]
list_b = [4, 5, 6]
combined = list_a + list_b
print(combined)  # [1, 2, 3, 4, 5, 6]

# .index() — returns the position of the first match
position = fruits.index("banana")
print(position)  # 1

# .pop() — removes and returns the last item (or item at a given index)
last = fruits.pop()
print(last)     # "melon"
print(fruits)   # "melon" is gone

# sorted() — returns a NEW sorted list (original is unchanged)
numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 5, 8, 9]
print(numbers)         # [5, 2, 8, 1, 9] — unchanged

# List comprehension — concise way to build a list
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# .title() — capitalizes each word in a string (useful when cleaning list items)
names = ["alice smith", "bob jones"]
titled = [name.title() for name in names]
print(titled)  # ["Alice Smith", "Bob Jones"]


# ------------------------------------------------------------
# PART 2: TUPLES
# ------------------------------------------------------------
# A tuple is an ordered, IMMUTABLE sequence.
# Once created, you cannot change, add, or remove items.
# Use tuples when the data should not change (e.g., coordinates, records).

# Creating a tuple
point = (3, 7)
print(point[0])  # 3

# Tuples are commonly created by zip() and enumerate()
names = ["Alice", "Bob", "Charlie"]
scores = [88, 92, 75]

zipped = list(zip(names, scores))
print(zipped)  # [("Alice", 88), ("Bob", 92), ("Charlie", 75)]

for name, score in zipped:
    print(f"{name}: {score}")

# Tuple unpacking — assign each position to a variable
first, second = (10, 20)
print(first)   # 10
print(second)  # 20

# TRAILING COMMA WARNING:
# "butter" is a string — just parentheses around a value
not_a_tuple = ("butter")
print(type(not_a_tuple))  # <class 'str'>

# "butter," IS a tuple — the comma makes it one
yes_a_tuple = ("butter",)
print(type(yes_a_tuple))  # <class 'tuple'>


# ------------------------------------------------------------
# EXERCISES
# ------------------------------------------------------------

# Exercise 1 — Lists
# You have this list of students:
students = ["omri", "dana", "yosi", "maya"]
# a) Add "lior" to the end of the list using .append()
# b) Print the student at index 2
# c) Remove and print the last student using .pop()
# d) Print a sorted version of the list (do not modify the original)

# Your code here:


# Exercise 2 — List comprehension
# Create a list called "even_squares" containing the square of every even number
# from 2 to 10 (inclusive: 2, 4, 6, 8, 10).
# Expected result: [4, 16, 36, 64, 100]

# Your code here:


# Exercise 3 — Tuples and zip()
# You have two lists:
cities = ["Tel Aviv", "Jerusalem", "Haifa"]
populations = [460000, 936000, 285000]
# a) Use zip() to pair each city with its population
# b) Loop over the pairs and print: "Tel Aviv has a population of 460000"
#    (use an f-string)

# Your code here:


# Exercise 4 — Tuple unpacking
# Given this tuple representing a product:
product = ("Laptop", 3499.99, "Electronics")
# Unpack it into three variables: name, price, category
# Then print: "Laptop costs 3499.99 and belongs to Electronics"

# Your code here:


# Exercise 5 — Trailing comma trap
# Look at these two lines. Without running them, predict the type of each variable.
# Then run the code to verify.
mystery_a = ("hello")
mystery_b = ("hello",)
# What type is mystery_a? ___________
# What type is mystery_b? ___________
print(type(mystery_a))
print(type(mystery_b))
