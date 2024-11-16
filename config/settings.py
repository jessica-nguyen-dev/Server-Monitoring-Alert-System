"""
Configure settings for the Server Monitoring and Alert System here.

IMPORTANT NOTE: If you don't want to use your own email to send the alerts, you can keep mine and just change the
receiving address! This is an email I made specifically for this project you can use it. If you use your own, generate
an APP PASSWORD through Google first, and use that instead of your actual password to bypass 2FA.

Other settings, like thresholds and email details, can be customized below!
"""

# Email settings

EMAIL_HOST = "smtp.gmail.com"  # Replace with your email provider's SMTP server
EMAIL_PORT = 587  # Replace with the SMTP port (usually 587 for TLS)
EMAIL_USERNAME = "jessica.u.nguyen.dev@gmail.com"
EMAIL_PASSWORD = "caaf wxzp mwap sgqb"
EMAIL_RECEIVER = "jessica.u.nguyen.2003@gmail.com"

# Threshold settings (all values are in terms of percent)
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90
BATTERY_THRESHOLD = 20

# Monitoring interval (aka amount of time between checks, in seconds)
MONITOR_INTERVAL = 60