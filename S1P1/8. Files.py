import csv
import json
from datetime import datetime

# Assignment 1: Convert CSV to JSON
def csv_to_json(csv_file, json_file):
    """Converts a CSV file to JSON."""
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

# Test Assignment 1
csv_to_json('products.csv', 'products.json')

# Assignment 2: Log File Writer
def log_message(message, log_file):
    """Writes a log message with timestamp to a file."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {message}\n"
    with open(log_file, 'a') as file:
        file.write(log_entry)

# Test Assignment 2
log_message("User 'Alice' logged in.", 'app.log')
log_message("Error: Connection timed out.", 'app.log')
log_message("User 'Bob' accessed the dashboard.", 'app.log')
