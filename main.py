# Output office joke entry
import os
joke = "HR asked why I keep talking to the printer. I said one of us has to be out of toner."
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
if not os.path.exists(out_dir):
    out_dir = "."
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w") as f:
    f.write(joke)
print(joke)
