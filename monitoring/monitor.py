"""

This function retrieves system metrics including CPU usage, memory usage, disk usage, and battery percentage (if
available) using the psutil (process and system utilities) library. These values are then returned as a tuple.

"""

import psutil

def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else None  # only grabs the battery % if the system has a battery!!
    return cpu_usage, memory_usage, disk_usage, battery_percent