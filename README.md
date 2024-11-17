# System Monitoring and Alert Tool

A Python-based tool for monitoring system metrics (CPU, memory, disk usage, and battery) that sends email alerts when 
certain thresholds are exceeded. 

## Features
- Monitors CPU, memory, disk, and battery levels
- Sends email alerts when usage exceeds set thresholds
- Customizable monitoring intervals and thresholds

## Installation

1. Clone the repository:
   ```bash
   git clone <https://github.com/jessica-nguyen-dev/Server-Monitoring-Alert-System.git>
   cd <repo_folder>

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Configure settings in `config/settings.py`:
   - Set your email details (`EMAIL_HOST`, `EMAIL_PORT`, etc.).
   - Adjust thresholds for CPU, memory, disk, and battery usage.

_Important Note: If you'd like, you can keep my email settings and simply change the recipient address to your own for convenience. 
I created that email specifically for testing this project anyway!_

## Usage

To start monitoring your system:
```bash
python main.py
