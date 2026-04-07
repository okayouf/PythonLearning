# ============================================================
# 13 — Strings
# Course: Data Types in Python (DataCamp)
# Chapter 1: Fundamental Sequence Data Types
# ============================================================

# ------------------------------------------------------------
# PART 1: F-STRINGS
# ------------------------------------------------------------
# An f-string lets you embed variables directly inside a string.
# Prefix the string with f and wrap variable names in { }.

name = "Omri"
age = 25
print(f"My name is {name} and I am {age} years old.")

# You can put expressions inside the braces
price = 49.99
print(f"The total with tax is {price * 1.17:.2f}")
# :.2f means: format as a float with 2 decimal places


# ------------------------------------------------------------
# PART 2: .join()
# ------------------------------------------------------------
# .join(iterable) concatenates items in an iterable into one string.
# The string you call .join() on becomes the SEPARATOR.

words = ["Python", "is", "fun"]
sentence = " ".join(words)   # separator is a space
print(sentence)              # "Python is fun"

items = ["apple", "banana", "cherry"]
csv_line = ", ".join(items)
print(csv_line)  # "apple, banana, cherry"

# You can join with no separator:
letters = ["P", "Y", "T", "H", "O", "N"]
print("".join(letters))  # "PYTHON"


# ------------------------------------------------------------
# PART 3: SEARCHING STRINGS
# ------------------------------------------------------------
# .startswith(prefix) — returns True if the string starts with the given text
# .endswith(suffix)   — returns True if the string ends with the given text
# in operator         — returns True if a substring exists anywhere in the string

email = "omri@gmail.com"
print(email.startswith("omri"))    # True
print(email.endswith(".com"))      # True
print("gmail" in email)           # True
print("yahoo" in email)           # False

# Practical use: filtering a list
emails = ["alice@gmail.com", "bob@yahoo.com", "charlie@gmail.com"]
gmail_users = [e for e in emails if e.endswith("@gmail.com")]
print(gmail_users)


# ------------------------------------------------------------
# PART 4: CASE NORMALIZATION
# ------------------------------------------------------------
# When comparing user input, case differences cause problems.
# .lower() converts a string to all lowercase — great for comparisons.

user_input = "Yes"
if user_input.lower() == "yes":
    print("User said yes")

# Checking membership regardless of case
fruits = ["apple", "banana", "cherry"]
search = "BANANA"
print(search.lower() in fruits)  # True


# ------------------------------------------------------------
# EXERCISES
# ------------------------------------------------------------

# Exercise 1 — F-strings
# You have these variables:
product = "Laptop"
price = 3499.99
discount = 0.10
# Print this output using an f-string (no hardcoding the calculated values):
# "Laptop is on sale: original 3499.99, discounted price 3149.99"
# Hint: discounted price = price * (1 - discount)

# Your code here:


# Exercise 2 — .join()
# You have a list of city names:
cities = ["Tel Aviv", "Haifa", "Jerusalem", "Beer Sheva"]
# a) Join them with " | " as the separator and print the result
# b) Join just the first 3 cities with " → " and print the result
#    Hint: use slicing — cities[:3]

# Your code here:


# Exercise 3 — .startswith() / .endswith() / in
# You have a list of file names:
files = ["report.pdf", "data.csv", "notes.txt", "summary.pdf", "backup.csv"]
# a) Create a list of all .pdf files using a list comprehension
# b) Create a list of all files that contain the word "data"
#    (use the in operator)

# Your code here:


# Exercise 4 — Case normalization
# You have a list of responses from users:
responses = ["YES", "No", "yes", "NO", "Maybe", "YES"]
# Count how many users said "yes" (case-insensitive).
# Print: "3 users said yes" (or however many there are)

# Your code here:


# Exercise 5 — Combining it all
# You have a list of names entered by users (messy capitalization):
raw_names = ["alice", "BOB", "Charlie", "DANA", "eve"]
# a) Normalize all names to Title Case using a list comprehension
# b) Join them into one string separated by ", "
# c) Print: "Attendees: Alice, Bob, Charlie, Dana, Eve"

# Your code here:
