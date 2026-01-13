📘 ERPNext Code Analyzer (CLI Tool)
Author: Abhi Pandey

Project: ERPNext Developer Experience

🧠 One-Line Description
A simple command-line tool that scans ERPNext Python code and helps beginners understand the codebase by displaying structured information like functions and imports.

🎯 Purpose of This Project
ERPNext is a very large and complex project. For new developers, it is difficult to understand how the code works by reading files one by one.

This tool helps beginners by:

Automatically scanning Python files.

Extracting important details directly from the source code.

Presenting the output in a clean, structured, and easy-to-read format.

🛠️ What This Tool Does
Scans any given folder for Python (.py) files.

Extracts vital metadata:

File names

Function names (logic blocks)

Import statements (dependencies)

Saves all results into a structured summary.json file.

Prints a high-level summary in the terminal for quick reference.

📁 Project Structure
Plaintext


code-analyzer/
├── analyzer.py      # Main CLI entry point
├── scanner.py       # Logic for scanning files and extracting data
└── output/
    └── summary.json # Structured scan results
▶️ How to Run the Tool
Open Terminal or Command Prompt.

Navigate to the project directory.

Run the following command:

Bash

python analyzer.py .
(The . means the current folder and all subfolders will be scanned.)

📤 Output
✅ Terminal Output
The terminal provides an immediate snapshot of the codebase:

Plaintext

Scanning files...
Files scanned: 2
Functions found: 3
Imports found: 6
JSON output saved to output/summary.json
📄 JSON Output
Results are stored in output/summary.json for deep analysis:

JSON

{
  "file": "scanner.py",
  "functions": ["scan_folder", "scan_python_file"],
  "imports": ["os", "ast"]
}
📚 What I Learned
File System Navigation: How to programmatically scan folders and files using Python.

Static Code Analysis: Using Python libraries to "read" and understand code without running it.

Data Serialization: Organizing raw source code data into structured JSON format.

CLI Development: Building a functional command-line utility for real-world developer workflows.

🚀 Future Improvements
Direct Search: Add a feature to answer: “Which file contains this function?”

Scalability: Improve performance for massive ERPNext codebases with thousands of files.

Visual Documentation: Generate flowcharts or diagrams automatically for better understanding.
