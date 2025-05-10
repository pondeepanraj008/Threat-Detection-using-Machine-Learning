import psutil
import subprocess
import re
import joblib
import pandas as pd

# Load trained model
model = joblib.load("threat_detection_model.pkl")

# Function to check for network activity (Metasploit detection)
def check_network_activity():
    netstat_output = subprocess.run(["netstat", "-ano"], capture_output=True, text=True, shell=True)
    if re.search(r'\b4444\b', netstat_output.stdout):  # Check if port 4444 (Metasploit) is active
        print("Suspicious activity detected on port 4444.")
        return True
    return False

# Function to check for keylogger activity
def check_process_activity():
    for proc in psutil.process_iter(['name']):
        if "keylogger" in proc.info['name'].lower():
            print(f"Keylogger detected: {proc.info['name']}")
            return True
    return False
