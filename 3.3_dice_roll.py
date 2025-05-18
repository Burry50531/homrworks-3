import random
import os

filename = "dice_rolls.txt"
limit = 1024  # 1 KB max file size

with open(filename, "a") as f:
    while True:
        if os.path.getsize(filename) >= limit:
            print("File size limit exceeded")
            break
        roll = random.randint(1, 6)
        f.write(f"{roll}\n")
