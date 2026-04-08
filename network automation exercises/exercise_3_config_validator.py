# ============================================
# Exercise 3: Config Validator
# ============================================
# Write a function called "validate_config" that takes **kwargs representing
# a device config and:
#   1. Checks that all required fields are present: "name", "type", "ip", "status"
#      If any are missing, raise a ValueError listing which fields are missing.
#      Hint: use a list comprehension to find missing fields
#   2. Checks that "status" is either "online" or "offline"
#      If not, raise a ValueError with a clear message.
#   3. Checks that "ip" contains exactly 3 dots (basic format check)
#      If not, raise a ValueError with a clear message.
#   4. If all checks pass, prints:
#       "Config valid: [name] ([type]) at [ip] is [status]"
#      and returns the kwargs dict.
#   Use try-except when calling the function to catch and print errors cleanly.
#
# Test with all three calls below — each one should behave differently.
# ============================================

# Your code here:


try:
    validate_config(name="switch-D", type="switch", ip="10.0.0.5", status="online")
except ValueError as e:
    print("Error:", e)

try:
    validate_config(name="router-X", ip="10.0.0.6", status="online")
except ValueError as e:
    print("Error:", e)

try:
    validate_config(name="ap-1", type="access_point", ip="bad_ip", status="active")
except ValueError as e:
    print("Error:", e)
