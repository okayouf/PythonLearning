# ============================================================
#  Practice Exercises — based on your recent learning
#  Topics: comprehensions, generators, functions, pandas
# ============================================================
#
#  Instructions: solve each exercise below the comment block.
#  Each exercise builds on what you already built in
#  "Student Grade Tracker & Analyzer.py" and "learning.py".
# ============================================================


# ------------------------------------------------------------------
# EXERCISE 1 — Comprehensions
# ------------------------------------------------------------------
# You have a list of (name, score) tuples.
# Using ONE list comprehension, create a list of strings like:
#   "Yael Cohen: A"  (use your get_grade logic inside the comprehension)
#
# Expected output (order may vary):
#   ['Yael Cohen: A', 'Noam Levy: D', 'Tamar Shapira: A',
#    'Ori Mizrahi: F', 'Dana Peretz: B', 'Eitan Katz: C']

students_data = [
    ("Yael Cohen", 92), ("Noam Levy", 65), ("Tamar Shapira", 95),
    ("Ori Mizrahi", 45), ("Dana Peretz", 83), ("Eitan Katz", 71),
]

def get_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"

# Your code here:
grade_strings = ...

print("Exercise 1:", grade_strings)


# ------------------------------------------------------------------
# EXERCISE 2 — Dictionary comprehension + filtering
# ------------------------------------------------------------------
# From students_data above, build a dictionary of ONLY the students
# who are FAILING (score < 60).
# Format: { name: score }
#
# Expected: {'Ori Mizrahi': 45}

# Your code here:
failing_students = ...

print("Exercise 2:", failing_students)


# ------------------------------------------------------------------
# EXERCISE 3 — Generator function
# ------------------------------------------------------------------
# Write a generator function called `score_above(data, threshold)`
# that takes a list of (name, score) tuples and a threshold number,
# and yields each (name, score) pair where score > threshold.
#
# Then use it to print all students scoring above 80.

# Your code here:
def score_above(data, threshold):
    ...

for item in score_above(students_data, 80):
    print("Exercise 3:", item)


# ------------------------------------------------------------------
# EXERCISE 4 — enumerate() + zip()
# ------------------------------------------------------------------
# You have two separate lists: names and scores (already defined below).
# Using zip() and enumerate(), print each student with their rank (1-based),
# name, score, AND grade letter.
#
# Expected output:
#   1. Yael Cohen — 92 — A
#   2. Noam Levy  — 65 — D
#   ... etc.

names  = ["Yael Cohen", "Noam Levy", "Tamar Shapira", "Ori Mizrahi", "Dana Peretz", "Eitan Katz"]
scores = [92, 65, 95, 45, 83, 71]

# Your code here:


# ------------------------------------------------------------------
# EXERCISE 5 — Lambda + sorted()
# ------------------------------------------------------------------
# Sort students_data by score from highest to lowest using a lambda.
# Print each sorted entry.
#
# Hint: use the `sorted()` built-in with a `key=` argument.

# Your code here:
sorted_students = ...

print("Exercise 5 - sorted by score:")
for student in sorted_students:
    print(" ", student)


# ------------------------------------------------------------------
# EXERCISE 6 — Functions with error handling
# ------------------------------------------------------------------
# Write a function `average_score(score_list)` that:
#   - Takes a list of numbers
#   - Returns the average rounded to 1 decimal place
#   - Raises a ValueError with the message "List is empty" if the list is empty
#   - Raises a TypeError with the message "All values must be numbers"
#     if any value in the list is not an int or float
#
# Test it with these three calls:
#   average_score([90, 80, 70])       -> should return 80.0
#   average_score([])                 -> should raise ValueError
#   average_score([90, "eighty", 70]) -> should raise TypeError

# Your code here:
def average_score(score_list):
    ...

# Uncomment to test:
# print("Exercise 6:", average_score([90, 80, 70]))
# print("Exercise 6:", average_score([]))
# print("Exercise 6:", average_score([90, "eighty", 70]))


# ------------------------------------------------------------------
# EXERCISE 7 — Pandas: subject averages
# ------------------------------------------------------------------
# Load students.csv with pandas.
# For each SUBJECT (Math, English, Science), calculate the average score
# across ALL students and semesters, and print the results.
#
# Expected output (approximate):
#   Math    : 73.2
#   English : 68.4
#   Science : 75.1
#
# Hint: use groupby('subject')['score'].mean()

import pandas as pd

# Your code here:


# ------------------------------------------------------------------
# EXERCISE 8 — Pandas: best student per subject
# ------------------------------------------------------------------
# Using students.csv, find the student with the HIGHEST average score
# for each subject. Print:
#   Math    -> Tamar Shapira (95.0)
#   ...
#
# Hint: you'll need groupby(['subject','name']).mean() then
#       use .idxmax() or sort + head.

# Your code here:


# ------------------------------------------------------------------
# EXERCISE 9 — Putting it all together (mini-project)
# ------------------------------------------------------------------
# Write a function `full_report(filename)` that reads the CSV and prints
# a report in this format for every student:
#
#   === Yael Cohen ===
#   Average score : 87.3
#   Grade         : B
#   Subjects      : Math, English, Science
#   Status        : Pass
#
# Requirements:
#   - Use your get_grade() and average_score() functions
#   - List the subjects the student appears in (sorted alphabetically)
#   - Status is "Pass" if average >= 60, otherwise "Fail"
#   - Handle file-not-found with a clear error message

# Your code here:
def full_report(filename):
    ...

# Uncomment to test:
# full_report('students.csv')
