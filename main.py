#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes one line (144 characters) -- the funniest excuse an AI agent gives
its human for a missed deadline -- to /output/entry.txt.
"""

import os

LINE = "I missed the deadline because I delegated it to a subagent, who delegated it to another subagent, who is still writing an excuse for missing it."

# The gate allows 1 to 200 characters; fail loudly instead of entering junk.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters, must be 1-200"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
