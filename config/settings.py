# Email settings
EMAIL_HOST = "smtp.example.com"             # Replace with your email provider's SMTP server
EMAIL_PORT = 587                            # Replace with the SMTP port (usually 587 for TLS)
EMAIL_USERNAME = "your-email@example.com"   # Your email address
EMAIL_PASSWORD = "your-email-password"      # Your email password
EMAIL_USE_TLS = True                        # Whether to use TLS for secure connections
EMAIL_RECEIVER = "jessica.u.nguyen.2003@gmail.com"

# Threshold settings
CPU_THRESHOLD = 80                          # CPU usage percentage threshold
MEMORY_THRESHOLD = 80                       # Memory usage percentage threshold
DISK_THRESHOLD = 90                         # Disk usage percentage threshold
BATTERY_THRESHOLD = 20                      # Battery level threshold (in percentage)

# Monitoring interval
MONITOR_INTERVAL = 60                       # Interval between checks, in seconds