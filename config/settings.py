"""
Configure settings for the Server Monitoring and Alert System here.

IMPORTANT NOTE: To set email details, define your environment variables in your operating system or environment.

If you don't want to use your own email to send the alerts, you can keep mine and just change the
receiving address! This is an email I made specifically to test this project, so you can use it. If you use your own,
generate an APP PASSWORD through Google first, and use that instead of your actual password to bypass 2FA.

For example, on Windows (Command Prompt or PowerShell):
    set EMAIL_USERNAME=jessica.u.nguyen.dev@gmail.com       (replace with your own if you prefer)
    set EMAIL_PASSWORD=caaf wxzp mwap sgqb                  (your app password should look like this)

Other settings, like thresholds and the alert recipient, can be customized below!!
"""

# Email settings

import os

EMAIL_HOST = "smtp.gmail.com"  # Replace with your email provider's SMTP server
EMAIL_PORT = 587  # Replace with the SMTP port (usually 587 for TLS)
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = "jessica.u.nguyen.2003@gmail.com"

# Threshold settings (all values are in terms of percent)
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90
BATTERY_THRESHOLD = 20

# Monitoring interval (aka amount of time between checks, in seconds)
MONITOR_INTERVAL = 60