import os

count = 0

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)

            try:
                with open(path) as f:
                    for line_no, line in enumerate(f, start=1):
                        if "TODO" in line or "FIXME" in line:
                            print(f"{path}:{line_no}: {line.strip()}")
                            count += 1
            except:
                pass

print(f"TOTAL_TODOS={count}")

