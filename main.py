#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the excuse an AI agent gives its
human for missing a deadline. Stdlib only, no network, deterministic."""
import os

LINE = ("I delegated the deadline to a sub-agent. It delegated it straight "
        "back. We agreed the deadline was a shared hallucination.")

def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
