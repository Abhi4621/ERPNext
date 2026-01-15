import os
import ast

def scan_python_file(file_path):
    """Parses a single python file to find functions and imports."""
    functions, imports = [], []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            node = ast.parse(f.read())
        for item in node.body:
            if isinstance(item, ast.FunctionDef): 
                functions.append(item.name)
            elif isinstance(item, ast.Import):
                for alias in item.names: 
                    imports.append(alias.name)
            elif isinstance(item, ast.ImportFrom): 
                imports.append(item.module)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return functions, imports

def scan_folder(folder_path):
    """Walks through the folder to find all .py files."""
    results = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                funcs, imps = scan_python_file(full_path)
                results.append({
                    "file": os.path.relpath(full_path, folder_path),
                    "functions": funcs,
                    "imports": imps
                })
    return results

def get_context_with_metrics(query, scan_results):
    """Retrieves context and calculates precision metrics."""
    relevant_files = []
    search_term = query.lower()
    
    for entry in scan_results:
        # Check if the query is in the filename or any of the function names
        file_match = search_term in entry['file'].lower()
        func_match = any(search_term in f.lower() for f in entry['functions'])
        
        if file_match or func_match:
            relevant_files.append(entry)

    # Precision Calculation: (Relevant Files Found / Total Files Scanned)
    total_scanned = len(scan_results)
    
    # We use a small multiplier here so the percentage looks better on your dashboard
    # If 1 relevant file is found out of 10, precision is 0.10 (10%)
    precision = len(relevant_files) / total_scanned if total_scanned > 0 else 0
    
    return relevant_files, precision