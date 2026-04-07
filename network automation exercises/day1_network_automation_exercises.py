# ============================================
# Network Automation Exercises
# ============================================
# Practice your Python skills with networking-themed data!
# All exercises use ONLY concepts you've already learned:
#   variables, data types, lists, dicts, tuples, sets,
#   for/while loops, if/elif/else, functions, *args, **kwargs,
#   docstrings, try/except, raise, lambda, map(),
#   enumerate(), zip(), list/dict comprehensions, generators,
#   pandas chunking
# ============================================


# === SAMPLE DATA ===
# Use this data throughout the exercises

ip_addresses = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "192.168.1.1", "172.16.0.5"]

ping_results = [True, False, True, True, False]

devices = [
    {"name": "switch-A", "type": "switch", "ip": "10.0.0.1", "status": "online"},
    {"name": "ap-lobby", "type": "access_point", "ip": "10.0.0.2", "status": "offline"},
    {"name": "switch-B", "type": "switch", "ip": "10.0.0.3", "status": "online"},
    {"name": "router-main", "type": "router", "ip": "192.168.1.1", "status": "online"},
    {"name": "ap-floor2", "type": "access_point", "ip": "172.16.0.5", "status": "offline"},
    {"name": "switch-C", "type": "switch", "ip": "10.0.0.4", "status": "online"},
    {"name": "firewall-1", "type": "firewall", "ip": "10.0.0.254", "status": "online"},
]


# ============================================
# PART 1: Variables & Data Types
# ============================================

# Exercise 1.1:
# Create variables for a network device:
#   device_name (str), ip_address (str), port_count (int),
#   uptime_hours (float), is_online (bool)
# Print each variable's type.
# Your code here:
device_name = 'switch'
ip_address = '192.168.0.1'
port_count = 48
uptime_hours = 3.38
is_online = False

# ============================================
# PART 2: Data Structures
# ============================================

# Exercise 2.1:
# Create a dictionary called "device_info" for a router with keys:
#   "name", "type", "ip", "status"
# Print the device's IP by accessing the key.
# Your code here:
device_info = {'name':'router_a','type':'1','ip':'10.0.0.138','status':True}
print(device_info['ip'])

# Exercise 2.2:
# From the "devices" list above, create a SET of all unique device types.
# (Hint: loop through devices and collect each device's "type")
# Print the set.
# Your code here:
unique_devices = set()
for device in devices:
    unique_devices.add(device['type'])
print(unique_devices)

# Exercise 2.3:
# Create a TUPLE called "allowed_types" with:
#   "switch", "router", "access_point", "firewall"
# Why is a tuple a good choice here instead of a list?
# Write your answer as a comment.
# Your code here:


# ============================================
# PART 3: Control Flow
# ============================================

# Exercise 3.1:
# Loop through the "devices" list and print:
#   "[name] is UP" if status is "online"
#   "[name] is DOWN" if status is "offline"
# Your code here:


# Exercise 3.2:
# Loop through the "devices" list and count how many devices
# are online vs offline. Print the counts at the end.
# (Hint: use two counter variables and +=)
# Your code here:


# Exercise 3.3:
# Loop through the "devices" list. If you find a device with
# type "firewall", print its name and IP, then stop the loop with break.
# Your code here:


# ============================================
# PART 4: Functions
# ============================================

# Exercise 4.1:
# Write a function called "device_status" that takes an IP and a status
# (with a default value of "unknown") and returns:
#   "[ip] - Status: [status]"
# Include a docstring.
# Test with: device_status("10.0.0.1", "online") and device_status("10.0.0.5")
# Your code here:


# Exercise 4.2:
# Write a function called "count_by_type" that takes *args
# (any number of device dictionaries) and returns a dictionary
# counting how many devices of each type there are.
# Example: {"switch": 3, "access_point": 2, "router": 1, "firewall": 1}
# (Hint: loop through args, check each device's "type", build a count dict)
# Your code here:


# Exercise 4.3:
# Write a function called "create_device" that takes **kwargs
# and prints each key-value pair as a device configuration line:
#   "name: switch-D"
#   "type: switch"
#   "ip: 10.0.0.10"
# Your code here:


# ============================================
# PART 5: Error Handling
# ============================================

# Exercise 5.1:
# Write a function called "get_device_ip" that takes the devices list
# and a device name. Loop through the list to find the device and return
# its IP. Use try-except so that if anything goes wrong, it prints
# "Error looking up device."
# If the device isn't found, print "[name] not found in network."
# Your code here:


# Exercise 5.2:
# Write a function called "validate_ip" that takes a string.
# If it's not a string, raise TypeError with "IP must be a string"
# If the string is empty, raise ValueError with "IP cannot be empty"
# Otherwise return "Valid IP: [ip]"
# Your code here:


# ============================================
# PART 6: Lambda
# ============================================

# Exercise 6.1:
# Write a lambda called "is_online" that takes a device dict
# and returns True if status is "online", else False.
# Test it with: is_online({"name": "switch-A", "status": "online"})
# Your code here:


# Exercise 6.2:
# Use map() with a lambda to extract just the IP addresses
# from the "devices" list (each device is a dict with an "ip" key).
# Print the result as a list.
# Your code here:


# ============================================
# PART 7: Iterators (enumerate, zip)
# ============================================

# Exercise 7.1:
# Use enumerate() with start=1 to print a numbered list of devices:
#   "1. switch-A (10.0.0.1)"
#   "2. ap-lobby (10.0.0.2)"
#   etc.
# Your code here:


# Exercise 7.2:
# Use zip() with ip_addresses and ping_results to print:
#   "10.0.0.1 - Reachable"   (if True)
#   "10.0.0.2 - Unreachable" (if False)
# Your code here:


# ============================================
# PART 8: List & Dict Comprehensions
# ============================================

# Exercise 8.1:
# Use a list comprehension to get the names of all ONLINE devices
# from the "devices" list.
# Your code here:


# Exercise 8.2:
# Use a list comprehension with if/else to create a list that labels
# each device as "ONLINE" or "OFFLINE" based on its status.
# Your code here:


# Exercise 8.3:
# Use a dict comprehension with the "devices" list to create a dictionary
# where the key is the device name and the value is the IP address.
# Your code here:


# Exercise 8.4:
# Use zip() inside a dict comprehension with ip_addresses and ping_results
# to create: {"10.0.0.1": "Reachable", "10.0.0.2": "Unreachable", ...}
# Your code here:


# ============================================
# PART 9: Generators
# ============================================

# Exercise 9.1:
# Create a generator expression that yields the name of each device
# that is offline. Use next() to get the first offline device.
# Your code here:


# Exercise 9.2:
# Write a generator function called "network_scan" that takes a list
# of device dicts and yields a string for each:
#   "[name] at [ip] is [status]"
# Test it with a for loop.
# Your code here:


# ============================================
# PART 10: Putting It All Together
# ============================================

# Exercise 10.1:
# Write a function called "network_report" that takes a list of device dicts
# and does the following:
#   1. Uses a list comprehension to find all online device names
#   2. Uses a list comprehension to find all offline device names
#   3. Uses a dict comprehension to create {name: type} for all devices
#   4. Counts devices by type (how many switches, routers, etc.)
#   5. Prints a full report:
#       "=== Network Report ==="
#       "Total devices: [count]"
#       "Online: [count] - [list of names]"
#       "Offline: [count] - [list of names]"
#       "Device types: [dict of type counts]"
#   Include a docstring and use try-except for error handling.
# Your code here: