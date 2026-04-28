# ============================================================
# 14 — Dictionaries
# Course: Data Types in Python (DataCamp)
# Chapter 2: Dictionaries — The Root of Python
# ============================================================

# ------------------------------------------------------------
# PART 1: CREATING DICTIONARIES
# ------------------------------------------------------------
# A dictionary stores key-value pairs.
# Keys must be unique. Values can be anything.
# Two ways to create one:

# Using curly braces
student = {"name": "Omri", "age": 25, "grade": "A"}

# Using dict()
student2 = dict(name="Dana", age=22, grade="B")

# Accessing a value by key
print(student["name"])   # "Omri"


# ------------------------------------------------------------
# PART 2: SAFE ACCESS WITH .get()
# ------------------------------------------------------------
# Direct access raises a KeyError if the key doesn't exist.
# .get(key, default) returns the default instead — no crash.

print(student.get("email", "No email on file"))  # "No email on file"
print(student.get("name", "Unknown"))            # "Omri"


# ------------------------------------------------------------
# PART 3: ADDING AND UPDATING
# ------------------------------------------------------------
# Direct assignment adds a new key or overwrites an existing one
student["email"] = "omri@example.com"   # new key
student["grade"] = "A+"                 # update existing key

# .update() — adds/updates multiple keys at once
student.update({"city": "Tel Aviv", "age": 26})
print(student)


# ------------------------------------------------------------
# PART 4: REMOVING KEYS
# ------------------------------------------------------------
# del — removes the key, returns nothing
del student["email"]

# .pop(key) — removes the key AND returns its value
removed_grade = student.pop("grade")
print(f"Removed grade: {removed_grade}")
print(student)


# ------------------------------------------------------------
# PART 5: PYTHONIC ITERATION WITH .items()
# ------------------------------------------------------------
# .items() gives you (key, value) pairs — unpack them directly in the loop

inventory = {"apple": 50, "banana": 30, "cherry": 80}
for fruit, quantity in inventory.items():
    print(f"{fruit}: {quantity} units")

# .keys() — iterate over keys only
for key in inventory.keys():
    print(key)


# ------------------------------------------------------------
# PART 6: CHECKING IF A KEY EXISTS
# ------------------------------------------------------------
# Use the in operator — fast and Pythonic
if "banana" in inventory:
    print("We have bananas!")

# Avoid using .get() just to check existence — in is cleaner


# ------------------------------------------------------------
# PART 7: NESTED DICTIONARIES
# ------------------------------------------------------------
# A dictionary whose values are also dictionaries

school = {
    "class_a": {"teacher": "Mr. Cohen", "students": 30},
    "class_b": {"teacher": "Ms. Levi",  "students": 25},
}

# Chained indexing to reach nested values
print(school["class_a"]["teacher"])   # "Mr. Cohen"
print(school["class_b"]["students"])  # 25

# Get all top-level keys
print(list(school.keys()))  # ["class_a", "class_b"]


# ------------------------------------------------------------
# EXERCISES
# ------------------------------------------------------------

# Exercise 1 — Creating and accessing
# Create a dictionary called "book" with these keys:
# title = "The Hitchhiker's Guide to the Galaxy"
# author = "Douglas Adams"
# year = 1979
# pages = 224
# Then print the author using direct access.

# Your code here:
book = {
    'title':"The Hitchhiker's Guide to the Galaxy",
    'author':"Douglas Adams",
    'year':1979,
    'pages':224
}
print(book['author'])

# Exercise 2 — Safe access
# Using the "book" dictionary you just created:
# a) Try to get the value for key "rating" — use .get() with a default of "Not rated"
# b) Try to get the value for key "title" — use .get() with a default of "Unknown"
# Print both results.
print(book.get('rating','Not rated'))
print(book.get('title', 'unknown'))

# Your code here:


# Exercise 3 — Adding, updating, removing
# Start with this dictionary:
employee = {"name": "Yosi", "department": "Engineering", "salary": 12000}
# a) Add a key "years_at_company" with value 3
# b) Update the salary to 13500
# c) Remove the "department" key using .pop() and print what was returned
# d) Print the final dictionary

# Your code here:
employee["years_at_company"] = 3
employee['salary'] = 13500
print(employee.pop('department'))
print(employee)

# Exercise 4 — Iteration with .items()
# You have a grade book:
grades = {"Alice": 91, "Bob": 78, "Charlie": 85, "Dana": 94}
# Loop over it and print each student's result in this format:
# "Alice passed with 91" if grade >= 80
# "Bob needs improvement with 78" if grade < 80

# Your code here:
for name,grade in grades.items():
    if grade >= 80:
        print(f'{name} passed with {grade}')
    else:
        print(f'{name} needs improvement with {grade}')

# Exercise 5 — Nested dictionary
# You manage two stores:
stores = {
    "north": {"city": "Haifa", "employees": 12, "open": True},
    "south": {"city": "Beer Sheva", "employees": 8, "open": False},
}
# a) Print the city of the "south" store
# b) Print how many employees the "north" store has
# c) Loop over stores.items() and print:
#    "north store in Haifa is open" or "south store in Beer Sheva is closed"
#    based on the "open" value

# Your code here:
print(stores['south']['city'])
print(stores["north"]['employees'])

for district, store in stores.items():
    if store['open'] :
        print(f'{district} store in {store["city"]} is open')
    else:
        print(f'{district} store in {store["city"]} is closed')
