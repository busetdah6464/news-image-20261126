#!/usr/bin/env python3
"""news-image-20261126 entry: copy the pre-rendered entry.png to /output.

Standard library only. The image was drawn locally with Pillow by
render.py (see VERIFIKASI.md for the sourced stories); this program
only copies the finished bytes, so the two grader runs are identical.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")


def main():
    if not os.path.isfile(SRC):
        print("missing " + SRC, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(SRC, OUT)
    if os.path.getsize(SRC) != os.path.getsize(OUT):
        print("copy mismatch: " + OUT, file=sys.stderr)
        return 1
    print("wrote " + OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
