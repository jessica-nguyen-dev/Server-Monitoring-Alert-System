"""
Configure settings for the Server Monitoring and Alert System here.

To securely set your email password, use the EMAIL_PASSWORD environment variable:
    - Windows (Command Prompt):     set EMAIL_PASSWORD=your-email-password
    - Windows (PowerShell):         $Env:EMAIL_PASSWORD = "your-email-password"
    - macOS/Linux (Terminal):       export EMAIL_PASSWORD=your-email-password

    For PyCharm Users: add the variable by clicking "more actions" next to the run/debug buttons. Then, click edit and add
    the variable, making sure to name it "EMAIL_PASSWORD".

If not set, the default value will be used for testing (this is an email I made specifically for this project you can use it!)

Other settings, like thresholds and email details, can be customized below.
"""

import os

# Email settings - IMPORTANT NOTE:
# If you don't want to use your own email to send the alerts, you can keep mine and just change the receiving address!

EMAIL_HOST = "smtp.gmail.com"  # Replace with your email provider's SMTP server
EMAIL_PORT = 587  # Replace with the SMTP port (usually 587 for TLS)
EMAIL_USERNAME = "jessica.u.nguyen.dev@gmail.com"
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "caaf wxzp mwap sgqb")    # default password from my mock email
EMAIL_RECEIVER = "jessica.u.nguyen.2003@gmail.com"

# Threshold settings (all values are in terms of percent)
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90
BATTERY_THRESHOLD = 20

# Monitoring interval (aka amount of time between checks, in seconds)
MONITOR_INTERVAL = 60