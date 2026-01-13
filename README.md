# 📘 ERPNext Code Analyzer (CLI Tool)

**Author:** Abhi Pandey  
**Project:** ERPNext Developer Experience  

---

## 🧠 One-Line Description
A simple command-line tool that scans ERPNext Python code and helps beginners understand the codebase by displaying structured information like functions and imports.

---

## 🎯 Purpose of This Project
ERPNext is a very large and complex project. For new developers, it is difficult to understand how the code works by reading files one by one.

This tool helps beginners by:
- Automatically scanning Python files  
- Extracting important details directly from the source code  
- Presenting the output in a clean, structured, and easy-to-read format  

---

## 🛠️ What This Tool Does
- Scans any given folder for Python (`.py`) files  
- Extracts key metadata:
  - File names  
  - Function names (logic blocks)  
  - Import statements (dependencies)  
- Saves all results into a structured `summary.json` file  
- Prints a high-level summary in the terminal for quick reference  

---

## 📁 Project Structure
code-analyzer/
├── analyzer.py # Main CLI entry point
├── scanner.py # Logic for scanning files and extracting data
└── output/
└── summary.json # Structured scan results

---

## ▶️ How to Run the Tool
1. Open Terminal or Command Prompt  
2. Navigate to the project directory  
3. Run the command:
```bash
python analyzer.py .

---

## ▶️ How to Run the Tool
1. Open Terminal or Command Prompt  
2. Navigate to the project directory  
3. Run the command:
```bash
python analyzer.py .
📤 Output
✅ Terminal Output
Scanning files...
Files scanned: 2
Functions found: 3
Imports found: 6
JSON output saved to output/summary.json
📄 JSON Output

Stored in output/summary.json:
{
  "file": "scanner.py",
  "functions": ["scan_folder", "scan_python_file"],
  "imports": ["os", "ast"]
}
📚 What I Learned

File system navigation using Python

Static code analysis without executing code

Structuring extracted data using JSON

Building a practical CLI tool for developer workflows

🚀 Future Improvements

Add direct search: “Which file contains this function?”

Improve performance for very large ERPNext codebases

Generate diagrams or flowcharts for better visualization
