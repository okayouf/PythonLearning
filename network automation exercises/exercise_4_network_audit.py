# ============================================
# Exercise 4: Full Network Audit (Boss Level)
# ============================================
# This exercise combines everything. Take your time.
#
# Step 1 — Write a generator function called "device_stream" that takes
# a list of devices and yields one device at a time.
#
# Step 2 — Write a function called "network_audit" that takes a devices list
# and a logs list and:
#   1. Consumes the "device_stream" generator to loop through devices and build:
#       a. A count of devices per type (same pattern as day 1)
#       b. A dict of {name: ip} for online devices only — using a dict comprehension
#       c. A list of offline device names — using a list comprehension
#   2. Reuses your "error_logs" generator from Exercise 2 to find devices with errors.
#      Build a set of device names that have at least one error.
#      Hint: sets automatically remove duplicates — you can use set() or add to a set in a loop
#   3. Cross-references: finds online devices that also appear in the error set
#      Hint: loop through online device names and check if each is in the error set
#   4. Prints a full audit report:
#       "=== Full Network Audit ==="
#       "Devices by type: [dict]"
#       "Offline devices: [list]"
#       "Online device IPs: [dict]"
#       "Devices with errors: [set]"
#       "Online but has errors: [list]  <-- these need attention!"
#   Include a docstring and try-except.
# ============================================

devices = [
    {"name": "switch-A",    "type": "switch",       "ip": "10.0.0.1",    "status": "online",  "location": "floor1"},
    {"name": "switch-B",    "type": "switch",       "ip": "10.0.0.2",    "status": "online",  "location": "floor1"},
    {"name": "switch-C",    "type": "switch",       "ip": "10.0.1.1",    "status": "offline", "location": "floor2"},
    {"name": "router-main", "type": "router",       "ip": "192.168.1.1", "status": "online",  "location": "server_room"},
    {"name": "router-bkp",  "type": "router",       "ip": "192.168.1.2", "status": "offline", "location": "server_room"},
    {"name": "firewall-1",  "type": "firewall",     "ip": "10.0.0.254",  "status": "online",  "location": "server_room"},
    {"name": "ap-lobby",    "type": "access_point", "ip": "172.16.0.1",  "status": "offline", "location": "lobby"},
    {"name": "ap-floor1",   "type": "access_point", "ip": "172.16.0.2",  "status": "online",  "location": "floor1"},
    {"name": "ap-floor2",   "type": "access_point", "ip": "172.16.0.3",  "status": "online",  "location": "floor2"},
]

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


network_audit(devices, logs)
