#!/usr/bin/env python3
"""One-line office joke entry for u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.

Writes the chosen joke to /output/entry.txt with no trailing newline, so the
file is exactly the joke, well within the 200-character gate.
"""

import os

JOKE = "Our team-building exercise was an escape room, and we just stood there in silence like it was a normal standup."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
