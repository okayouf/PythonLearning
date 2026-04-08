# ============================================
# Exercise 2: Log Parser with Generator
# ============================================
# Part A — Write a generator function called "error_logs" that takes a list
# of log strings and yields only logs that contain the word "ERROR".
#
# Part B — Write a function called "error_summary" that:
#   1. Uses the "error_logs" generator to loop through errors
#   2. Counts how many errors each device has: {device_name: error_count}
#      Hint: the device name is always the first word — use .split()
#   3. Finds the device with the most errors
#      Hint: loop through the dict and track the max, or use max() with a key argument
#   4. Prints:
#       "=== Error Summary ==="
#       "Errors per device: [dict]"
#       "Most errors: [device_name] ([count] errors)"
#   Include a docstring and try-except.
# ============================================

logs = [
    "switch-A INFO port 1 up",
    "switch-A ERROR port 3 down",
    "router-main INFO BGP session established",
    "firewall-1 ERROR intrusion attempt detected",
    "switch-B INFO port 5 up",
    "switch-A ERROR port 7 down",
    "ap-lobby ERROR connection lost",
    "router-main ERROR BGP session dropped",
    "switch-C INFO rebooting",
    "firewall-1 ERROR packet drop threshold exceeded",
]

# Your code here:


error_summary(logs)
