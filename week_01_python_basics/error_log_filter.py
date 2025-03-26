# error_log_filter.py

# confirm that the logs directory exists (os)
# Set up logging (logginh)
# Define a function filter_errors(filepath)
#   Try to open the file
#       Read each line
#       if the line contains 'ERROR' add it to results
#       Return the results list
#   if file not found
#       show error and return []
# In main:
#   set path to a simple log file
#   call filer_errors()
#   print number of errors found
#   print each error line

import logging
import os

# ✅ Ensure logs directory exists
os.makedirs("logs", exist_ok = True)


# ✅ Set up Logging config
logging.basicConfig(
    filename = "logs/error_filter.log", # Save the logs to this file
    level = logging.INFO,  # Set minimum log level
    format = '[%(asctime)s] %(levelname)s: %(message)s',  # The log format
    datefmt = '%y-%m-%d %H:%M:%S'   # Timestamo format
)

# Function to read each line, check if it starts with "Error" and log success or error
def filter_errors(filepath):
    lines = []
    try:
        with open(filepath, 'r') as file:
            for line in file.readlines():
                if line.startswith("ERROR"):
                    lines .append(line.strip()) # Add matching line to the list
        logging.info(f"Successfully read file: {filepath}")
        return lines
    except FileNotFoundError:
        logging.error(f"File Not Found: {filepath}")
        return []
    
# ✅ Main script logic
def main():
    path = "data/settings.txt"
    new_list = filter_errors(path)

    if new_list:
        logging.info("Displaying lines that start with ERRORS...")
        for line in new_list:
            print(f".{line}")
    else:
        logging.warning("No ERRORS to display")

# ✅ Run the script if this is the main file
if __name__ == "__main__":
    main()