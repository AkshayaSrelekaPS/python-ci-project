import subprocess

files = subprocess.check_output(
    ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
    text=True
).splitlines()

diff = subprocess.check_output(
    ["git", "diff", "--numstat", "HEAD~1", "HEAD"],
    text=True
)

added = 0
deleted = 0

for line in diff.splitlines():
    parts = line.split()
    if len(parts) >= 2:
        try:
            added += int(parts[0])
            deleted += int(parts[1])
        except:
            pass

todos = []

for file in files:
    try:
        with open(file) as f:
            for n, line in enumerate(f, start=1):
                if "TODO" in line or "FIXME" in line:
                    todos.append(f"{file}:{n}: {line.strip()}")
    except:
        pass

with open("report.md", "w") as f:
    f.write("# PR Review Summary\n\n")
    f.write(f"Files changed: {len(files)}\n\n")
    f.write(f"Lines added: {added}\n\n")
    f.write(f"Lines removed: {deleted}\n\n")

    if todos:
        f.write("## TODO/FIXME Found\n")
        for item in todos:
            f.write(f"- {item}\n")
    else:
        f.write("No TODO/FIXME found.\n")
