# ============================================
# 9. Generators
# ============================================
# Topics: generator expressions, generator functions, yield
#
# Generator expression:
#   - Same as list comprehension but with () instead of []
#   - Does NOT build the full list in memory
#   - Produces values on the fly (lazy evaluation)
#   - Great for huge datasets
#
# Generator function:
#   - A function that uses yield instead of return
#   - When called, returns a generator object
#   - Each call to next() runs until the next yield, then pauses
#   - Remembers its state between calls
#
# Getting values from generators:
#   - next() — one value at a time
#   - for loop — all values
#   - list() — convert to a list (defeats the memory purpose!)
#   - * (splat) — unpack all values
#
# Key difference from list comprehension:
#   [x for x in range(1000000)] — creates full list, uses lots of memory
#   (x for x in range(1000000)) — creates generator, barely uses memory
# ============================================
from dataclasses import dataclass
from datetime import date

# --- Examples ---

# Generator expression
gen = (2 * num for num in range(10))
print(type(gen))  # <class 'generator'>

# Using next()
result = (num for num in range(6))
print(next(result))  # 0
print(next(result))  # 1
print(next(result))  # 2

# Using a for loop
gen2 = (num ** 2 for num in range(5))
for val in gen2:
    print(val)

# Conditional in generator expression
even_squares = (num ** 2 for num in range(10) if num % 2 == 0)
print(list(even_squares))  # [0, 4, 16, 36, 64]

# Generator function
def num_sequence(n):
    """Generate values from 0 to n."""
    i = 0
    while i < n:
        yield i
        i += 1

result = num_sequence(5)
print(next(result))  # 0
print(next(result))  # 1

for val in num_sequence(3):
    print(val)  # 0, 1, 2


# ============================================
# EXERCISES
# ============================================

# Exercise 1:
# Create a generator expression that produces the cubes (x**3)
# of numbers from 1 to 10.
# Use next() to print the first 3 values.
# Your code here:
cubed = (num ** 3 for num in range(1, 11))
print(next(cubed))
print(next(cubed))
print(next(cubed))

# Exercise 2:
# Create a generator expression that produces "Pass" or "Fail"
# for each score in this list (>= 60 is Pass):
scores = [85, 42, 73, 58, 91, 66, 39]
# Use a for loop to print all the results.
# Your code here:
test_result = ( "pass" if score >= 60 else "fail" for score in scores )
for score in test_result:
    print(score)

# Exercise 3:
# Write a generator function called "countdown" that takes a number n
# and yields values from n down to 1.
# Test it: list(countdown(5)) should give [5, 4, 3, 2, 1]
# Your code here:
def countdown(n):
    while n > 0:
        yield n
        n -= 1
print(list(countdown(5)))

# Exercise 4:
# Write a generator function called "even_numbers" that takes a max number
# and yields only even numbers from 0 up to (but not including) that max.
# Test it: list(even_numbers(10)) should give [0, 2, 4, 6, 8]
# Your code here:
def even_numbers(n):
    for num in range(n):
        if num % 2 == 0:
            yield num

print(list(even_numbers(10)))

# Exercise 5:
# What is the difference between a list comprehension and a generator expression?
# When would you use one over the other?
# Write your answer as a comment.
# Answer: List comprehension → builds the full list in memory immediately
# Generator expression → produces values one at a time, on demand
# Use a list comprehension when you need to reuse the data or its size is small.
# Use a generator when the dataset is large or you only need to go through it once.


# ============================================
# BONUS — Generators for streaming data (Chapter 3)
# ============================================
#
# with open() — context manager for file reading
# -------------------------------------------------
# When you open a file with:
#     with open("filename.csv") as file:
#         ...
# Python automatically closes the file when the block ends — even if an error occurs.
# This is safer than calling file.open() / file.close() manually.
#
# A file object is itself an iterable — you can loop over it line by line.
# This makes it a perfect match for generators: you never load the whole file.
#
# Pattern:
#     def read_large_file(file_object):
#         while True:
#             line = file_object.readline()
#             if not line:       # empty string = end of file
#                 break
#             yield line
#
# Then use it:
#     with open("big_file.csv") as f:
#         gen = read_large_file(f)
#         print(next(gen))   # first line only — rest not yet read
# ============================================

# Exercise 6 — Generators + with open()
# Write a generator function called read_large_file(file_object) that:
# - Reads one line at a time using file_object.readline()
# - Yields each line
# - Stops when readline() returns an empty string (end of file)
#
# Then open students.csv (path: "../Projects/students.csv") using with open(),
# call your generator, and use next() to print just the first 3 lines.
#
# Why not just read the whole file at once?
# Write your answer as a comment too.

# Answer: Loading the whole file at once stores it all in memory.
# If the file is larger than available RAM, Python will slow down significantly or raise a MemoryError.
# A generator reads one line at a time, so memory usage stays constant no matter how big the file is
# Your code here:
def read_large_file(file_object):
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data
with open(r'C:\Users\Omri\PycharmProjects\PythonLearning\Projects\students.csv') as file:
    get_file = read_large_file(file)
    print(next(get_file))
    print(next(get_file))
    print(next(get_file))