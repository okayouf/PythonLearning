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