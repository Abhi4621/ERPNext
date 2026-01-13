📘 ERPNext Code Analyzer (CLI Tool)
Author: Abhi Pandey

Project: ERPNext Utility

🧠 Overview
ERPNext is a massive, enterprise-grade codebase. For new developers, navigating thousands of files to understand logic flow can be overwhelming.

ERPNext Code Analyzer is a lightweight command-line interface (CLI) tool designed to help beginners deconstruct Python files. It identifies the "what" and "where" of the code without requiring the developer to read every line manually.

🎯 Purpose
Simplify Onboarding: Helps new developers map out the structure of ERPNext modules.

Automated Scanning: Removes the manual effort of searching for function definitions.

Structured Insights: Converts raw code into readable JSON data for further analysis or documentation.

🛠️ Key Features
Recursive Scanning: Walks through directories to find all .py files.

AST Analysis: Uses Python's Abstract Syntax Tree (AST) to accurately identify:

Function Names: Every logic block defined in the file.

Import Statements: External dependencies and internal module links.

Dual Output: * Terminal Summary: Quick stats for immediate feedback.

JSON Export: A persistent data file for deep dives.

📁 Project Structure
Plaintext

code-analyzer/
├── analyzer.py     # Main CLI entry point (handles user input)
├── scanner.py      # Core logic (AST parsing and file traversal)
└── output/
    └── summary.json # Generated results
▶️ Getting Started
1. Installation
Ensure you have Python 3.x installed. Clone this repository to your local machine:

Bash

git clone https://github.com/your-username/erpnext-code-analyzer.git
cd erpnext-code-analyzer
2. Usage
Run the analyzer by pointing it to any ERPNext app or specific folder:

Bash

python analyzer.py /path/to/erpnext/module
Note: Use . to scan the current directory.

📤 Output Examples
✅ Terminal Output
Plaintext

Scanning files...
---------------------------------------
Files scanned  : 12
Functions found: 45
Imports found  : 112
---------------------------------------
✅ Success! JSON output saved to output/summary.json
📄 JSON Output (summary.json)
JSON

{
  "file": "controllers/sales_order.py",
  "functions": [
    "make_sales_invoice",
    "on_submit",
    "validate_warehouse"
  ],
  "imports": [
    "frappe",
    "frappe.model.document",
    "erpnext.controllers.selling_controller"
  ]
}
📚 Technical Learnings
During the development of this tool, I explored:

File I/O: Navigating complex directory trees using the os and pathlib libraries.

Static Analysis: Using the ast module to inspect code without executing it.

Data Serialization: Structuring Python objects into clean, portable JSON.

CLI Design: Creating a user-friendly experience in the terminal.

🚀 Future Roadmap
[ ] Search Functionality: "Which file contains the function get_query?"

[ ] Dependency Graphing: Visualize how different ERPNext files import one another.

[ ] Docstring Extraction: Include function descriptions in the summary.
