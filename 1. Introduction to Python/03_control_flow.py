# ============================================
# 3. Control Flow
# ============================================
# Topics: if/elif/else, for loops, while loops,
#         comparison operators, break, +=
#
# Comparison operators:
#   ==  equal to          !=  not equal to
#   >   more than         >=  more than or equal to
#   <   less than         <=  less than or equal to
#
# if / elif / else:
#   - if: first condition check
#   - elif: additional condition (only runs if previous was False)
#   - else: runs if nothing above matched
#   - Use elif (not multiple if) when only ONE should run
#
# for loop: iterate over a known sequence
# while loop: keep going until a condition is False
# break: exit a loop early
# +=: add to a variable (total += 1 means total = total + 1)
# ============================================

# --- Examples ---

# if / elif / else
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# for loop
quantities = [1000, 800, 40, 30, 30, 15]
for qty in quantities:
    if qty >= 100:
        print(qty, "- large quantity")
    else:
        print(qty, "- small quantity")

# while loop
items_added = 0
ingredients_to_add = 5
while items_added < ingredients_to_add:
    items_added += 1
    remaining = ingredients_to_add - items_added
    print(remaining, "ingredients left")

# break
for num in range(10):
    if num == 5:
        break
    print(num)
# Prints 0, 1, 2, 3, 4 then stops


# ============================================
# EXERCISES
# ============================================

# Exercise 1:
# Write an if/elif/else that checks a variable called "age":
#   - Under 13: print "Child"
#   - 13-17: print "Teenager"
#   - 18-64: print "Adult"
#   - 65+: print "Senior"
# Test it with age = 25
# Your code here:
age = 25
if age < 13:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")

# Exercise 2:
# Given this list of temperatures:
temperatures = [22, 35, 18, 40, 28, 15, 33]
# Write a for loop that prints:
#   "Hot!" for temperatures above 30
#   "Nice" for temperatures between 20 and 30 (inclusive)
#   "Cold" for temperatures below 20
# Your code here:
for temp in temperatures:
    if temp < 20:
        print("Cold")
    elif temp <= 30:
        print("Nice")
    else:
        print("Hot!")

# Exercise 3:
# Write a while loop that starts with count = 10
# and counts down to 1, printing each number.
# When it reaches 0, print "Liftoff!"
# Your code here:
count = 10
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")

# Exercise 4:
# Given this list:
numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6]
# Write a for loop that finds the first number greater than 7
# and prints it, then stops (use break).
# Your code here:
for num in numbers:
    if num > 7:
        print(num)
        break

# Exercise 5:
# Write a for loop that goes through numbers 1 to 20.
# For each number, print:
#   "[number] is even" if it's even (hint: num % 2 == 0)
#   "[number] is odd" if it's odd
# Your code here:
for num in range(1,21):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

# Exercise 6:
# Why do we use elif instead of multiple if statements?
# What goes wrong if you use all if's?
# Write your answer as a comment.
# Answer: when we use elif, once the condition matches it skips all the rest, while multiple ifs will wil check the value for every if statement.
