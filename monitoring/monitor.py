import psutil

def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else None
    return cpu_usage, memory_usage, disk_usage, battery_percent