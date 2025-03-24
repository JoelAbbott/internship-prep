# file_reader_logger.py

# -----------------------------------------------
# 🧠 Pseudocode – File Reader & Logger Script
# -----------------------------------------------
# Define a function named read_file that takes a file path:
#   Try to open the file
#     Read each line from the file
#     Strip space (so it's clean)
#     Add it to a list
#     Return the list
#   If file is not found:
#     Show an error
#     Return an empty list

# Main part of the script:
#   Set the file path
#   Call the read_file function
#   If it returned data:
#       Print the cleaned lines
#       Print how many lines were found
#   If it didn’t:
#       Print a message saying "no data"
# -----------------------------------------------

# Step 1: Define a function to read and clean file contents
def read_file(filepath):
    """
    Tries to open a file and return a list of cleaned lines.
    Handles missing file errors gracefully.
    """
    try:
        with open(filepath, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        return lines
    except FileNotFoundError:
        print(f"❌ Error: File '{filepath}' not found.")
        return []

# Step 2: Main function to call the logic
def main():
    path = "data/settings.txt"
    cleaned_data = read_file(path)

    if cleaned_data:
        print("📄 File Contents:")
        for line in cleaned_data:
            print(f"• {line}")
        print(f"\n✅ Total lines: {len(cleaned_data)}")
    else:
        print("⚠️ No data to display.")

# Step 3: Only run main() if this script is run directly
if __name__ == "__main__":
    main()
