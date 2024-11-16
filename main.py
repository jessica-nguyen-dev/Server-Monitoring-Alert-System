import psutil                                   # monitor system metrics like CPU, memory, and disk space
import smtplib                                  # send email alerts
from email.mime.text import MIMEText            # create email message objects that have plain text or HTML content
from email.mime.multipart import MIMEMultipart  # create email messages that can have multiple parts
from config import settings
import time
import logging
import os

# Set up logging configuration

logging.basicConfig(
    filename=os.path.join('logs', 'monitoring.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format: timestamp, log level, message
)

# This function monitors the system’s CPU, memory, and disk space usage, as well as battery level!

def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)              # Get CPU usage over 1 second
    memory_usage = psutil.virtual_memory().percent          # Memory usage in percentage
    disk_usage = psutil.disk_usage('/').percent             # Disk usage in percentage
    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else None  # Handle systems without a battery (non-laptops mostly)
    return cpu_usage, memory_usage, disk_usage, battery_percent

#  This function will send an email when a threshold is exceeded.

def send_email(subject, body, to_email):
    from_email = "jessica.u.nguyen.dev@gmail.com"
    password = "caaf wxzp mwap sgqb"

    # Create the email message
    msg = MIMEMultipart()                           # creates a new email message object using the MIMEMultipart class
    msg['From'] = from_email                        # defined by the monitor_system function
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))    # attaches the body of the email to the msg in plain text format

    # After connecting to Gmail's SMTP server, the program logs in with the credentials (provided above), sends an email
    # with the specified subject and body, and ensures a secure connection using TLS encryption. It formats the message
    # with MIME and handles any errors by printing an exception message.

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Using Gmail's SMTP server
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Checks the system metrics at regular intervals and send an email if any metric exceeds the threshold.

def monitor_system():
    # Define the thresholds
    cpu_threshold = settings.CPU_THRESHOLD
    memory_threshold = settings.MEMORY_THRESHOLD
    disk_threshold = settings.DISK_THRESHOLD
    battery_threshold = settings.BATTERY_THRESHOLD
    monitor_interval = settings.MONITOR_INTERVAL

    to_email = settings.EMAIL_RECEIVER

    while True:
        cpu, memory, disk, battery= get_system_metrics()

        # Check if any metric exceeds the threshold, and log the issue if true
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

        if disk > disk_threshold:
            subject = "Battery Alert"
            body = f"Battery level is {battery}%, which is below the threshold of {battery_threshold}%."
            send_email(subject, body, to_email)
            logging.warning(f"Battery level is below {battery_threshold}%: {battery}%")

        # Log general activity (even if thresholds aren't exceeded)
        logging.info(f"CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%")

        time.sleep(monitor_interval)  # Wait for X amount of seconds before checking again

if __name__ == "__main__":
    monitor_system()
