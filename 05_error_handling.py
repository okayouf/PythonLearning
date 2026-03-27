# ============================================
# 5. Error Handling
# ============================================
# Topics: try/except, raise, TypeError, ValueError, tracebacks
#
# Common error types:
#   - TypeError: wrong data type used (e.g., "hello" + 5)
#   - ValueError: right type but wrong value (e.g., float("hello"))
#   - KeyError: key doesn't exist in dictionary
#
# Tracebacks: error reports showing what went wrong and where
#   - Read from bottom up to find the error type and message
#
# try-except:
#   - try: code that might cause an error
#   - except: code to run IF an error occurs
#   - Program keeps running after the error
#
# raise:
#   - Intentionally produces an error with a custom message
#   - Program STOPS (useful to prevent bad results)
#
# try-except vs raise:
#   - try-except: program continues after error
#   - raise: program stops at the error
# ============================================


# --- Examples ---

# try-except
def safe_average(values):
    """Calculate average, handling errors gracefully."""
    try:
        avg = sum(values) / len(values)
        return avg
    except:
        print("Error: please provide a list or set of numbers.")

print(safe_average([10, 20, 30]))  # 20.0
safe_average("hello")  # Prints error message, doesn't crash

# raise TypeError
def strict_average(values):
    """Calculate average, raising error for wrong types."""
    if type(values) != list and type(values) != set:
        raise TypeError("Please provide a list or set.")
    avg = sum(values) / len(values)
    return avg

print(strict_average([10, 20, 30]))  # 20.0
# strict_average({"a": 1})  # Would raise TypeError


# ============================================
# EXERCISES
# ============================================

# Exercise 1:
# Write a function called "safe_divide" that takes two numbers
# and returns the result of dividing the first by the second.
# Use try-except to handle division by zero.
# If dividing by zero, print "Cannot divide by zero!"
# Test with: safe_divide(10, 2) and safe_divide(10, 0)
# Your code here:


# Exercise 2:
# Write a function called "get_item" that takes a dictionary and a key.
# Use try-except to handle the case where the key doesn't exist.
# If the key is missing, print "[key] not found in dictionary."
# Test with an existing and a non-existing key.
# Your code here:


# Exercise 3:
# Write a function called "validate_age" that takes an age.
# If age is not an int, raise TypeError with "Age must be an integer"
# If age is negative, raise ValueError with "Age cannot be negative"
# Otherwise, return "Valid age: [age]"
# Test with: validate_age(25), validate_age("twenty"), validate_age(-5)
# Your code here:


# Exercise 4:
# What is the difference between try-except and raise?
# When would you use each one?
# Write your answer as a comment.
# Answer:


# Exercise 5:
# Look at this code. What error will it produce and why?
# Write your answer as a comment, then run it to check.
# 
# my_dict = {"name": "Yael", "age": 22}
# print(my_dict["grade"])
#
# Answer:
