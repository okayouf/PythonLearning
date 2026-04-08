# ============================================
# Exercise 1: Device Health Monitor
# ============================================
# Write a function called "health_monitor" that takes *args of device dicts and:
#   1. Uses a list comprehension to get names of all CRITICAL offline devices
#      (critical = type is "router" or "firewall")
#   2. Calculates a health score: (online devices / total devices) * 100, rounded to 1 decimal
#   3. Groups devices by location into a dict: {location: [list of device names]}
#      Hint: a plain dict comprehension won't work here — think about why,
#      and use a regular loop instead.
#   4. Prints a report:
#       "=== Health Monitor ==="
#       "Health score: [score]%"
#       "Critical offline devices: [list]"
#       "Devices by location: [dict]"
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

# Your code here:


health_monitor(*devices)
