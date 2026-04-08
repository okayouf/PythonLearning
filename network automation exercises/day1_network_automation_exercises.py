# ============================================
# Network Automation Exercises
# ============================================
# Practice your Python skills with networking-themed data!
# ============================================

# === SAMPLE DATA ===
# Use this data throughout the exercises

devices = [
    {"name": "switch-A", "type": "switch", "ip": "10.0.0.1", "status": "online"},
    {"name": "ap-lobby", "type": "access_point", "ip": "10.0.0.2", "status": "offline"},
    {"name": "switch-B", "type": "switch", "ip": "10.0.0.3", "status": "online"},
    {"name": "router-main", "type": "router", "ip": "192.168.1.1", "status": "online"},
    {"name": "ap-floor2", "type": "access_point", "ip": "172.16.0.5", "status": "offline"},
    {"name": "switch-C", "type": "switch", "ip": "10.0.0.4", "status": "online"},
    {"name": "firewall-1", "type": "firewall", "ip": "10.0.0.254", "status": "online"},
]

# Exercise 1:
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
def network_report(devices_list):
    """takes a list of dicts and makes a network report"""
    try:
        online_devices = [device['name'] for device in devices_list if device['status'] == 'online']
        offline_devices = [device['name'] for device in devices_list if device['status'] == 'offline']
        device_type = {device['name']:device['type'] for device in devices_list}
        device_count = {}
        for device in devices_list:
            if device['type'] in device_count:
                device_count[device['type']] += 1
            else:
                device_count[device['type']] = 1
        print("=== Network Report ===")
        print("Total devices:",len(online_devices) + len(offline_devices))
        print("Online:", len(online_devices),"-",online_devices)
        print("Offline:",len(offline_devices),"-",offline_devices)
        print("Device types:",device_count )
    except:
        print("please provide a list of dicts")

network_report(devices)