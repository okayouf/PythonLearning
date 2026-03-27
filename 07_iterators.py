# ============================================
# 7. Iterators
# ============================================
# Topics: iterables, iterators, iter(), next(),
#         splat operator *, enumerate(), zip()
#
# Iterable: an object you can loop over
#   - Examples: lists, strings, dicts, range objects, file connections
#   - Has an associated iter() method
#
# Iterator: the object that does the actual looping
#   - Created by calling iter() on an iterable
#   - Produces values one at a time with next()
#   - Throws StopIteration when exhausted
#   - Under the hood, this is what for loops do!
#
# * (splat operator): unpacks all remaining values at once
#   - Once unpacked, the iterator is exhausted
#
# enumerate(): adds a counter to an iterable
#   - Returns iterator of tuples: (index, value)
#   - Optional: start=n to change starting number
#
# zip(): stitches multiple iterables together
#   - Returns iterator of tuples pairing corresponding elements
#   - Can zip 2 or more iterables
# ============================================


# --- Examples ---

# iter() and next()
my_list = ['a', 'b', 'c']
it = iter(my_list)
print(next(it))  # a
print(next(it))  # b
print(next(it))  # c
# print(next(it))  # StopIteration!

# Splat operator
word = 'Data'
it = iter(word)
print(*it)  # D a t a
# print(*it)  # Nothing! Iterator is exhausted.

# Iterating over dictionaries
pythonistas = {'hugo': 'bowne-anderson', 'francis': 'castro'}
for key, value in pythonistas.items():
    print(key, value)

# enumerate()
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
for index, value in enumerate(avengers):
    print(index, value)

# enumerate with start
for index, value in enumerate(avengers, start=1):
    print(index, value)

# zip()
names = ['barton', 'stark', 'odinson', 'maximoff']
for hero, name in zip(avengers, names):
    print(hero, name)

# zip with splat
z = zip(avengers, names)
print(*z)


# ============================================
# EXERCISES
# ============================================

# Exercise 1:
# Create an iterator from the string "Python"
# Use next() to print the first 3 characters one by one.
# Then use * to print the rest.
# Your code here:


# Exercise 2:
# Given this list:
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# Use enumerate() with start=1 to print:
# "1. apple"
# "2. banana"
# etc.
# Your code here:


# Exercise 3:
# Given these two lists:
products = ["Laptop", "Phone", "Tablet"]
prices = [3500, 2800, 1500]
# Use zip() to print:
# "Laptop costs 3500"
# "Phone costs 2800"
# "Tablet costs 1500"
# Your code here:


# Exercise 4:
# Given these THREE lists:
students = ["Yael", "Noam", "Tamar"]
subjects = ["Math", "English", "Science"]
scores = [92, 78, 95]
# Use zip() to combine all three and print:
# "Yael got 92 in Math"
# etc.
# Your code here:


# Exercise 5:
# What happens if you try to use * on an iterator twice?
# Why does this happen?
# Write your answer as a comment, then test it.
# Answer:


# Exercise 6:
# What is the difference between an iterable and an iterator?
# In your own words, explain the relationship.
# Write your answer as a comment.
# Answer:
