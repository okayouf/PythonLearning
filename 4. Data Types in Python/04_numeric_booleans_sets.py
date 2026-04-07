# ============================================================
# 15 — Numeric Types, Booleans, and Sets
# Course: Data Types in Python (DataCamp)
# Chapter 3: Numeric Data Types, Booleans, and Sets
# ============================================================

# ------------------------------------------------------------
# PART 1: int vs float
# ------------------------------------------------------------
# int  — exact whole numbers, no decimals
# float — approximate fractional numbers (stored in binary)

x = 10       # int
y = 3.14     # float
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>

# Division always returns a float
print(10 / 2)   # 5.0 (not 5!)

# Floor division — returns int (rounds DOWN)
print(10 // 3)  # 3
print(-7 // 2)  # -4  (floors toward negative infinity)


# ------------------------------------------------------------
# PART 2: Decimal — for exact precision
# ------------------------------------------------------------
# Use Decimal when exact arithmetic matters (e.g., money)
from decimal import Decimal

price = Decimal("19.99")
tax = Decimal("0.17")
total = price + price * tax
print(total)  # Exact result, no floating-point error

# float version — less reliable
price_f = 19.99
total_f = price_f + price_f * 0.17
print(total_f)  # Might be something like 23.388299999...


# ------------------------------------------------------------
# PART 3: Float formatting
# ------------------------------------------------------------
value = 1234.5678

# Fixed notation — all decimal places shown
print(f"{value:f}")      # 1234.567800

# Specific decimal places
print(f"{value:.2f}")    # 1234.57  (rounds)
print(f"{value:.0f}")    # 1235

# Scientific notation
big = 0.000012345
print(f"{big:.2e}")      # 1.23e-05


# ------------------------------------------------------------
# PART 4: THE FLOAT PRECISION TRAP
# ------------------------------------------------------------
# Floats are stored in binary — some decimals can't be represented exactly.
result = 0.1 + 1.1
print(result)          # 1.2000000000000002  (NOT 1.2!)
print(result == 1.2)   # False

# Fix: use Decimal for precise comparisons
from decimal import Decimal
d_result = Decimal("0.1") + Decimal("1.1")
print(d_result == Decimal("1.2"))  # True


# ------------------------------------------------------------
# PART 5: BOOLEANS
# ------------------------------------------------------------
# Booleans represent truth values. Only two possible values:
# True  and  False  (capital T and F — these are NOT strings)

is_open = True
is_empty = False

print(type(is_open))   # <class 'bool'>

# Comparison operators — all return a Boolean
print(5 > 3)    # True
print(5 == 5)   # True
print(5 != 4)   # True
print(5 <= 5)   # True
print(5 < 5)    # False

# Truthy values — treated as True in a boolean context
print(bool(1))       # True
print(bool("hello")) # True
print(bool([1, 2]))  # True

# Falsey values — treated as False in a boolean context
print(bool(0))    # False
print(bool(""))   # False
print(bool([]))   # False
print(bool({}))   # False
print(bool(None)) # False


# ------------------------------------------------------------
# PART 6: SETS
# ------------------------------------------------------------
# A set is an unordered collection of UNIQUE items.
# Use it when you need to eliminate duplicates or do set math.

# Creating a set from a list (removes duplicates automatically)
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)
print(unique)  # {1, 2, 3, 4} — order may vary

# .add() — add a single item
unique.add(5)

# .update() — add multiple items
unique.update([6, 7])

# .discard() — remove an item (no error if it doesn't exist)
unique.discard(7)

# .pop() — remove and return an arbitrary item
removed = unique.pop()
print(f"Removed: {removed}")

# SET OPERATIONS
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))         # {1, 2, 3, 4, 5, 6}  — all items from both
print(a.intersection(b))  # {3, 4}               — items in BOTH
print(a.difference(b))    # {1, 2}               — in a but NOT in b
print(b.difference(a))    # {5, 6}               — in b but NOT in a (order matters!)


# ------------------------------------------------------------
# EXERCISES
# ------------------------------------------------------------

# Exercise 1 — int vs float and division
# a) What is the result of 15 / 4? Print it and print its type.
# b) What is the result of 15 // 4? Print it and print its type.
# c) What is the result of -9 // 2? Predict first, then verify.

# Your code here:


# Exercise 2 — Decimal precision
# A product costs 89.95 (use Decimal).
# Tax rate is 17% (use Decimal("0.17")).
# Calculate the final price and print it with 2 decimal places using an f-string.

# Your code here:


# Exercise 3 — Float trap
# a) Run: result = 0.1 + 0.2 — print the result
# b) Check: does result == 0.3? Print the comparison.
# c) Fix it using Decimal and confirm the comparison is now True.

# Your code here:


# Exercise 4 — Booleans and truthy/falsey
# For each of the following, predict True or False BEFORE running,
# then verify with bool():
# 1. bool(42)
# 2. bool(0)
# 3. bool("False")   <-- careful, think about what type this is
# 4. bool([])
# 5. bool({"key": "value"})

# Write your predictions as comments, then verify:
# 1. prediction: ___
# 2. prediction: ___
# 3. prediction: ___
# 4. prediction: ___
# 5. prediction: ___

# Your code here:


# Exercise 5 — Sets
# You collected survey responses (with duplicates):
responses = ["yes", "no", "yes", "maybe", "yes", "no", "no", "maybe"]
# a) Create a set of unique responses and print it
# b) Add "undecided" to the set
# c) Print the number of unique responses (use len())

# Your code here:


# Exercise 6 — Set operations
# Two classes picked their favorite subjects:
class_a = {"Math", "Physics", "History", "English"}
class_b = {"Physics", "Chemistry", "English", "Biology"}
# a) What subjects does BOTH classes like? (intersection)
# b) What subjects are liked by at least one class? (union)
# c) What subjects does class_a like that class_b does NOT? (difference)
# d) What subjects does class_b like that class_a does NOT?

# Your code here:
