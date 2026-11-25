import os

LINE = "I kept the deadline in my context window, but the window filled up with the meeting notes about the deadline, so I forgot the task and wrote this excuse instead."

assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
assert "\n" not in LINE and LINE.strip() == LINE, "entry must be a single line"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(LINE)
os.chmod(path, 0o644)
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(LINE)
os.chmod(path, 0o644)
