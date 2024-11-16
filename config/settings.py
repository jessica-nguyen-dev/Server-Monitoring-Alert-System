"""
This is where you can configure the settings for the Server Monitoring and Alert System.

To securely set your email password, set the EMAIL_PASSWORD environment variable on your system:
    - On Windows (Command Prompt): set EMAIL_PASSWORD=your-email-password
    - On Windows (PowerShell): $Env:EMAIL_PASSWORD = "your-email-password"
    - On macOS/Linux (Terminal): export EMAIL_PASSWORD=your-email-password
    - In PyCharm, click on the three dots to the right of the run/debug buttons, click edit configuration, and add your
      environment variable from there (make sure to name it EMAIL_PASSWORD).

If the environment variable is not set, the default value provided here will be used for testing purposes!

Other settings (like thresholds and email server details) can be customized directly in this file.
"""

import os

# Email settings
EMAIL_HOST = "smtp.gmail.com"                       # Replace with your email provider's SMTP server
EMAIL_PORT = 587                                    # Replace with the SMTP port (usually 587 for TLS)
EMAIL_USERNAME = "jessica.u.nguyen.dev@gmail.com"
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "caaf wxzp mwap sgqb")    # default password from my mock email
EMAIL_RECEIVER = "jessica.u.nguyen.2003@gmail.com"

# Threshold settings
CPU_THRESHOLD = 80                          # CPU usage percentage threshold
MEMORY_THRESHOLD = 80                       # Memory usage percentage threshold
DISK_THRESHOLD = 90                         # Disk usage percentage threshold
BATTERY_THRESHOLD = 20                      # Battery level threshold (in percentage)

# Monitoring interval
MONITOR_INTERVAL = 60                       # Interval between checks, in seconds