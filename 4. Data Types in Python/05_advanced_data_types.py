# ============================================================
# 16 — Advanced Data Types (collections + dataclasses)
# Course: Data Types in Python (DataCamp)
# Chapter 4: Advanced Data Types
# ============================================================

# ------------------------------------------------------------
# PART 1: Counter
# ------------------------------------------------------------
# Counter is a special dictionary designed for counting.
# Pass it any iterable and it counts how many times each item appears.
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(word_count)          # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(word_count["apple"]) # 3

# .most_common(N) — returns the N most frequent items as a list of tuples
print(word_count.most_common(2))  # [('apple', 3), ('banana', 2)]

# Counter works on strings too (counts characters)
letter_count = Counter("mississippi")
print(letter_count)
print(letter_count.most_common(3))


# ------------------------------------------------------------
# PART 2: defaultdict
# ------------------------------------------------------------
# defaultdict works like a regular dict, but instead of raising
# a KeyError for missing keys, it automatically creates a default value.
# You pass it a TYPE (like list or int) as the default factory.
from collections import defaultdict

# Without defaultdict — you'd need to check if the key exists first
regular = {}
for fruit in ["apple", "banana", "apple", "cherry"]:
    if fruit not in regular:
        regular[fruit] = 0
    regular[fruit] += 1

# With defaultdict(int) — int() returns 0, so missing keys start at 0
counter = defaultdict(int)
for fruit in ["apple", "banana", "apple", "cherry"]:
    counter[fruit] += 1   # no KeyError, no if-check needed
print(dict(counter))  # {'apple': 2, 'banana': 1, 'cherry': 1}

# defaultdict(list) — missing keys auto-initialize to an empty list
grouped = defaultdict(list)
data = [("fruit", "apple"), ("veggie", "carrot"), ("fruit", "banana"), ("veggie", "broccoli")]
for category, item in data:
    grouped[category].append(item)
print(dict(grouped))
# {'fruit': ['apple', 'banana'], 'veggie': ['carrot', 'broccoli']}


# ------------------------------------------------------------
# PART 3: namedtuple
# ------------------------------------------------------------
# namedtuple creates a tuple where each position has a name.
# Access fields by name (like an attribute) instead of by index.
# Good for structured records when you want lightweight, immutable objects.
from collections import namedtuple

# Define the structure: type name + field names
Eatery = namedtuple("Eatery", ["name", "location", "cuisine"])

# Create instances
r1 = Eatery(name="The Blue Plate", location="Tel Aviv", cuisine="Mediterranean")
r2 = Eatery("Spice Garden", "Jerusalem", "Indian")

# Access by attribute name (much clearer than r1[0])
print(r1.name)      # "The Blue Plate"
print(r1.cuisine)   # "Mediterranean"
print(r2.location)  # "Jerusalem"

# Still works as a regular tuple
print(r1[0])         # "The Blue Plate"
name, loc, cuisine = r1  # unpacking still works


# ------------------------------------------------------------
# PART 4: dataclass
# ------------------------------------------------------------
# @dataclass is a decorator that creates a class with less boilerplate.
# You declare fields using type annotations — Python auto-generates
# __init__, __repr__, and more.
from dataclasses import dataclass, asdict, astuple

@dataclass
class Employee:
    name: str
    department: str
    salary: float
    years: int = 0  # default value

e1 = Employee(name="Omri", department="Engineering", salary=15000, years=3)
e2 = Employee("Dana", "HR", 12000)

print(e1)          # Employee(name='Omri', department='Engineering', salary=15000, years=3)
print(e1.name)     # "Omri"
print(e2.years)    # 0  (default)

# asdict() — convert to a regular dictionary
e1_dict = asdict(e1)
print(e1_dict)

# astuple() — convert to a regular tuple
e1_tuple = astuple(e1)
print(e1_tuple)

# @property — computed attribute (acts like a field but is calculated on the fly)
@dataclass
class Product:
    name: str
    price: float
    tax_rate: float = 0.17

    @property
    def price_with_tax(self):
        return self.price * (1 + self.tax_rate)

laptop = Product(name="Laptop", price=3000)
print(f"{laptop.name} costs {laptop.price_with_tax:.2f} with tax")

# frozen=True — makes the dataclass immutable (like a tuple, can't change fields)
@dataclass(frozen=True)
class Coordinate:
    x: float
    y: float

point = Coordinate(3.0, 7.5)
print(point.x)
# point.x = 10  # This would raise FrozenInstanceError


# ------------------------------------------------------------
# EXERCISES
# ------------------------------------------------------------

# Exercise 1 — Counter
# You have a list of programming languages students are learning:
languages = ["Python", "Java", "Python", "C++", "Java", "Python", "JavaScript", "Java"]
# a) Use Counter to count occurrences of each language
# b) Print the top 2 most popular languages using .most_common(2)
# c) Print how many students are learning Python

# Your code here:


# Exercise 2 — defaultdict
# You have a list of (student, subject) pairs:
enrollments = [
    ("Alice", "Math"), ("Bob", "Science"), ("Alice", "English"),
    ("Charlie", "Math"), ("Bob", "Art"), ("Charlie", "Science")
]
# Use defaultdict(list) to group subjects by student.
# Result should be: {'Alice': ['Math', 'English'], 'Bob': ['Science', 'Art'], ...}
# Then print each student and their subjects.

# Your code here:


# Exercise 3 — namedtuple
# Define a namedtuple called "Movie" with fields: title, director, year, rating
# Create 3 movie instances of your choice.
# Loop over them and print: "Inception (2010) directed by Nolan — Rating: 8.8"
# (adjust to your actual movies)

# Your code here:


# Exercise 4 — dataclass
# Create a @dataclass called "Student" with fields:
#   name (str), grade (float), subject (str), passed (bool) with default True
# Add a @property called "letter_grade" that returns:
#   "A" if grade >= 90, "B" if >= 80, "C" if >= 70, "F" otherwise
# Create 3 students and print their name and letter_grade.

# Your code here:


# Exercise 5 — Putting it together
# You are building a simple inventory system.
# Define a namedtuple "Item" with fields: name, category, quantity
# Create a list of 5 items (mix of categories like "electronics", "food", etc.)
# Use Counter to count how many items exist per category.
# Print the most common category.

# Your code here:
