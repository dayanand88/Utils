import os

# Define the file names and their initial content
files = {
    "config.json": "{}",
    "fetch_data.py": "# Code for fetching data\n",
    "indicators.py": "# Code for indicators\n",
    "strategy.py": "# Code for strategy\n",
    "google_sheets.py": "# Code for Google Sheets\n",
    "main.py": "# Main entry point for the project\n",
    "requirements.txt": "# List your dependencies here\n"
}

# Create each file with its content
for filename, content in files.items():
    with open(filename, 'w') as file:
        file.write(content)

print("Files created successfully.")
