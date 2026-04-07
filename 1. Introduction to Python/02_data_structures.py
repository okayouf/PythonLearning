# ============================================
# 2. Data Structures
# ============================================
# Topics: lists, dictionaries, tuples, sets
#
# Lists: ordered, changeable, allows duplicates
#   - Created with square brackets []
#   - Access by index: my_list[0]
#   - Methods: .append(), .remove()
#
# Dictionaries: key-value pairs, changeable
#   - Created with curly braces {} and colons
#   - Access by key: my_dict["key"]
#   - Methods: .items(), .keys(), .values()
#
# Tuples: ordered, IMMUTABLE (cannot be changed)
#   - Created with parentheses ()
#   - Access by index: my_tuple[0]
#   - Good for data that shouldn't change
#
# Sets: unordered, unique values only
#   - Created with curly braces {}
#   - Great for removing duplicates
#   - Fast for checking membership
# ============================================


# --- Examples ---

# List
ingredients = ["pasta", "tomatoes", "garlic", "basil", "olive oil", "salt"]
print(ingredients[0])  # pasta
ingredients.append("pepper")
print(ingredients)

# Dictionary
recipe_dict = {"pasta": 500, "tomatoes": 400, "garlic": 15}
print(recipe_dict["pasta"])  # 500

# Tuple
serving_sizes = (1, 2, 4, 6, 8)
print(serving_sizes[1])  # 2
# serving_sizes[0] = 10  # This would cause an error! Tuples are immutable.

# Set
ingredients_set = {"pasta", "tomatoes", "pasta", "basil", "garlic"}
print(ingredients_set)  # "pasta" appears only once!


# ============================================
# EXERCISES
# ============================================

# Exercise 1:
# Create a list of 5 cities you'd like to visit.
# Print the third city using indexing.
# Add a 6th city using .append()
# Print the full list.
# Your code here:
cities = ["Haifa","Tel Aviv","Beer sheva","Jerusalem","Rishon LeZion"]
print(cities[2])
cities.append("Nahariyya")
print(cities)

# Exercise 2:
# Create a dictionary called "student" with keys:
# "name", "age", "grade" and assign appropriate values.
# Print the student's name by accessing the key.
# Your code here:
student = {"name": "Omri", "age": 25, "grade": 90}
print(student["name"])

# Exercise 3:
# Create a tuple with the days of the week.
# Try to change "Monday" to "Funday" — what happens?
# Write the error as a comment.
# Your code here:
week_days = ("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
# week_days[1] = "funday"
print(week_days)

# Exercise 4:
# Given this list with duplicates:
colors = ["red", "blue", "green", "red", "blue", "yellow", "red"]
# Convert it to a set to remove duplicates, then back to a list.
# Print the result.
# Your code here:
set_colors = set(colors)
print(set_colors)

# Exercise 5:
# Create a dictionary where:
#   - Keys are 3 friends' names
#   - Values are their favorite foods
# Loop through it using .items() and print:
# "[name] loves [food]"
# Your code here:
names_foods = {"omri": "burger", "danny" : "steak", "john" : "pizza"}
for name, food in names_foods.items():
    print(name,"loves", food)

# Exercise 6:
# What is the difference between a tuple and a list?
# When would you use a tuple instead of a list?
# Write your answer as a comment.
# Answer: a list can be changed and tuples can't be changed. i would use a tuple when the data needs to stay fixed.
