📘 ERPNext Code Analyzer (CLI Tool)
👤 Author

Name: Abhi Pandey
Project: ERPNext

🧠 One-Line Description

A simple command-line tool that scans ERPNext Python code and helps beginners understand the code by showing structured information like functions and imports.

🎯 Purpose of This Project

ERPNext is a very large and complex project.
For new developers, it is difficult to understand how the code works by reading files one by one.

This tool helps beginners by:

Automatically scanning Python files

Extracting important details from the code

Presenting the output in a clean and structured format

🛠️ What This Tool Does

Scans a given folder for Python (.py) files

Extracts:

File names

Function names

Import statements

Saves all results in a JSON file

Prints a summary in the terminal for quick understanding

📁 Project Structure
code-analyzer/
├── analyzer.py     # Main CLI entry point
├── scanner.py      # Logic for scanning files and extracting data
└── output/
    └── summary.json

▶️ How to Run the Tool

Open Terminal / Command Prompt

Navigate to the project directory

Run the following command:

python analyzer.py .


. means the current folder will be scanned.

📤 Output
✅ Terminal Output

Displays:

Total number of Python files scanned

Total number of functions found

Total number of import statements found

Example:

Scanning files...
Files scanned: 2
Functions found: 3
Imports found: 6
JSON output saved to output/summary.json

📄 JSON Output

Saved at:

output/summary.json


Example content:

{
  "file": "scanner.py",
  "functions": ["scan_folder", "scan_python_file"],
  "imports": ["os", "ast"]
}

📚 What I Learned

How to scan folders and files using Python

How to analyze Python code programmatically

How to extract structured data from source code

How to build a basic CLI tool for real projects

🚀 Future Improvements

Add basic question answering like:

“Which file contains this function?”

Improve support for very large ERPNext codebases

Add diagrams and better summaries for easier understanding
