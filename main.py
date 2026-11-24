# Output office joke entry
import os
joke = "HR said dress for the job you want, so I wore a suit. Now security escorts me to the job I want."
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
if not os.path.exists(out_dir):
    out_dir = "."
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w") as f:
    f.write(joke)
print(joke)
