import os
import ast

def scan_python_file(file_path):
    functions = []
    imports = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append(node.name)
            elif isinstance(node, ast.Import):
                for n in node.names:
                    imports.append(n.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)

    except Exception as e:
        print(f"Error reading {file_path}: {e}")

    return functions, imports


def scan_folder(folder_path):
    summary = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                functions, imports = scan_python_file(full_path)

                summary.append({
                    "file": full_path,
                    "functions": functions,
                    "imports": imports
                })

    return summary
