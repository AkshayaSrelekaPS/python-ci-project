import os
import ast

total_lines = 0
missing_docstrings = []

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):

            path = os.path.join(root, file)

            with open(path, "r") as f:
                total_lines += len(f.readlines())

            with open(path, "r") as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if not ast.get_docstring(node):
                        missing_docstrings.append(
                            f"{path}: {node.name}"
                        )

print("TOTAL_LINES=", total_lines)

if missing_docstrings:
    print("DOCSTRING_FAIL")
    for item in missing_docstrings:
        print(item)
else:
    print("DOCSTRING_PASS")
