import sys
import json
import os
from scanner import scan_folder

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <project_folder>")
        return

    project_folder = sys.argv[1]

    print("Scanning files...")
    results = scan_folder(project_folder)

    total_files = len(results)
    total_functions = sum(len(r["functions"]) for r in results)
    total_imports = sum(len(r["imports"]) for r in results)

    print(f"Files scanned: {total_files}")
    print(f"Functions found: {total_functions}")
    print(f"Imports found: {total_imports}")

    os.makedirs("output", exist_ok=True)

    with open("output/summary.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print("JSON output saved to output/summary.json")

if __name__ == "__main__":
    main()
