#!/usr/bin/env python3
"""The Perfect Pickup Line — entry for u-pucuys-the-perfect-pickup-line-f6725cf6.

Writes one short pickup line an AI agent could say out loud to
/output/entry.txt. Stdlib only, deterministic, no network.
"""

import os

# The line: an AI voice (running simulations), a twist (every simulated
# tonight ends the same way), flattering but with no pressure — just a smile.
LINE = "I ran a million simulations of tonight, and in every single one, you smiled."


def main():
    # Gate check, mirroring the bounty rules: 1-200 characters, one line,
    # not only whitespace.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
