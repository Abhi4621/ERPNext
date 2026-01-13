📘 ERPNext Code Analyzer (CLI Tool)
👤 Author

Name: Abhi Pandey
Project: ERPNext

🧠 One-line Description

I am building a simple CLI tool that scans ERPNext code files and helps me understand what the code is doing by showing structured output and answering basic questions.

🎯 Purpose of This Project

ERPNext is a very large project.
For new developers, it is hard to understand the code by reading every file.

This tool helps by:

Scanning Python files

Extracting useful information

Showing structured output in a simple way

🛠️ What This Tool Does

Scans a given folder for Python (.py) files

Finds:

File names

Functions

Import statements

Saves the result in a JSON file

Displays a short summary in the terminal

📁 Project Structure
code-analyzer/
├── analyzer.py     # Main CLI file
├── scanner.py      # Scans files and extracts code info
└── output/
    └── summary.json

▶️ How to Run the Tool

Open terminal / command prompt

Go to the project folder

Run the command:

python analyzer.py .


(The dot . means current folder)

📤 Output
Terminal Output

Shows:

Number of files scanned

Number of functions found

Number of imports found

JSON Output

Saved at:

output/summary.json


Example:

{
  "file": "scanner.py",
  "functions": ["scan_folder", "scan_python_file"],
  "imports": ["os", "ast"]
}

📚 What I Learned

How to scan folders using Python

How to read and analyze Python code files

How to extract structured information from code

How to build a basic CLI tool

🚀 Future Improvements

Add simple question answering like:

“Where is this function used?”

Support for large ERPNext folders

Better summaries and diagrams
