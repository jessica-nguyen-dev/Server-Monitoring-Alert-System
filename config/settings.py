"""
Configure settings for the Server Monitoring and Alert System here.

To securely set your email password, use the EMAIL_PASSWORD environment variable:
    - Windows (Command Prompt): set EMAIL_PASSWORD=your-email-password
    - Windows (PowerShell): $Env:EMAIL_PASSWORD = "your-email-password"
    - macOS/Linux (Terminal): export EMAIL_PASSWORD=your-email-password
    - In PyCharm, add the variable in the run/debug configuration.

If not set, the default value will be used for testing.

Other settings, like thresholds and email details, can be customized in this file.
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