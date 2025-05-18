import random
import os

filename = "big_output.txt"
limit = 10 * 1024  # 10 KB for fallback check

try:
    with open(filename, "a") as f:
        while True:
            line = str(random.randint(1, 100)) + "\n"
            f.write(line)
            if os.path.getsize(filename) > limit:
                print("Limit reached by check, stopping.")
                break
except OSError as e:
    print(f"Write failed: {e}")
