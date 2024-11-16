import time
import logging
import os
from monitoring.monitor import get_system_metrics
from alerts.email_alert import send_email
from config import settings

# Set up logging configuration
logging.basicConfig(
    filename=os.path.join('logs', 'monitoring.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def monitor_system():
    cpu_threshold = settings.CPU_THRESHOLD
    memory_threshold = settings.MEMORY_THRESHOLD
    disk_threshold = settings.DISK_THRESHOLD
    battery_threshold = settings.BATTERY_THRESHOLD
    monitor_interval = settings.MONITOR_INTERVAL
    to_email = settings.EMAIL_RECEIVER

    while True:
        cpu, memory, disk, battery = get_system_metrics()

        # Check thresholds and send alerts
        if cpu > cpu_threshold:
            subject = "CPU Usage Alert"
            body = f"CPU usage is {cpu}%, which exceeds the threshold of {cpu_threshold}%."
            send_email(subject, body, to_email)
            logging.warning(f"CPU usage exceeded {cpu_threshold}%: {cpu}%")

        if memory > memory_threshold:
            subject = "Memory Usage Alert"
            body = f"Memory usage is {memory}%, which exceeds the threshold of {memory_threshold}%."
            send_email(subject, body, to_email)
            logging.warning(f"Memory usage exceeded {memory_threshold}%: {memory}%")

        if disk > disk_threshold:
            subject = "Disk Usage Alert"
            body = f"Disk usage is {disk}%, which exceeds the threshold of {disk_threshold}%."
            send_email(subject, body, to_email)
            logging.warning(f"Disk usage exceeded {disk_threshold}%: {disk}%")

        if battery < battery_threshold:
            subject = "Battery Alert"
            body = f"Battery level is {battery}%, which is below the threshold of {battery_threshold}%."
            send_email(subject, body, to_email)
            logging.warning(f"Battery level is below {battery_threshold}%: {battery}%")

        # Log general activity
        logging.info(f"CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%")

        time.sleep(monitor_interval)

if __name__ == "__main__":
    monitor_system()