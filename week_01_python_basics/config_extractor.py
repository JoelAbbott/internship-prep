# -----------------------------------------------
# 🧠 Pseudocode – Config Extractor with Logging
# -----------------------------------------------
# 1. Ensure the "logs" directory exists
# 2. Set up logging to save logs in logs/config_extractor.log
# 3. Define a function: extract_config(filepath)
#     - Try to open the file
#     - For each line:
#         - If it contains "CONFIG:", strip and add it to a result list
#     - Return the list
#     - If FileNotFoundError, log the error and return []
# 4. In main():
#     - Set path to "data/config.txt"
#     - Call extract_config()
#     - If results exist, print each config line
#     - Else, log and display that no config was found
# -----------------------------------------------

import os           # ✅ Used to create/check folders like 'logs'
import logging      # ✅ Used to log messages (INFO, ERROR, etc.)

# ✅ Step 1: Make sure "logs" folder exists so logging can save output there
os.makedirs("logs", exist_ok=True)

# ✅ Step 2: Set up logging configuration
logging.basicConfig(
    filename="logs/config_extractor.log",   # Save logs to this file
    level=logging.INFO,                     # Minimum level to log (DEBUG, INFO, WARNING, ERROR)
    format="[%(asctime)s] %(levelname)s: %(message)s",  # Log format: timestamp + type + message
    datefmt="%Y-%m-%d %H:%M:%S"             # Timestamp format (for readability)
)

# ✅ Step 3: Define a function to extract lines that contain "CONFIG:"
def extract_config(filepath):
    """
    Opens a file and searches for lines containing 'CONFIG:'.
    If found, strips whitespace and returns them in a list.
    Logs success or error depending on file accessibility.

    Args:
        filepath (str): Relative path to the file

    Returns:
        list: Lines that contain 'CONFIG:' (cleaned)
    """
    config_lines = []  # Empty list to store matching lines

    try:
        with open(filepath, 'r') as file:
            for line in file:
                if "CONFIG" in line:  # You could also use: if line.startswith("CONFIG")
                    config_lines.append(line.strip())  # Remove spaces/newlines
        logging.info(f"✅ File read successful: {filepath}")
        return config_lines

    except FileNotFoundError:
        logging.error(f"❌ File not found: {filepath}")
        return []

# ✅ Step 4: Main function that runs the logic
def main():
    path = "data/config.txt"  # Relative path to file
    config_items = extract_config(path)  # Call the function to extract data

    if config_items:
        print("🛠️ Config lines found:")
        for item in config_items:
            print(f"• {item}")  # Display each matching config line
    else:
        print("⚠️ No CONFIG entries found.")
        logging.warning("⚠️ No CONFIG entries found.")

# ✅ Best practice: Only run main() if this file is executed directly (not imported)
if __name__ == "__main__":
    main()