# ============================================
# 10. Pandas Chunking
# ============================================
# Topics: pd.read_csv() with chunksize
#
# Problem: some files are too large to fit in memory
# Solution: load and process data in chunks!
#
# pd.read_csv('file.csv', chunksize=n)
#   - Returns an iterator of DataFrames
#   - Each DataFrame has n rows
#   - Process each chunk inside a for loop
#   - Aggregate results across chunks
#
# Two common patterns:
#
# Pattern 1 — collect results in a list:
#   result = []
#   for chunk in pd.read_csv('file.csv', chunksize=1000):
#       result.append(sum(chunk['column']))
#   total = sum(result)
#
# Pattern 2 — running total (more concise):
#   total = 0
#   for chunk in pd.read_csv('file.csv', chunksize=1000):
#       total += sum(chunk['column'])
# ============================================
import pandas as pd


# --- Examples ---

# Pattern 1: collect in a list
# result = []
# for chunk in pd.read_csv('students.csv', chunksize=10):
#     result.append(sum(chunk['score']))
# total = sum(result)
# print(total)

# Pattern 2: running total
# total = 0
# for chunk in pd.read_csv('students.csv', chunksize=10):
#     total += sum(chunk['score'])
# print(total)


# ============================================
# EXERCISES
# (These exercises use the students.csv file from the project)
# ============================================

# Exercise 1:
# Read students.csv with chunksize=5
# For each chunk, print the chunk and its number of rows.
# Your code here:


# Exercise 2:
# Using chunksize=10, calculate the total of all scores
# in students.csv using the running total pattern.
# Print the total.
# Your code here:


# Exercise 3:
# Using chunksize=6, count how many scores are above 80
# across all chunks. Print the total count.
# Hint: inside the loop, you can filter with chunk[chunk['score'] > 80]
# and use len() to count.
# Your code here:


# Exercise 4:
# Why would you use chunksize when reading a CSV file?
# In what situation is it useful vs. just loading the whole file?
# Write your answer as a comment.
# Answer:
