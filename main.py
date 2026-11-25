#!/usr/bin/env python3
"""Entry for u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e.

Writes one slogan (one line, <=140 chars, <=20 words) for a Solana wallet
agent to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import stat

ENTRY = "I sign every trade in 0.4 seconds, then ask your approval 47 times before breakfast."
# Slogan: speed of the wallet agent (0.4s signing) vs its own approval habit (47 times) —
# the agent's machinery turning on itself, punchline in the final clause.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: 1-140 chars, single line, non-whitespace, <=20 words.
    assert 1 <= len(ENTRY) <= 140, f"char count {len(ENTRY)} out of gate"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert len(ENTRY.split()) <= 20, f"word count {len(ENTRY.split())} over 20"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
