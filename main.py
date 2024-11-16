import psutil                                   # To monitor system metrics like CPU, memory, and disk space.
import smtplib                                  #  To send email alerts.
from email.mime.text import MIMEText            # to create email message objects that have plain text or HTML content.
from email.mime.multipart import MIMEMultipart  # used to create email messages that can have multiple parts.
import time

# This function monitors the system’s CPU, memory, and disk space usage.

def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage over 1 second
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent          # Memory usage in percentage
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent              # Disk usage in percentage
    return cpu_usage, memory_usage, disk_usage

#  This function will send an email when a threshold is exceeded.

def send_email(subject, body, to_email):
    from_email = "jessica.u.nguyen.dev@gmail.com"
    password = "caaf wxzp mwap sgqb"

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the mail server and send the email
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

# This loop will check the system metrics at regular intervals and send an email if any metric exceeds a the threshold.

def monitor_system():
    # Define the thresholds (e.g., 80% CPU, 80% memory, 90% disk)
    cpu_threshold = 80
    memory_threshold = 80
    disk_threshold = 90
    to_email = "jessica.u.nguyen.2003@gmail.com"

    while True:
        cpu, memory, disk = get_system_metrics()

        # Check if any metric exceeds the threshold
        if cpu > cpu_threshold:
            subject = "CPU Usage Alert"
            body = f"CPU usage is {cpu}%, which exceeds the threshold of {cpu_threshold}%."
            send_email(subject, body, to_email)

        if memory > memory_threshold:
            subject = "Memory Usage Alert"
            body = f"Memory usage is {memory}%, which exceeds the threshold of {memory_threshold}%."
            send_email(subject, body, to_email)

        if disk > disk_threshold:
            subject = "Disk Usage Alert"
            body = f"Disk usage is {disk}%, which exceeds the threshold of {disk_threshold}%."
            send_email(subject, body, to_email)

        time.sleep(60)  # Wait for 60 seconds before checking again

if __name__ == "__main__":
    monitor_system()
