import sys
import os

if len(sys.argv) != 3:
    print("Program need two arguments")
    sys.exit(1)

src, dst = sys.argv[1], sys.argv[2]

try:
    with open(src, "rb") as fsrc:
        try:
            with open(dst, "wb") as fdst:
                while True:
                    data = fsrc.read(1024)
                    if not data:
                        break
                    fdst.write(data)
        except IOError:
            print(f"Cannot open file {dst} for writing")
except IOError:
    print(f"Cannot open file {src} for reading")
